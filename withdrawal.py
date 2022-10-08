from datetime import datetime
import uuid

def with_insert(username, with_amnt, new_user, with_amnt_sum, rec, rec1):
    now = datetime.now()
    date = str(now)
    trans = uuid.uuid4()
    trans_id = str(trans)
    if with_amnt <= new_user[2]:
        if with_amnt_sum < 50000:
            total_amnt = new_user[2] - with_amnt
            obj = {
                "_id": trans_id,
                "Aadhar": username,
                "Name": new_user[0],
                "Account Type": new_user[1],
                "Date": date,
                "Deposit/Withdrawal": "Withdrawal",
                "Amount": with_amnt,
                "Total Balance": total_amnt
            }
            rec1.insert_one(obj)
            print('You have Withdrawn', with_amnt, 'under the Transaction Id', trans_id)
            print('Your Total Balance is: ', total_amnt)
            reg_update(username, total_amnt, rec)
        else:
            print('You Already have exceeded the Withdrawal Limit, Please Withdraw after 24 Hours!!')
    else:
        print('Insufficient Balance!!')


def reg_update(username, total_amnt, rec):
    myquery = {"_id": username}
    new_values = {"$set": {"Total Balance": total_amnt}}
    rec.update_one(myquery, new_values)


def main(username,rec,rec1):
    with_amnt = int(input('Enter the Amount to be Withdrawn: '))
    with_amnt_sum = 0
    now = datetime.now()
    date = str(now)
    for details_user in rec.find({"_id": username}, {'_id': 0, 'Name': 1, 'Account Type': 1, 'Total Balance': 1}):
        res_user = details_user.values()
        new_user = list(res_user)
    for details_user in rec1.find({"Aadhar": username, },
                                  {'_id': 0, 'Date': 1, 'Deposit/Withdrawal': 1, 'Amount': 1}):
        with_tran = details_user.values()
        with_user = list(with_tran)
        if with_user[0][:10] == date[:10] and with_user[1] == 'Withdrawal':
            with_amnt_sum += with_user[2]
    with_insert(username,with_amnt, new_user, with_amnt_sum, rec, rec1)