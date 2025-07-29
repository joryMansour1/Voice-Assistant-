# SmartMethods Voice Assistant 

مشروع Python صوتي، يقوم بتحويل الصوت إلى نص باستخدام Whisper، ثم إرسال النص إلى نموذج لغوي (Cohere) للحصول على رد، ثم تحويل الرد إلى صوت باستخدام RealtimeTTS.

---

## 📁 هيكل المجلد

```
audio-to-text-project/
│
├── main.py                 # الملف الرئيسي لتنفيذ المشروع
├── README.md               # هذا الملف
└── smartmethods-env/       # بيئة Python الافتراضية 
```

---

## 💡 مميزات المشروع

- دعم **اللغة العربية بالكامل**.
- يعمل **محليًا بالكامل** باستثناء نموذج Cohere.
- يدعم **إما تسجيل صوت مباشر من المايك** أو **تشغيل ملف صوتي موجود**.
- مناسب للمشاريع الأكاديمية أو النماذج التجريبية للذكاء الاصطناعي الصوتي.

---

## 🧪 المتطلبات

- Python 3.10+
- ffmpeg
- مفتاح API من [Cohere](https://dashboard.cohere.com/)
- مكتبات Python التالية:
  - `cohere`
  - `openai-whisper`
  - `sounddevice`
  - `scipy`
  - `realtime-tts`

---

## ⚙️ خطوات التشغيل

### 1. إنشاء بيئة افتراضية وتفعيلها:

```bash
cd audio-to-text-project
python3.10 -m venv smartmethods-env
source smartmethods-env/bin/activate  # على macOS/Linux
# .\smartmethods-env\Scripts\activate ← على Windows
```

### 2. تثبيت المكتبات:

```bash
pip install --upgrade pip
pip install cohere openai-whisper sounddevice scipy realtime-tts
```

### 3. تثبيت ffmpeg:

- **macOS**: `brew install ffmpeg`
- **Ubuntu**: `sudo apt install ffmpeg`
- **Windows** (مع Chocolatey): `choco install ffmpeg`

---

## ▶️ تشغيل المشروع

### تسجيل الصوت من المايك (افتراضي):

```bash
python main.py
```

### تشغيل ملف صوتي موجود (input.wav):

1. ضع ملف صوتي باسم `input.wav` في المجلد.
2. داخل `main.py`، غيّر `record_audio()` إلى `use_existing_audio()` في `main()`.

---

## 🧠 مثال تفاعلي

##   تجربة المشروع

[![Demo Video](https://img.icons8.com/color/480/youtube-play.png)](https://drive.google.com/file/d/1cetjgEwxpz_Zd-1tGFG19I98JwTqoIte/view?usp=sharing)

> 🎤 المستخدم: "ما هو عدد كواكب المجموعة الشمسية؟"  
> 🤖 الرد (صوتياً): "ثمانية كواكب."

---

## 🔐 إعداد مفتاح Cohere

في `main.py`، استبدل السطر التالي:

```python
co = cohere.Client("YOUR_COHERE_API_KEY")
```

بمفتاحك الحقيقي من لوحة Cohere:  
👉 https://dashboard.cohere.com/api-keys

---

## 👩‍💻 من تنفيذ

**جوري** – ضمن مشروع تدريبي مع SmartMethods لتطبيقات الذكاء الاصطناعي باللغة العربية.

---