def send_messages(messages, send_message):
    while messages:
        current_message = messages.pop()
        print("sending message: ", current_message)
        send_message.append(current_message)