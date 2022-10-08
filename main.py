import pymongo
import registration as reg
import login as log
import forgotpwd as fpwd

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/",)
    db = myclient.bankdb
    rec = db.regdb
    rec1 = db.bnk_tran
    print('1. User')
    print('2. Forgot Password')
    print('3. Exit')
    option = int(input('Enter the option: '))
    if option == 1:
        print('1. Register')
        print('2. Login')
        user_option = int(input('Enter the option: '))
        if user_option == 1:
            reg.main(rec,rec1)
        elif user_option == 2:
            log.main(rec,rec1)
    elif option == 2:
        fpwd.main(rec)
    elif option == 3:
        exit()
    else:
        print('Invalid Option, Please Enter from the Below Options Only')
        main()


if __name__ == '__main__':
    main()
