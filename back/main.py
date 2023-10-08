from telebot import types
from telebot.types import LabeledPrice
import telebot

bot = telebot.TeleBot('token')
provider_token = 'provider_token'

prices = {
    LabeledPrice(label='Pet food', amount=5750), LabeledPrice('Medicines', 5000)
}


def webAppKeyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    webAppTest = types.WebAppInfo(
        "https://bobrov.dev/pacman-pwa/index.html")
    webAppGame = types.WebAppInfo(
        "https://rolling-scopes-school.github.io/infraket-JSFE2022Q1/shelter/pages/main/main.html")
    one_button = types.KeyboardButton(text="Game page", web_app=webAppTest)
    two_button = types.KeyboardButton(text="Shelter", web_app=webAppGame)
    keyboard.add(one_button, two_button)

    return keyboard


def webAppKeyboardInline():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    webApp = types.WebAppInfo("https://bobrov.dev/pacman-pwa/index.html")
    one = types.InlineKeyboardButton(text="WebApp", web_app=webApp)
    keyboard.add(one)

    return keyboard


@bot.message_handler(commands=['start'])
def start_fun(message):
    bot.send_message(message.chat.id, 'Hello, I am miniapps bot!', parse_mode="Markdown",
                     reply_markup=webAppKeyboard())


@bot.message_handler(content_types='web_app_data')
def command_pay(web_app_message):
    bot.send_message(web_app_message.chat.id,
                     text="Pay"
                     )
    bot.send_invoice(
        chat_id=web_app_message.chat.id,
        title='Donate',
        description='Donate to the shelter',
        invoice_payload='g',
        provider_token=provider_token,
        currency='usd',
        prices=prices,
    )



if __name__ == '__main__':
    bot.infinity_polling()
