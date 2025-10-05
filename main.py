
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import load_dotenv
import os

# ===========================================
# 🔹 Khởi tạo
# ===========================================
load_dotenv()
app = FastAPI(title="AI Mood Buddy - LINE Webhook", version="1.0.0")

CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

if not CHANNEL_SECRET or not CHANNEL_ACCESS_TOKEN:
    print("[WARN] Missing LINE credentials. Fill .env first.")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN) if CHANNEL_ACCESS_TOKEN else None
handler = WebhookHandler(CHANNEL_SECRET) if CHANNEL_SECRET else None

# ===========================================
# 🔹 Route test (GET)
# ===========================================
@app.get("/")
def root():
    return {"message": "AI Mood Buddy is running!"}

@app.get("/health")
def health():
    return {"ok": True, "status": "running"}

# ===========================================
# 🔹 Route nhận tin nhắn từ LINE (POST)
# ===========================================
@app.post("/callback")
async def callback(request: Request):
    if handler is None:
        raise HTTPException(status_code=500, detail="Missing LINE credentials")

    signature = request.headers.get("x-line-signature", "")
    body = await request.body()

    try:
        handler.handle(body.decode("utf-8"), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    return JSONResponse({"status": "ok"})   # <-- QUAN TRỌNG! LINE cần 200 OK

# ===========================================
# 🔹 Xử lý message
# ===========================================
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text
    reply_text = f"Bạn vừa nói: {user_text}"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

# ===========================================
# 🔹 Chạy server
# ===========================================
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
