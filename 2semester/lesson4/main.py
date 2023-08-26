import gspread
import pandas as pd
from matplotlib import pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet_key = "1Sib2_H2Ag9fZ6zRTgZvj13XesX0K6yhMLfUGlurIIOk"
file = client.open_by_key(sheet_key)

sheet = file.worksheet("Graph2")

dataframe = pd.DataFrame(sheet.get_all_records())
my_labels = sheet.get_values("A2:A6")

labels_list = []
for el in my_labels:
    label = ''.join(el)
    labels_list.append(label)

dataframe.plot.bar(x="Жанр", y="Кількість")
plt.savefig("graph.png")
plt.show()

# sheet1 = data.sheet1

# sheet1.clear()

# sheet1.batch_clear(["G2:H4", "J6:L10"])

# sheet1.update("E8", "This is E8 cell")

# data.add_worksheet(title="Sheet2", rows=100, cols=100)

# new_row = ["Апельсини", 35, "-", 10]
#
# sheet.append_row(new_row)

# data = [
#     ["Кількість", "ASD"],
#     [1, 123],
#     [5, 123],
#     [15, 123],
#     [3, 123],
#     [20, 123],
# ]
#
# sheet1.update("D1:E9", data)

# frame = pd.DataFrame(sheet.get_values())
#
# row1 = sheet.row_values(1)
# col1 = sheet.col_values(1)
#
# print("Row 1:", row1)
# print("Col 1:", col1)

# c4 = sheet.acell("C4").value
# print(f"C4 = {c4}")

# sheet = client.create("Test Del 2")
# sheet.share(
#     email_address="ookno16@gmail.com",
#     perm_type="user",
#     role="reader"
# )
