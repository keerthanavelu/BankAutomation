import main
import registration as reg
import deposit as dep
import withdrawal as wd


def login(username, password, user_list, pas_list):
    if username in user_list:
        if password in pas_list:
            print('Login Successful!!')
        else:
            print('Wrong Password!!')
            password = input('Enter the Password: ')
            login(username, password, user_list, pas_list)
    else:
        print('No Username Registered!!')
        print('1. Register')
        print('2. Exit')
        option = int(input('Enter the Option: '))
        wrong_option(option)


def wrong_option(option):
    if option == 1:
        reg.main()
    elif option == 2:
        exit()
    else:
        print('Enter the Correct Option: ')
        print('1. Register')
        print('2. Exit')
        option = int(input('Enter the Option: '))
        wrong_option(option)


def login_option(username, rec, rec1):
    print('1. Withdrawal')
    print('2. Deposit')
    print('3. Mini Statement')
    print('4. Display Total Balance')
    print('5. Update')
    print('6. Logout')
    log_option = int(input('Enter the Option: '))
    if log_option == 1:
        wd.main(username,rec,rec1)
    elif log_option == 2:
        dep.main(username, rec, rec1)
    elif log_option == 3:
        pass
    elif log_option == 4:
        for details_amnt in rec.find({"_id": username}, {'_id': 0, 'Total Balance': 1}):
            total_amnt = details_amnt.values()
            total_bal = list(total_amnt)
        print('Your Total Balance is: ', total_bal[0])
        login_option(username, rec, rec1)
    elif log_option == 5:
        pass
    elif log_option == 6:
        exit()
        main.main()
    else:
        print('Enter the Correct Option:')
        login_option(username,rec,rec1)


def main(rec, rec1):
    username = input("Enter your Aadhar Number: ")
    password = input("Enter your Password: ")
    user_list = []
    for details_user in rec.find({"_id": username}, {'_id': 1}):
        res_user = details_user.values()
        new_user = list(res_user)
        user_list.append(new_user[0])
    pas_list = []
    for details_pas in rec.find({"_id": username}, {'_id': 0}):
        res_pas = details_pas.values()
        new_pas = list(res_pas)
        pas_list.append(new_pas[0])
    login(username, password, user_list, pas_list)
    login_option(username, rec, rec1)
