import re


def aadhar_validation(aadhar):
    regex = r'^\d{4}\s\d{4}\s\d{4}$'
    if re.fullmatch(regex, aadhar):
        return True
    else:
        return False


def pas_validation(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&?*&])[A-Za-z\d@#$%&?*&]{5,16}$'
    if re.fullmatch(regex, password):
        return True
    else:
        return False


def pan_validation(pan):
    regex = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.fullmatch(regex, pan):
        return True
    else:
        return False


def mobile_validation(mobile):
    regex = r'^[7-9][0-9]{9}$'
    if re.fullmatch(regex, mobile):
        return True
    else:
        return False


def mail_validation(mail):
    regex = r'\b[A-Za-z0-9]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, mail):
        return True
    else:
        return False


def acnt_validation(acnt_type):
    regex = r'^[S]{1}[B]{1}$'
    if re.fullmatch(regex, acnt_type):
        return True
    else:
        return False
