
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from utils.mood_analyzer import detect_lang, analyze_mood
from utils.response_generator import generate_supportive_reply, generate_general_reply

load_dotenv()
CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "")
CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")

if not CHANNEL_SECRET or not CHANNEL_ACCESS_TOKEN:
    print("[WARN] Missing LINE credentials. Fill .env first.")

app = FastAPI(title="AI Mood Buddy - LINE Webhook", version="1.0.0")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN) if CHANNEL_ACCESS_TOKEN else None
handler = WebhookHandler(CHANNEL_SECRET) if CHANNEL_SECRET else None

@app.get("/health")
def health():
    return {"ok": True}

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

@handler.add(MessageEvent, message=TextMessage) if handler else (lambda f: f)
def handle_message(event: MessageEvent):
    user_text = event.message.text.strip()
    lang = detect_lang(user_text)  # 'vi' or 'zh' or 'unk'
    mood = analyze_mood(user_text, lang)

    is_question = user_text.endswith("?") or ("？" in user_text)
    negative = mood in ["sad", "anxious", "angry", "stressed", "lonely", "tired"]
    if is_question and not negative:
        reply = generate_general_reply(user_text, lang)
    else:
        reply = generate_supportive_reply(user_text, mood, lang)

    if line_bot_api:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
