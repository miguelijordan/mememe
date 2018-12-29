import telebot
import meme_getter
import me3.core.me3_persistence as me3_persistence
import os

TOKEN = "780550229:AAHU8uZnq8B6jmJ-vaapRlRX6KMPIdWf9uY"
SOURCES_FILE = 'meme_sources.dat'
SENT_MEMES = 'SentMemes.dat'

CHAT_ID = "-112216197"

def get_sources():
    with open(SOURCES_FILE, 'r') as f:
        return f.read().splitlines()

def request_memes():
    all_memes = []
    sources = get_sources()
    sources = filter(str.strip, sources)

    for s in sources:
        mg = meme_getter.MemeGetter(s)
        memes = mg.downloadMemes()
        print(s + ': ' + str(len(memes)))

        all_memes += memes

    return all_memes

def send_memes(chat_id, memes):
    for m in memes:
        photo = open(m.url, 'rb')
        bot.send_photo(chat_id, photo)
        photo.close()
        os.remove(m.url)

    me3_persistence.register_memes(memes, SENT_MEMES)

def filter_repeated_memes(all_memes):
    sent_memes = me3_persistence.load_memes(SENT_MEMES)
    filtered_memes = []
    for m in all_memes:
        if m in sent_memes:
            os.remove(m.url)
        else:
            filtered_memes.append(m)
    #filtered_memes = [x for x in all_memes if x not in sent_memes]
    return filtered_memes

def meme_them():
    memes = request_memes()
    memes = filter_repeated_memes(memes)
    if len(memes) == 0:
        bot.reply_to(message, "There's no new memes! Come back later!!")
    else:
        send_memes(CHAT_ID, memes)

if __name__ == '__main__':
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        CHAT_ID = message.chat.id
        print("Chat ID: " + str(CHAT_ID))
        bot.reply_to(message, "Hi! I'm ready to memeü!")

    @bot.message_handler(commands=['mememe'])
    def send_welcome(message):
        chat_id = message.chat.id
        bot.reply_to(message, "Searching for new memes...")
        memes = request_memes()
        memes = filter_repeated_memes(memes)
        if len(memes) == 0:
            bot.reply_to(message, "There's no new memes! Come back later!!")
        else:
            send_memes(chat_id, memes)

    bot.polling()
