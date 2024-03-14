def strong_password(password):
    regex_count = 0
    for regex in regex_list:
        if regex.search(password) is None:
            print('Sorry, your password is not strong enough')
            break
        else:
            regex_count += 1
            continue
    if regex_count is 4:
        print('Congrats. Your password is strong enough!')
