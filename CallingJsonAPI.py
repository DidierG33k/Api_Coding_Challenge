import requests as re
import pandas as pd
import numpy as np



def filterUsersByLocation(locationId, data):
    filteredUsers = [user["amount"].replace("$", "").replace(",", "") for user in list(data) if
                     user["location"]["id"] == locationId]
    print(filteredUsers)
    return filteredUsers


def totalTransactions(locationId, transactionType):
    allUsers = []


    for pageNumber in range(16):
        response = re.get('https://jsonmock.hackerrank.com/api/transactions/search?txnType=' + transactionType + '&page=' + str(pageNumber))
        print(response.text)
        data = response.json()["data"]
        print("All the data:",data)




        allUsers.extend(filterUsersByLocation(locationId, data))
        if allUsers == []:
            return [[-1, -1]]
    df = pd.DataFrame(allUsers, columns=["userId", "totalAmount"]).groupby(["userId"])["totalAmount"].agg("sum").reset_index()
    df = df.sort_values('userId', ascending=True)
    return df.values
    print(df.sort_values)
totalTransactions(10,"debit")
