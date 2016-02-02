import pandas as pd
import os

SOURCE_DIR = './SampleInitialStatsInput/'

tables = []
for table in os.listdir(SOURCE_DIR):
    tables.append(pd.read_excel(SOURCE_DIR + table))

Out_table = pd.concat(tables, ignore_index = True).sort_values('Faction')

Out_table.to_excel('./Sample_Output_by_ISMdotPY.xlsx', index = False)