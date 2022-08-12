def show_messages(messages, sent_messages):
    if messages:
        for message in messages:
            print("not sent messages: ", message)
    if sent_messages:
        for message in sent_messages:
            print("sent messages: ", message)