import pandas as pd
import os

file_path_byty = "C:/byty/pronajem/data/"
os.chdir(file_path_byty)

na_values1 = ["N/A"]
file_name = "2020-07-22.csv"
df_pronajem = pd.read_csv(file_name, na_values=na_values1, encoding="utf-8-sig")

print(df_pronajem.iloc[43])
df_pronajem = df_pronajem[df_pronajem.item_no != "item_no"]
print(df_pronajem.iloc[43, 0])
