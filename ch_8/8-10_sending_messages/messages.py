import showM 
import sendM

messages = ['hello', 'hello there', 'welcome', 'welcome home']
sent_messages = []

showM.show_messages(messages, sent_messages)
sendM.send_messages(messages, sent_messages)
showM.show_messages(messages, sent_messages)