import reg_validation as val
import db_insertion as ins


def aadhar_val(aadhar,rec):
    global aadhar_result
    user_list = []
    for details_user in rec.find({"_id": {'$exists': True}}, {'_id:0'}):
        res_user = details_user.values()
        new_user = list(res_user)
        user_list.append(new_user[0])
    if aadhar in user_list:
        print('Aadhar Number already Exists!!')
        aadhar = input('Enter Your Aadhar Number: ')
        aadhar_val(aadhar,rec)
    else:
        aadhar_valid = val.aadhar_validation(aadhar)
        if len(aadhar) == 14:
            if aadhar_valid:
                print('Valid Aadhar Number')
                aadhar_result = aadhar
            else:
                print('Invalid Aadhar')
                aadhar = input('Enter the Valid Aadhar: ')
                aadhar_val(aadhar,rec)
        else:
            print('Enter the correct length!!')
            aadhar = input('Enter the Valid Aadhar: ')
            aadhar_val(aadhar,rec)
    return aadhar_result


def pas_val(password, re_pas):
    global pas_result
    pas_valid = val.pas_validation(password)
    if password == re_pas:
        if pas_valid:
            print('Valid Password Format')
            pas_result = password
        else:
            password = input('Enter the Password in Correct Format: ')
            pas_val(password, re_pas)
    else:
        print('Re-Entered password is not same as Password!!')
        password = input('Enter the Password:')
        re_pas = input('Re-Enter the Password Again: ')
        pas_val(password, re_pas)
    return pas_result


def pan_val(pan):
    global pan_result
    pan_valid = val.pan_validation(pan)
    if len(pan) == 10:
        if pan_valid:
            print('Valid Pan Number')
            pan_result = pan
        else:
            print('Invalid Pan Number')
            pan = input('Enter the Valid PAN Number: ')
            pan_val(pan)
    else:
        print('Enter the correct length!!')
        pan = input('Enter the Valid PAN Number: ')
        pan_val(pan)
    return pan_result


def mobile_val(mobile):
    global mobile_result
    mobile_valid = val.mobile_validation(mobile)
    if len(mobile) == 10:
        if mobile_valid:
            print('Valid Mobile Number')
            mobile_result = mobile
        else:
            print('Invalid Mobile Number')
            mobile = input('Enter the Valid Mobile Number: ')
            mobile_val(mobile)
    else:
        print('Enter the correct length!!')
        mobile = input('Enter the Valid Mobile Number: ')
        mobile_val(mobile)
    return mobile_result


def mail_val(mail):
    global mail_result
    mail_valid = val.mail_validation(mail)
    if mail_valid:
        print('Valid Mail Id')
        mail_result = mail
    else:
        print('Invalid Mail Id')
        mail = input('Enter the Valid Mail Id: ')
        mail_val(mail)
    return mail_result


def acnt_val(acnt_type):
    global acnt_result
    acnt_valid = val.acnt_validation(acnt_type)
    if len(acnt_type) == 2:
        if acnt_valid:
            print('Valid Account Type')
            acnt_result = acnt_type
        else:
            print('Invalid Account Type')
            acnt_type = input('Enter the Valid Account Type: ')
            acnt_val(acnt_type)
    else:
        acnt_type = input('Enter the Valid Account Type: ')
        acnt_val(acnt_type)
    return acnt_result


def dep_val(deposit):
    global deposit_result
    if len(deposit) >= 4 and 49 <= ord(deposit[0]) <= 57:
        print('Deposited')
        deposit_result = deposit
    else:
        deposit = input('Deposit Should be more than 1000, Enter deposit amount: ')
        dep_val(deposit)
    return deposit_result


def main(rec,rec1):
    name = input('Enter Your FullName: ')
    aadhar = input('Enter Your Aadhar Number: ')
    aadhar_final = aadhar_val(aadhar, rec)
    password = input('Enter the Password: ')
    re_pas = input('Re-Enter the Password: ')
    pas_final = pas_val(password, re_pas)
    pan = input('Enter Your Pan Number: ')
    pan_final = pan_val(pan)
    mobile = input('Enter your Mobile Number: ')
    mobile_final = mobile_val(mobile)
    mail = input('Enter your Mail Id: ')
    mail_final = mail_val(mail)
    acnt_type = input('Enter Account Type (SB): ')
    acnt_final = acnt_val(acnt_type)
    deposit = input('Enter the Amount deposited: ')
    deposit_final = dep_val(deposit)
    ins.reg_insertion(name, aadhar_final, pas_final, pan_final, mobile_final, mail_final, acnt_final, deposit_final, rec)
    ins.tran_insertion(name,aadhar_final,acnt_final,deposit_final,rec1)