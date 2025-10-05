
def _vi_supportive(mood: str) -> str:
    templates = {
        "sad": "Mình nghe bạn nói và cảm nhận được nỗi buồn của bạn 🌧️. Buồn là cảm xúc rất bình thường khi mọi thứ dồn dập. Bạn thử đặt tay lên ngực, hít vào sâu 4 giây, thở ra 6 giây trong 6 vòng nhé. Nếu muốn, mình ở đây để nghe bạn kể thêm.",
        "anxious": "Có vẻ bạn đang thấy lo âu và bồn chồn 😥. Thử viết ra 3 điều bạn có thể kiểm soát ngay lúc này và 3 điều bạn tạm gác lại. Mình sẽ đồng hành cùng bạn qua từng bước nhỏ.",
        "angry": "Mình hiểu cảm giác bực tức của bạn 🔥. Hãy cho phép bản thân dừng 1 phút, hít sâu, thả lỏng vai. Khi sẵn sàng, mình giúp bạn sắp xếp lại suy nghĩ theo hướng xây dựng nhé.",
        "stressed": "Áp lực chồng chất thật mệt phải không 😮‍💨. Mình gợi ý phiên tập trung 25 phút + nghỉ 5 phút (Pomodoro). Bắt đầu bằng việc nhỏ nhất và mình sẽ nhắc bạn nghỉ đúng nhịp.",
        "lonely": "Cô đơn là tín hiệu bạn cần được kết nối 🫶. Bạn muốn nhắn một người thân quen không? Mình có thể gợi ý một lời mở đầu dịu dàng.",
        "tired": "Cơ thể bạn đang đòi nghỉ ngơi 💤. Thử đặt báo thức đi ngủ sớm hôm nay, tắt màn hình 30 phút trước khi ngủ nhé.",
        "happy": "Mừng vì bạn đang thấy tích cực 🌈! Viết nhanh 1–2 điều làm bạn vui hôm nay để giữ năng lượng này nào!",
        "neutral": "Cảm ơn bạn đã chia sẻ 🌿. Bạn đang quan tâm điều gì lúc này? Mình có thể gợi ý vài bước nhỏ để thấy dễ chịu hơn."
    }
    return templates.get(mood, templates["neutral"])

def _zh_supportive(mood: str) -> str:
    templates = {
        "sad": "我聽見你的心情了，今天真的不好受 🌧️。難過是很正常的情緒，先把手放在胸前，吸氣4秒、吐氣6秒做6輪，好嗎？想說更多，我都在。",
        "anxious": "你似乎正感到焦慮與不安 😥。試著寫下此刻你能掌控的3件事，以及可以暫時放下的3件事；一步一步來，我陪你。",
        "angry": "我懂你在生氣 🔥。先停一下，深呼吸，放鬆肩膀。等準備好，我們再把事情理清，換個建設性的角度看。",
        "stressed": "壓力好多真的很累 😮‍💨。要不要試試25分鐘專注＋5分鐘休息（番茄鐘）？從最小的步驟開始，我會提醒你休息。",
        "lonely": "孤單其實是在提醒自己需要連結 🫶。要不要傳個訊息給熟悉的人？我可以幫你想一段溫柔的開場白。",
        "tired": "身體在跟你要休息了 💤。今晚提早睡，睡前30分鐘關螢幕，讓自己慢慢安靜下來。",
        "happy": "替你感到開心 🌈！把今天1–2件讓你開心的小事寫下來，留住這份能量～",
        "neutral": "謝謝你分享 🌿。此刻你最在意的是什麼呢？我可以給你一些小步驟，讓心情更好。"
    }
    return templates.get(mood, templates["neutral"])

def generate_supportive_reply(user_text: str, mood: str, lang: str) -> str:
    return _zh_supportive(mood) if lang == "zh" else _vi_supportive(mood)

def generate_general_reply(user_text: str, lang: str) -> str:
    if lang == "zh":
        return f"你想問的是：「{user_text}」對嗎？若需要更完整的答案，告訴我你的情境或限制；我也可以先給你三個可行做法。"
    else:
        return f"Bạn đang hỏi: “{user_text}”, đúng không? Nếu cần trả lời cụ thể hơn, cho mình biết bối cảnh/giới hạn nhé. Mình cũng có thể gợi ý nhanh 3 hướng làm."
