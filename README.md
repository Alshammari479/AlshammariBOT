# AlshammariBOT 🤖

بوت ديسكورد شامل مع جميع الأدوات اللي تحتاجها لإدارة السيرفر!

## 🚀 الميزات

✅ نظام الترحيب التلقائي
✅ نظام التذاكر
✅ أوامر الإدارة (Ban, Kick, Timeout, Warn)
✅ نظام التسجيل
✅ أوامر Slash Commands
✅ إعدادات منفصلة لكل سيرفر

## 📋 المتطلبات

- Python 3.8+
- pip

## 🔧 التثبيت والتشغيل

### 1️⃣ استنساخ المستودع
```bash
git clone https://github.com/Alshammari479/AlshammariBOT.git
cd AlshammariBOT
```

### 2️⃣ تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### 3️⃣ إعداد المتغيرات البيئية
```bash
cp .env.example .env
```

### 4️⃣ إضافة التوكن
افتح ملف `.env` وأضف:
```
DISCORD_TOKEN=your_bot_token_here
```

### 5️⃣ التشغيل
```bash
python main.py
```

## 📖 كيفية الحصول على Bot Token

1. اذهب إلى [Discord Developer Portal](https://discord.com/developers/applications)
2. انقر على "New Application"
3. اكتب اسم التطبيق (AlshammariBOT)
4. اذهب إلى "Bot" من الجانب الأيسر
5. انقر على "Add Bot"
6. تحت "TOKEN" انقر "Copy"
7. الصق التوكن في ملف `.env`

## 🔐 إضافة البوت للسيرفر

1. في Developer Portal، اذهب إلى OAuth2 > URL Generator
2. اختر Scopes: `bot`
3. اختر Permissions:
   - `Send Messages`
   - `Manage Messages`
   - `Kick Members`
   - `Ban Members`
   - `Timeout Members`
   - `Manage Roles`
   - `Create Public Threads`
4. انسخ الرابط واضغط عليه لإضافة البوت

## 📁 هيكل المشروع

```
AlshammariBOT/
├── main.py              # ملف التشغيل الرئيسي
├── config.py            # الإعدادات
├── requirements.txt     # المكتبات المطلوبة
├── .env.example         # مثال ملف البيئة
├── .gitignore          # ملفات التجاهل
└── cogs/               # الأوامر والأنظمة
    ├── help.py         # نظام المساعدة
    ├── moderation.py   # أوامر الإدارة
    ├── welcome.py      # نظام الترحيب
    └── tickets.py      # نظام التذاكر
```

## 📝 الأوامر الحالية

- `/help` - عرض جميع الأوامر
- `/ban @user reason` - حظر عضو
- `/kick @user reason` - طرد عضو
- `/timeout @user minutes reason` - إيقاف مؤقت
- `/warn @user reason` - تحذير عضو
- `/clear count` - حذف رسائل
- `/setup_welcome #channel` - تعيين قناة الترحيب
- `/create_ticket subject` - إنشاء تذكرة

## 🤝 المساهمة

أنت مرحباً بك تساهم في المشروع!

## 📄 الترخيص

هذا المشروع مرخص تحت MIT License

## 👨‍💻 المطور

Alshammari479
