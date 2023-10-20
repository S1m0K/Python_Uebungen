import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_excel('data/Zeitreihe_Winter_2022092012.xlsx', skiprows=2)
df = df.drop(index=0)  # delete empty row

base = list(df.columns[:3])
years = df.columns[3:].astype(str)
base.extend('x' + years)
df.columns = base
# pd.set_option('display.expand_frame_repr', False)
# print(df.describe())
# print(df.head())

# print(df.tail())
# print(df)
# 2.1
# tourism_ibk = df.values[0, 3:]
# plt.title("Tourism Innsbruck")
# plt.xlabel("Year")
# plt.ylabel("Tourists")
# plt.plot(np.arange(2000, 2000 + len(df.columns) - 3), tourism_ibk, "o")
# plt.show()
# print(tourism_ibk)

# 2.2
# tourism_my_district = df.loc[df['Bez'] == 'LZ']
# tourism_my_district = tourism_my_district.sum(axis=0)
# plt.title("Tourism Lienz")
# plt.xlabel("Year")
# plt.ylabel("Tourists")
# plt.plot(np.arange(2000, 2000 + len(df.columns) - 3), tourism_my_district[3:], "o")
# plt.show()
# print(tourism_my_district[3:])

# 3.1
# dfv = df.values[:, 3:]
# df['Durchschnitt'] = dfv.mean(axis=1)
# df['Maximum'] = dfv.max(axis=1)
# df['Minimum'] = dfv.min(axis=1)
# df['Spannweite'] = np.ptp(dfv, axis=1)
# print(df)

# 3.1.1
# df['Spannweite'] = np.ptp(dfv, axis=1) / dfv.mean(axis=1)
# print(df)

# 3.2
dfv2 = df.values[:, 3:]
# total_tourists = dfv2.sum(axis=0)
# print(total_tourists)  # sum tourists per year
# sum_total_tourists = total_tourists.sum(axis=0)
# print(sum_total_tourists)  # sum all tourists since 2000

print(dfv2)

# sum_bez = 0
# sum_bez.plot.bar()
# plt.show();