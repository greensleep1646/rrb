from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("""
    Konum Bulma Aracı İşlevini Kullanın
    
    Konum Bulma Aracının İşlevleri:
    
    1. Kullanıcı Adı ile Konum Bulma
    2. Telegram Gruplarını Bulma
    3. Telegram Kanalını Bulma
    
    Lütfen İlk İşlevinizi Seçin:
    """)

def select_function(update, context):
    user_input = update.message.text.lower()
    if user_input in ["1", "kullanıcı adı ile konum bulma"]:
        find_user(update, context)
    elif user_input in ["2", "telegram gruplarını bulma"]:
        find_groups(update, context)
    elif user_input in ["3", "telegram kanalını bulma"]:
        find_channels(update, context)
    else:
        update.message.reply_text("Lütfen Doğru Seçim Yapınız!")

def find_user(update, context):
    update.message.reply_text("""
    Konum Bulma Aracının İkinci İşlevi:
    
    Kullanıcı Adı ile Konum Bulma
    
    Lütfen Kullanıcı Adını Girin:
    """)

def get_user_name(update, context):
    user_input = update.message.text.lower()
    user_name = user_input.split(" ")[0]
    return user_name

def find_user_location(user_name):
    # Your code to
