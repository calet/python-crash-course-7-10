from showM import *
from sendM import *

messages = ['hello', 'hello there', 'welcome', 'welcome home']
sent_messages = []

def send_messages(messages, send_message):
    while messages:
        current_message = messages.pop()
        print("sending message: ", current_message)
        send_message.append(current_message)

copied_messages = messages[:]  
show_messages(copied_messages=copied_messages, messages=messages)
send_messages(copied_messages, sent_messages)
show_messages(sent_messages=sent_messages)