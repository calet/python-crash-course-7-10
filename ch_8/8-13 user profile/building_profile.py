def build_profile(first, last, middle = "", **user_info):
    user_info['first name'] = first
    if middle:
        user_info['middle name'] = middle
    user_info['last_name'] = last
    return user_info
