import requests
import pandas as pd
import numpy as np
import openpyxl

# import json
#
# #no idea how to use pandas with this.
#
# url = "https://api.harvestapp.com/v2/clients?is_active=true&access_token=1634772.pt.xkDqrBxNoPJ762d2eafKMnsaCPxNRK6RI92c_IIwcMEGBNrv7M_Kcky_ppETpqVW2IMeH3kFNKhFH3QCMNDlmg&access_token=1634772.pt.xkDqrBxNoPJ762d2eafKMnsaCPxNRK6RI92c_IIwcMEGBNrv7M_Kcky_ppETpqVW2IMeH3kFNKhFH3QCMNDlmg"
#
# payload={}
# headers = {
#   'Harvest-Account-Id': '951752',
#   'Authorization': '1634772.pt.xkDqrBxNoPJ762d2eafKMnsaCPxNRK6RI92c_IIwcMEGBNrv7M_Kcky_ppETpqVW2IMeH3kFNKhFH3QCMNDlmg'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# # import json to memory as a dataframe
# df = pd.DataFrame(response)
#
# print(df.head())
#
# # save as a csv
# # pd.DataFrame.to_csv("Dataframe")
#
# df.to_csv("chris.csv", index=False, encoding="utf-8", sep="c")

##########

# with open("OriginalPLDetail.csv") as f:
#    print(f)

# To find out what kind of data a column is...
# type(df.Date[0])

# Loads xlsx file.
# df = pd.read_excel("OriginalPLDetail.xlsx", "Profit and Loss Detail", skiprows=4,parse_dates=["Date"])

# Loads Excel file. **Make sure to copy the file to the right folder: /Users/chrisstadler/PycharmProjects/Process QB detail p&l from csv**
df = pd.read_excel("Resound+Creative+Media,+LLC_Profit+and+Loss+Detail.xlsx", sheet_name= 'Profit and Loss Detail', skiprows=4,parse_dates=["Date"])


# Need to rename column 0 to "Type" (don't do this after
df.rename(columns={'Unnamed: 0':'Type'}, inplace=True )

# Need to fill forward only the first column
cols = ['Type']
df.loc[:,cols] = df.loc[:,cols].ffill()

# df.head(10)

# Need to drop the "Balance" column. Something like the following...
df = df.drop(columns=['Balance'])


#drop rows that contain specific 'value' in 'column_name'. Specifically "Invoice" in "Transaction Type"
#df = df[df.Transaction_Type != "Invoice"]
# df = df[ (df['Transaction Type'] != "Invoice")

# Need to drop all records where the date field is empty.
df.dropna(subset=['Date'], inplace=True)

pd.set_option('display.max_columns', None)


# Saves the new file
df.to_csv("new.csv", index=False, columns=['Type', 'Date', 'Transaction Type', 'Num', 'Name', 'Split', 'Memo/Description', 'Amount'])

print(df.head())

