import os
import sys
import pandas as pd
 
_CURR_PATH = os.path.dirname(os.path.abspath(__file__))
_INFO_PATH = os.path.join(_CURR_PATH, "MemberInfo/InfoFile")
print(_INFO_PATH)


def get_all_file_path(root_path):
    file_paths = []
    for file in os.listdir(root_path):
        file = os.path.join(root_path, file)
        if os.path.isfile(file):
            file_paths.append(file)
    return file_paths


for file in get_all_file_path(_INFO_PATH):
    re = pd.read_excel(file)
    print(re[re['工号'] == 44619].head())
    print(re[re['职级'].map(lambda x: x.endswith('A'))].head())
    print(re[(re['工号'] == 44619) & re['职级'].map(lambda x: x.endswith('A'))]['姓名'].values)
    df = pd.DataFrame(re)
    #print(df)
    
