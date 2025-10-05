
import re

def detect_lang(text: str) -> str:
    if re.search(r"[\u4e00-\u9fff]", text):
        return "zh"
    vi_diacritics = "ăâđêôơưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
    if any(ch in text.lower() for ch in vi_diacritics):
        return "vi"
    return "vi"

VI_NEG = {
    "sad": ["buồn", "chán", "tủi", "mất mát", "khóc"],
    "anxious": ["lo", "lo âu", "bồn chồn", "hoảng", "sợ"],
    "angry": ["giận", "tức", "cay", "bực"],
    "stressed": ["stress", "căng thẳng", "áp lực", "quá tải", "mệt mỏi"],
    "lonely": ["cô đơn", "một mình", "lạc lõng"],
    "tired": ["mệt", "kiệt sức", "đuối"],
    "happy": ["vui", "hạnh phúc", "tuyệt"],
}

ZH_NEG = {
    "sad": ["難過", "傷心", "沮喪", "流淚", "失落"],
    "anxious": ["焦慮", "緊張", "不安", "恐慌", "害怕"],
    "angry": ["生氣", "憤怒", "火大", "氣死"],
    "stressed": ["壓力", "累爆", "過勞", "好累", "疲倦"],
    "lonely": ["孤單", "孤獨", "沒人懂"],
    "tired": ["累", "疲憊", "精疲力盡"],
    "happy": ["開心", "幸福", "太棒了"],
}

def analyze_mood(text: str, lang: str) -> str:
    text_l = text.lower()
    lex = ZH_NEG if lang == "zh" else VI_NEG
    for label, kws in lex.items():
        for kw in kws:
            if kw in text_l:
                return label
    return "neutral"
