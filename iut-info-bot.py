from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def start(update, context):
    user = update.message.from_user

    keyboard = [
        [
            KeyboardButton('About'),
            KeyboardButton('Location')
        ],
        [
            KeyboardButton('Contact')
        ]
    ]

    update.message.reply_html('Hello <b>{}</b>\n\nWelcome to IUT Info Bot!'.format(user.first_name),
                              reply_markup= ReplyKeyboardMarkup(keyboard))

def about(update, context):
    update.message.reply_text('')

def location(update, context):

    button = [
        [InlineKeyboardButton('Address', callback_data='2')]
    ]
    #update.message.reply_html("Inha University in Tashkent is located at: \n\n<b>9, Ziyolilar Street, Mirzo Ulug'bek district</b>",
    #                           reply_markup=InlineKeyboardMarkup(button))

    update.message.reply_location(latitude="41.3385666855", longitude="69.3344961943", reply_markup=InlineKeyboardMarkup(button) )

def map_iut(update, context):
    query = update.callback_query
    query.answer()
    query.message.reply_html("Inha University in Tashkent is located at: \n<b>9, Ziyolilar Street, Mirzo Ulug'bek district</b>")

def contact(update, context):

    update.message.reply_html(
    """     
    Office: <b>Ziyolilar str 9, M.Ulugbek</b>\n
    Phone:  <b>+998 71 289 99 99</b>
    Fax:    <b>+998 71 269 00 58</b>\n
    For more infomation visit wesite:\n \t\t<b>www.inha.uz</b>
    """)

def main():
    updater = Updater('5462884979:AAHkCjLQupRu4SW2_so0wGj7mYiXInb1oIM', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text('About') & ~Filters.command, about))
    dispatcher.add_handler(MessageHandler(Filters.text('Location') & ~Filters.command, location))
    dispatcher.add_handler(MessageHandler(Filters.text('Contact') & ~Filters.command, contact))
    dispatcher.add_handler(CallbackQueryHandler(map_iut))

    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()
