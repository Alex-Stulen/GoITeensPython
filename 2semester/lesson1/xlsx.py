import pandas as pd
import matplotlib.pyplot as plt

# headers = ["Products", "Price"]
# products1 = [
#     ["Water", 15],
#     ["Milk", 50],
#     ["Apples", 45],
#     ["Nuts", 200],
# ]
#
# sheet1 = pd.DataFrame(data=products1, columns=headers)
#
# products2 = [
#     ["Water", 17],
#     ["Milk", 52],
#     ["Apples", 47],
#     ["Nuts", ""],
# ]
#
# sheet2 = pd.DataFrame(data=products2, columns=headers)
#
#
# with pd.ExcelWriter("products.xlsx") as writer:
#     sheet1.to_excel(writer, sheet_name="2021")
#     sheet2.to_excel(writer, sheet_name="2022")


# data = pd.read_excel("temps.xlsx", index_col=0)
# data.plot(
#     title="Температура",
#     xlabel="Дні",
#     ylabel="Температура, C",
# )
#
# plt.show()

# def add(num1, num2):
#     return num1 + num2
