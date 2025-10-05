import random
from mood_analyzer import analyze_mood, detect_lang

# -------------------------------------------------------------
# 1️⃣ Mẫu phản hồi tiếng Việt – kiểu “bạn tâm sự”
# -------------------------------------------------------------
def _vi_supportive(mood: str) -> str:
    templates = {
        "sad": [
            "Nghe như bạn đang buồn… 🌧️ Buồn là cảm xúc rất bình thường. Bạn thử hít sâu một chút, hoặc kể mình nghe điều khiến bạn buồn được không?",
            "Mình hiểu cảm giác đó mà. Nếu muốn, bạn có thể kể thêm cho mình nghe – mình ở đây để lắng nghe bạn 🌿.",
        ],
        "anxious": [
            "Có vẻ bạn đang thấy lo lắng 😥. Mình hiểu cảm giác đó. Thử hít vào sâu 4 giây, thở ra 6 giây nhé. Mình sẽ cùng bạn tìm hướng giải quyết.",
            "Lo âu là cảm xúc dễ đến mà khó đi, nhưng bạn không một mình đâu. Mình ở đây cùng bạn 🍀.",
        ],
        "angry": [
            "Có vẻ bạn đang giận ai đó hoặc chuyện gì đó 😤. Hít thở sâu nào, rồi kể mình nghe – đôi khi nói ra sẽ nhẹ hơn.",
            "Tức giận cũng là phản ứng tự nhiên thôi. Bạn muốn mình cùng giúp sắp xếp lại suy nghĩ không?",
        ],
        "stressed": [
            "Áp lực quá nhiều làm ai cũng mệt 😮‍💨. Thử tạm nghỉ 5 phút nhé, rồi làm từng việc nhỏ một thôi.",
            "Công việc, học tập hay mối quan hệ đều có thể khiến mình căng thẳng. Bạn đang gặp chuyện gì vậy?",
        ],
        "lonely": [
            "Cảm giác cô đơn thật không dễ chịu 😔. Nhưng bạn không hề một mình đâu – mình đang ở đây.",
            "Nếu bạn muốn nói chuyện, mình sẵn sàng lắng nghe 🫶.",
        ],
        "tired": [
            "Bạn mệt rồi hả… 😴 Nghỉ ngơi một chút cũng được mà, cơ thể cần được quan tâm nữa.",
            "Mình hiểu cảm giác đó. Bạn thử uống tí nước và duỗi người nhẹ nhé 🌙.",
        ],
        "happy": [
            "Thật vui khi nghe điều đó đó 😄! Giữ tâm trạng này cả ngày nhé!",
            "Tuyệt vời! Hạnh phúc nhỏ cũng đáng trân trọng lắm 🌈.",
        ],
        "neutral": [
            "Cảm ơn bạn đã chia sẻ 🌿. Mình ở đây nghe bạn nè, có chuyện gì trong lòng không?",
            "Bạn muốn kể thêm cho mình nghe không? Mình ở đây, bình tĩnh và không phán xét 🤝.",
        ],
    }
    return random.choice(templates.get(mood, templates["neutral"]))


# -------------------------------------------------------------
# 2️⃣ Mẫu phản hồi tiếng Trung – kiểu “朋友式倾听”
# -------------------------------------------------------------
def _zh_supportive(mood: str) -> str:
    templates = {
        "sad": [
            "聽起來你有點難過 🌧️，我在這裡聽你說。",
            "有時候難過也沒關係，慢慢說給我聽吧 💙。",
        ],
        "anxious": [
            "你是不是有點焦慮？深呼吸一下，好嗎？一切都會慢慢好起來的 🍀。",
            "別太擔心，我懂你的感覺，我會在這裡陪你。",
        ],
        "angry": [
            "看起來你很生氣 😤，先深呼吸一下吧。",
            "生氣的時候先停一下，等情緒平穩了我們再聊，好嗎？",
        ],
        "stressed": [
            "壓力太大真的很累 😮‍💨，要不要休息五分鐘？",
            "我知道那種感覺，別太逼自己了，放鬆一下吧。",
        ],
        "lonely": [
            "覺得孤單嗎？沒關係，我在這裡陪你 🫶。",
            "有時候孤單只是想被理解的心在說話，我懂。",
        ],
        "tired": [
            "好累喔 💭，今天真的辛苦了，早點休息吧。",
            "身體在提醒你該休息了，閉上眼睛放鬆一下 🌙。",
        ],
        "happy": [
            "太好了！聽到你開心我也替你高興 😄。",
            "這樣真好～保持這份好心情喔 🌈。",
        ],
        "neutral": [
            "謝謝你分享，我在聽喔 🙂。",
            "說說看吧，我想聽你的故事。",
        ],
    }
    return random.choice(templates.get(mood, templates["neutral"]))


# -------------------------------------------------------------
# 3️⃣ Hàm tổng hợp: trả lời phù hợp với ngôn ngữ và cảm xúc
# -------------------------------------------------------------
def generate_ai_reply(user_text: str, lang: str) -> str:
    """
    Trả lời thông minh, ấm áp như một người bạn.
    Dựa vào ngôn ngữ (lang) và cảm xúc được nhận diện.
    """
    mood = analyze_mood(user_text, lang)
    return _zh_supportive(mood) if lang == "zh" else _vi_supportive(mood)

