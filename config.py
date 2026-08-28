import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot_data.db')

# أعدادات البوت
COMMAND_PREFIX = '/'
BOT_COLOR = 0x2F3136
BOT_NAME = 'AlshammariBOT'

# الأدوار الافتراضية
DEFAULT_ROLES = {
    'citizen': 'مواطن',
    'admin': 'إدارة',
}
