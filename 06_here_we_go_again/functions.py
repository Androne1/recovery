from telegram.ext import CallbackContext
from telegram import Update
import random

def game(update: Update, context: CallbackContext):
    message = update.message.text
    if 'secret_number' not in context.user_data:
        secret_number = random.randint(1000, 9999)
        context.user_data['secret_number'] = secret_number
    secret_number = context.user_data['secret_number']
    # update.message.reply_text(f'Компьютер загадал число {secret_number}')
    
    if not message.isdigit():
        update.message.reply_text('Это не число')
        return None
    elif not len(message) == 4:
        update.message.reply_text('Это не 4-х значное число')
        return None
    secret_number = str(secret_number)
    
    cows = 0
    bulls = 0
    for mesto, chislo in enumerate(secret_number):
        if chislo in message:
            if message[mesto] == chislo:
                bulls += 1
            else:
                cows += 1
    update.message.reply_text(f'В вашем числе {cows} коров и {bulls} быков')
    if bulls == 4:
        update.message.reply_text('Поздравляю! Вы победили, возьмите с полки пирожок')
        del context.user_data['secret_number']