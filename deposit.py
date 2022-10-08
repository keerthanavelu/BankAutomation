from datetime import datetime
import uuid


def reg_update(username, total_amnt, rec):
    myquery = {"_id": username}
    new_values = {"$set": {"Total Balance": total_amnt}}
    rec.update_one(myquery, new_values)


def tran_insert(username, new_user, dep_amnt_sum, dep_amnt, total_amnt, rec, rec1):
    now = datetime.now()
    date = str(now)
    trans = uuid.uuid4()
    trans_id = str(trans)
    if dep_amnt_sum <= 100000:
        obj = {
            "_id": trans_id,
            "Aadhar": username,
            "Name": new_user[0],
            "Account Type": new_user[1],
            "Date": date,
            "Deposit/Withdrawal": "Deposit",
            "Amount": dep_amnt,
            "Total Balance": total_amnt
        }
        rec1.insert_one(obj)
        print('You have Deposited', dep_amnt, 'under the Transaction Id', trans_id)
        print('Your Total Balance is: ', total_amnt)
        reg_update(username, total_amnt, rec)
    else:
        print('You Per Day Deposit Should be less than 1 Lakh, Please Deposit after 24 Hours!!')


def main(username, rec, rec1):
    dep_amnt = int(input('Enter the Amount to be Deposited: '))
    for details_user in rec.find({"_id": username}, {'_id': 0, 'Name': 1, 'Account Type': 1, 'Total Balance': 1}):
        res_user = details_user.values()
        new_user = list(res_user)
    total_amnt = dep_amnt + new_user[2]
    dep_amnt_sum = 0
    now = datetime.now()
    date = str(now)
    for details_user in rec1.find({"Aadhar": username, },
                                  {'_id': 0, 'Date': 1, 'Deposit/Withdrawal': 1, 'Amount': 1}):
        dep_tran = details_user.values()
        dep_user = list(dep_tran)
        if dep_user[0][:10] == date[:10] and dep_user[1] == 'Deposit':
            dep_amnt_sum += dep_user[2]
    tran_insert(username, new_user, dep_amnt_sum, dep_amnt, total_amnt, rec, rec1)
