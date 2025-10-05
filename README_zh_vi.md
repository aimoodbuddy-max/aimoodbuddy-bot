
# AI Mood Buddy (ZH/VI) — FastAPI + LINE

## Quick Start
1) `pip install -r requirements.txt`
2) Copy `.env.example` to `.env` and paste your tokens
3) Run: `uvicorn main:app --reload --port 8000`
4) In another terminal: `ngrok http 8000`
5) Set Webhook URL in LINE Developers -> Messaging API -> `https://<ngrok>.ngrok.io/callback`
6) Turn ON "Use webhook" -> Verify
