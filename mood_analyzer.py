import re
import random

# -------------------------------------------------------------
# 1️⃣ Hàm nhận diện ngôn ngữ: tiếng Trung hoặc tiếng Việt
# -------------------------------------------------------------
def detect_lang(text: str) -> str:
    """Nhận diện ngôn ngữ người dùng (zh hoặc vi)"""
    if re.search(r"[\u4e00-\u9fff]", text):
        return "zh"  # Có ký tự Trung
    vi_diacritics = "ăâđêôơưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
    if any(ch in text.lower() for ch in vi_diacritics):
        return "vi"
    return "vi"

# -------------------------------------------------------------
# 2️⃣ Từ khóa cảm xúc
# -------------------------------------------------------------
VI_MOODS = {
    "sad": ["buồn", "chán", "tủi", "mất mát", "khóc", "tệ"],
    "anxious": ["lo", "lo âu", "bồn chồn", "sợ", "hoảng"],
    "angry": ["giận", "tức", "bực", "cay"],
    "stressed": ["stress", "căng thẳng", "mệt mỏi", "áp lực"],
    "lonely": ["cô đơn", "một mình", "lạc lõng"],
    "tired": ["mệt", "đuối", "kiệt sức"],
    "happy": ["vui", "hạnh phúc", "tốt", "vui vẻ"],
}

ZH_MOODS = {
    "sad": ["難過", "傷心", "沮喪", "失落"],
    "anxious": ["焦慮", "緊張", "不安", "害怕"],
    "angry": ["生氣", "憤怒", "氣死"],
    "stressed": ["壓力", "疲倦", "累爆", "好累"],
    "lonely": ["孤單", "孤獨", "沒人懂"],
    "tired": ["累", "疲憊", "精疲力盡"],
    "happy": ["開心", "幸福", "太棒了"],
}

# -------------------------------------------------------------
# 3️⃣ Hàm phân tích cảm xúc
# -------------------------------------------------------------
def analyze_mood(text: str, lang: str) -> str:
    """Dò cảm xúc dựa trên từ khóa"""
    text_l = text.lower()
    lex = ZH_MOODS if lang == "zh" else VI_MOODS
    for label, kws in lex.items():
        for kw in kws:
            if kw in text_l:
                return label
    return "neutral"

# -------------------------------------------------------------
# 4️⃣ Hàm tạo phản hồi tự nhiên
# -------------------------------------------------------------
def generate_friend_like_reply(text: str, mood: str, lang: str) -> str:
    """Tạo phản hồi giống người bạn (ngắn gọn, ấm áp)"""
    if lang == "vi":
        replies = {
            "sad": [
                "Nghe như bạn đang buồn… muốn kể mình nghe thêm không?",
                "Thỉnh thoảng buồn một chút cũng được, bạn không cô đơn đâu.",
                "Mình ở đây nè, cứ chia sẻ thoải mái nhé.",
            ],
            "anxious": [
                "Nghe có vẻ bạn đang lo lắng… có chuyện gì khiến bạn như vậy à?",
                "Mọi chuyện rồi sẽ ổn thôi, hít thở sâu một chút nhé.",
            ],
            "angry": [
                "Có vẻ bạn đang tức giận, thử nghỉ ngơi chút xem sao?",
                "Đôi khi im lặng một chút cũng giúp mình bình tâm hơn đó.",
            ],
            "stressed": [
                "Nghe mệt ghê, bạn làm việc nhiều quá hả?",
                "Đừng quên nghỉ ngơi nhé, mình tin bạn làm được.",
            ],
            "lonely": [
                "Bạn thấy cô đơn hả… Mình vẫn ở đây cùng bạn nè.",
                "Cảm giác đó khó chịu thật, nhưng bạn không một mình đâu.",
            ],
            "tired": [
                "Bạn mệt rồi hả? Nghỉ ngơi chút đi nhé.",
                "Mình hiểu cảm giác đó mà, cố gắng ít thôi, bạn xứng đáng được nghỉ ngơi.",
            ],
            "happy": [
                "Thật vui khi nghe điều đó đó!",
                "Tuyệt vời! Mình mừng cho bạn nha 😊",
            ],
            "neutral": [
                "Mình đang nghe nè, bạn muốn nói gì thêm không?",
                "Cảm ơn bạn đã chia sẻ, mình ở đây cùng bạn.",
            ],
        }
    else:  # zh
        replies = {
            "sad": ["聽起來你好像有點難過，我在這裡陪你。", "有時候傷心也沒關係，我都在。"],
            "anxious": ["你是不是有點緊張？沒事的，一切都會好起來。", "深呼吸一下，好嗎？我在聽。"],
            "angry": ["看起來你很生氣，先冷靜一下吧。", "有時候發脾氣也沒什麼的，我懂。"],
            "stressed": ["壓力太大了嗎？別太勉強自己喔。", "辛苦了，記得要休息一下。"],
            "lonely": ["覺得孤單嗎？我在這裡陪你。", "有我在，不用怕孤單。"],
            "tired": ["好累喔，休息一下吧。", "你做得已經很好了，別太逼自己。"],
            "happy": ["太棒了！聽起來你很開心呢！", "好開心聽到你這麼說 😊"],
            "neutral": ["我在聽喔，說說看吧。", "謝謝你分享給我。"],
        }

    return random.choice(replies.get(mood, replies["neutral"]))

