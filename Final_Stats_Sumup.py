import pandas as pd
import os
import sys
import warnings
warnings.filterwarnings("ignore")

SOURCE_DIR = './SampleFinalStatsInput/'
num = 2 #Number of best AP gainers under level 8 in each faction

files = os.listdir(SOURCE_DIR)
Out_table = pd.read_excel(SOURCE_DIR + files[0])
for table in files[1:]:
    Out_table.update(pd.read_excel(SOURCE_DIR + table))

Out_table.Delta_Level    = Out_table.Post_Level - Out_table.Pre_Level
Out_table.Delta_AP       = Out_table.Post_AP - Out_table.Pre_AP
Out_table.Delta_Distance = Out_table.Post_Distance - Out_table.Pre_Distance

Out_table.to_excel('./Sample_Output_by_FSSdotPY.xlsx', index = False)

class txtWriter():
    def __init__(self, stdout, filename):
        self.stdout = stdout
        self.log_file = file(filename, 'a')

    def write(self, text):
        self.stdout.write(text)
        self.log_file.write(text)

    def close(self,):
        # self.stdout.close()
        self.log_file.close()

writer = txtWriter(sys.stdout, './Recoring_Announce.txt')
old_stdout = sys.stdout
sys.stdout = writer

ENL_AllAP = Out_table[Out_table['Faction'] == 'ENL'].Delta_AP.sum()
RES_AllAP = Out_table[Out_table['Faction'] == 'RES'].Delta_AP.sum()
print(' ')
print('ENL AP gain: ' + str(int(ENL_AllAP)))
print('RES AP gain: ' + str(int(RES_AllAP)))
print('City AP gain: ' + str(int(ENL_AllAP + RES_AllAP)))
print(' ')

ENL_AllLevel = Out_table[Out_table['Faction'] == 'ENL'].Delta_Level.sum()
RES_AllLevel = Out_table[Out_table['Faction'] == 'RES'].Delta_Level.sum()
print('ENL level gain: ' + str(int(ENL_AllLevel)))
print('RES level gain: ' + str(int(RES_AllLevel)))
print('City level gain: ' + str(int(ENL_AllLevel + RES_AllLevel)))

print('\n-------------------------------\n')

ENL_MaxAP_id = Out_table[Out_table['Faction'] == 'ENL'].Delta_AP.idxmax()
RES_MaxAP_id = Out_table[Out_table['Faction'] == 'RES'].Delta_AP.idxmax()
print('Best AP gainers are: ')
print(Out_table.ix[[ENL_MaxAP_id, RES_MaxAP_id]][['AgentName', 'Delta_AP', 'Faction']])
print(' ')

print('Best Start-ups:')
ENL_best_startups = Out_table[Out_table['Faction'] == 'ENL'][Out_table['Pre_Level'] < 8][['AgentName', 'Delta_AP', 'Faction']].sort_values('Delta_AP', ascending = False).head(num)
RES_best_startups = Out_table[Out_table['Faction'] == 'RES'][Out_table['Pre_Level'] < 8][['AgentName', 'Delta_AP', 'Faction']].sort_values('Delta_AP', ascending = False).head(num)
print(pd.concat([ENL_best_startups, RES_best_startups]).sort_values('Faction'))
print(' ')

sys.stdout = old_stdout
writer.close()