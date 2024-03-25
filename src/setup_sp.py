from src import *

import subprocess, random, glob, time, sys, os

import numpy as np
##uilts

def sp_setup_args(setting_PATH, ground_PATH):
    #
    sett_ground = rs_read_ground_setting_(ground_PATH)
    #
    sett_ = rs_read_setting_(setting_PATH)
    #
    sett_strucure = rs_read_structure_(sett_['cfg'])

    return {"sett_ground": sett_ground,
            "sett_": sett_,
            "sett_structure": sett_strucure,
            "setting_PATH": setting_PATH,
            "structure_PATH": sett_['cfg']
            }

def sp_info(args):
    info = {}
    sett_ = args['sett_']
    info['setting_PATH'] = args['setting_PATH']
    info['structure_PATH'] = args['structure_PATH']
    info['save_csv_PATH'] = sett_['save_csv_path']
    info['save_check_PATH'] = sett_['save_check_path']
    info['os'] = os.name
    info['mode'] = sett_['mode']
    info['cpu_num'] = os.cpu_count() // 2 if sett_['cpu_num'] == None or sett_['cpu_num'] < 1 else sett_['cpu_num']
    info['file_len'] = len(glob.glob(f"{sett_['test_path']}{sett_['find_path']}"))
    return info

def sp_find_input_dim(args):
    cmd_setting = args['sett_ground'].cmd_setting
    input_v = random.choice(args['sett_']['test_input'])
    PATH =f"{args['sett_']['exmaple_path']}"
    for i in range(len(input_v)+1)[::-1]:
        try:
            start = time.monotonic()
            ut_cmd_run([f'{sys.executable}', f'{PATH}'], input_v[:i], cmd_setting, check=True)
            cmd_setting = {**cmd_setting, **{'timeout':(time.monotonic() - start)*1.5}}

        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            if i >= len(input_v):
                return False
            return i + 1

def sp_keyword_(str_dir):
    str_arr_ = np.array(str_dir, dtype=object)
    if len(str_arr_) == 1 and type(str_arr_[0]) == np.ndarray:
        return [str_arr_.tolist()[0], str_arr_.tolist()]

    str_conf = np.array([type(i) in [list, np.ndarray] for i in str_arr_])
    str_arr = np.hstack([str_arr_[~str_conf], *str_arr_[str_conf]]).tolist()
    str_group = str_arr_[str_conf].tolist()
    return [str_arr[::-1], str_group]


def sp_setup_keyword(args):
    in_dir = args['sett_structure'].get('input_key')
    out_dir = args['sett_structure'].get('output_key')
    return {'in_dir': sp_keyword_(in_dir),'out_dir': sp_keyword_(out_dir)}