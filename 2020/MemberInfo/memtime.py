import os
import sys
import pandas as pd

_CURR_PATH = os.path.dirname(os.path.abspath(__file__))
_EXCEL_PATH1 = os.path.join(_CURR_PATH, r"InfoFile/DK")
_EXCEL_PATH2 = os.path.join(_CURR_PATH, r"InfoFile/DL")
print(_EXCEL_PATH1)
print(_EXCEL_PATH2)
_OUTPUT_NAME = r"汇总.xlsx"

def get_all_file_path(root_path):
    file_paths = []
    for file in os.listdir(root_path):
        file = os.path.join(root_path, file)
        if os.path.isfile(file) and not file.endswith('汇总.xlsx'):
            file_paths.append(file)
    return file_paths


def excel_merge(excel_path):
    dfs = []
    for file in get_all_file_path(excel_path):
        print(f'file={file}')
        rdexcel = pd.read_excel(file)
        dfs.append(rdexcel)
    df = pd.concat(dfs)
    result = os.path.join(excel_path, r"汇总.xlsx")
    #if os.path.exists(result):
    #    os.remove(result)
    #df.to_excel(result, index=False)
    return result

def excel_change_timestyle(path2):
    data = pd.read_excel(path2)
    data['日期'] = data['日期'].apply(lambda x:x.strftime('%Y-%m-%d'))
    #pd.to_datetime(data['日期'], format='%Y-%m-%d')

    data['上班时间'] = data['日期'] + data['上班时间']
    data['下班时间'] = data['日期'] + data['下班时间']
    data.to_excel(path2, index=False)


def excel_compare(path1, path2):
    rdexcel1 = pd.read_excel(path1)
    rdexcel2 = pd.read_excel(path2)
    for i in rdexcel2.values:
        print(i)


if __name__ == "__main__":
    r1 = excel_merge(_EXCEL_PATH1)
    r2 = excel_merge(_EXCEL_PATH2)
    #excel_compare(r1, r2)
    excel_change_timestyle(r2)
