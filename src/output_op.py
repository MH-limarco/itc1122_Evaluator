from src import *
from itertools import compress
import pandas as pd
import shutil

def ot_df_concat(INPUT):
    df_list = INPUT['df_list']
    return pd.concat(df_list)

def ot_df_agg(df, int_col=4, group_col = 2):
    df.iloc[:, int_col:] = df.iloc[:, int_col:].astype(int)
    agg_ls = {col: ('mean' if '字串' in col
                              or '數值' in col
                              or '數量' in col
                    else pd.Series.mode) for col in list(df.columns[group_col:])}

    return df.groupby(list(df.columns[:group_col])).agg(agg_ls)
def ot_save_df(df, INPUT, int_col=4, encoding='utf_8_sig'):
    save_PATH = INPUT['save_PATH']
    ut_check_dir(save_PATH.split('{}'))

    df.to_csv(save_PATH, encoding=encoding)
    condition = df[df.columns[int_col:]].sum(axis=1) < len(df.columns[int_col:])
    return condition

def ot_save_file(condition, INPUT, encoding='utf_8_sig'):
    test_PATH = INPUT['test_PATH']
    save_check_PATH = INPUT['save_check_PATH']
    files = list(compress(INPUT['files'], condition))
    foot_notes = list(compress(INPUT['foot_notes'], condition))

    for file, note in tqdm(zip(files, foot_notes)):
        move_path = file.replace(test_PATH, save_check_PATH)
        ut_check_dir(move_path)
        shutil.copy(file, move_path)

        with open(f"{move_path}.txt", 'w+',encoding=encoding) as txt:
            [txt.write(line) for line in note]

    return sum(condition)

