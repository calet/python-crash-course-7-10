def show_messages(copied_messages="", messages="", sent_messages=""):
    if copied_messages:
        for message in copied_messages:
            print("not sent messages: ", message)
    else:
        print("no more copied messages")
    if messages:
        print("messages copied: ", messages)
    if sent_messages:
        for message in sent_messages:
            print("sent messages: ", message)