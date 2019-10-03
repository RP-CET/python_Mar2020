import sys
import time
import telepot
from telepot.loop import MessageLoop

TOKEN = 'Your Token'

# Define the information to return per command
def get_help():
    msg = '''
    Use one of the following commands:
        help: To show this help
        offers: To see this week offers
        events: To see this week events
    '''
    return msg

def get_offers():
    msg = '''
    This week enjoy these amazing offers!
        20% discount in beach products
        15% discount if you spend more than $50
    '''
    return msg

def get_events():
    msg = '''
    Join us for an incredible party the Thursday in our Marina Bay Sands shop!
    '''
    return msg

COMMANDS = {
    'help': get_help,
    'offers': get_offers,
    'events': get_events,
}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type != 'text':
        bot.sendMessage(chat_id, "I don't understand you.\nPlease type 'help' for options")
        return

    elif content_type == 'text':
        # Make the commands case insensitive
        command = msg['text'].lower()
        if command not in COMMANDS:
            bot.sendMessage(chat_id,"I don't understand you.\nPlease type 'help' for options")
            return
        message = COMMANDS[command]()
        bot.sendMessage(chat_id,message)
        
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)