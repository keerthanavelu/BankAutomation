from datetime import datetime
import uuid
import login as log


def reg_insertion(name, aadhar, password, pan, mobile, mail, acnt_type, deposit,rec):
    obj = {
            "_id": aadhar,
            "Password": password,
            "Name": name,
            "Pan Number": pan,
            "Mobile Number": mobile,
            "Mail": mail,
            "Account Type": acnt_type,
            "Total Balance": int(deposit)
    }
    rec.insert_one(obj)

def tran_insertion(name, aadhar, acnt_type, deposit, rec1):
    now = datetime.now()
    date = str(now)
    trans = uuid.uuid4()
    trans_id = str(trans)
    obj = {
        "_id": trans_id,
        "Aadhar": aadhar,
        "Name": name,
        "Account Type": acnt_type,
        "Date": date,
        "Deposit/Withdrawal": "Deposit",
        "Amount": int(deposit),
        "Total Balance": int(deposit)
    }
    rec1.insert_one(obj)