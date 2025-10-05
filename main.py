import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 🧠 Import các hàm từ mood_analyzer
from mood_analyzer import detect_lang, analyze_mood, generate_friend_like_reply

load_dotenv()
CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "")
CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")

if not CHANNEL_SECRET or not CHANNEL_ACCESS_TOKEN:
    print("[WARN] Missing LINE credentials. Fill .env first.")

app = FastAPI(title="AI Mood Buddy", version="3.0.0")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN) if CHANNEL_ACCESS_TOKEN else None
handler = WebhookHandler(CHANNEL_SECRET) if CHANNEL_SECRET else None


@app.get("/")
def root():
    return {"message": "AI Mood Buddy is running!"}


@app.get("/health")
def health():
    return {"ok": True, "status": "running"}


@app.post("/callback")
async def callback(request: Request):
    if handler is None:
        raise HTTPException(status_code=500, detail="Missing LINE credentials")
    signature = request.headers.get("x-line-signature", "")
    body = (await request.body()).decode("utf-8")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    return JSONResponse({"status": "ok"})


# 🗣️ Khi người dùng gửi tin nhắn
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event: MessageEvent):
    user_text = event.message.text.strip()

    # 🔍 Phát hiện ngôn ngữ
    lang = detect_lang(user_text)

    # 💭 Phân tích cảm xúc
    mood = analyze_mood(user_text, lang)

    # ❤️ Sinh phản hồi tự nhiên, giống người bạn
    reply = generate_friend_like_reply(user_text, mood, lang)

    # Gửi lại tin nhắn
    if line_bot_api:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply)
        )


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)


