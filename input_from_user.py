def get_user_input(typed_mess, user_list):
    
    while True:
        typed_data = input(typed_mess).lower()
        if typed_data in user_list:
            break
        if typed_data == 'all':
            break