import smtplib

def send_mail(temp_pwd):
    pass


def pwddisplay(username,rec):
    user_list = []
    for details_user in rec.find({"_id": {'$exists': True}}, {'_id:0'}):
        res_user = details_user.values()
        new_user = list(res_user)
        user_list.append(new_user[0])
    if username in user_list:
        temp_username = username
        pas_list = []
        for details_pas in rec.find({"_id": temp_username}, {'_id': 0, 'Password': 1}):
            res_pas = details_pas.values()
            new_pas = list(res_pas)
            pas_list.append(new_pas[0])
        temp_pwd = pas_list[0]
        print('Your Password:', temp_pwd)
        send_mail(temp_pwd)
    else:
        print('There is no such User registered with us or Please check your Username')
        process(rec)


def process(rec,username):
    fpwd_option = int(input('Enter Your Option: '))
    if fpwd_option == 1:
        pwddisplay(username, rec)
    elif fpwd_option == 2:
        exit()
    else:
        print('Enter the Correct option:')
        process(rec)


def main(rec):
    username = input('Enter your Username: ')
    print('1. Display Password')
    print('2. Exit')
    process(rec,username)