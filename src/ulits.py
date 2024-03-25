import subprocess, inspect
import time
from itertools import chain

from src import *

def ut_check_dir(PATH):
    if not os.path.isdir(PATH):
        os.makedirs(PATH)

def ut_flatten(x):
    return list(chain(*(i if isinstance(i, list) else (i,) for i in x)))

def ut_str_tr(x):
    if type(x) is not str:
        return str(x)
    return x

def ut_cmd_run(command, _input, setting, check = False):
    if len(_input) > 0:
        return subprocess.run(command,
                              check = check,close_fds=True,
                              input='\n'.join(map(ut_str_tr, _input)),
                              **setting)
    else:
        return subprocess.run(command,close_fds=True,
                              check=check,
                              **setting)

def ut_get_error_type(stderr):
    return re.findall(f"\\s(.*Error):", stderr)

def ut_format_check(PATH, file_format):
    if file_format is None:
        return None
    return len(re.findall(f"({file_format})", PATH)) == 1

def ut_get_default_args(func):
    signature = inspect.signature(func)
    return {k: v.default for k, v in signature.parameters.items()
                         if v.default is not inspect.Parameter.empty}


def ut_logging_begin(info):

    logging.info(f"\nos: {os_dir[info['os']]}\n"
                 f"mode: {mode_dir[info['mode']]}\n"
                 f"核心最大調用: {info['cpu_num']}\n"
                 f"檔案數量: {info['file_len']}\n"
                 f"設定檔: {info['setting_PATH']}\n"
                 f"架構檔: {info['structure_PATH']}\n"
                 f"=============開始運作=============")



def ut_print_end(info, pass_value, start_time):

    logging.info(f"\n=============運作結束=============\n"
                 f"運作時間: {round((time.monotonic() - start_time),3)}s\n"
                 f"csv檔位置: {info['save_csv_PATH']}\n"
                 f"異常檔案位置: {info['save_check_PATH']}\n"
                 f"異常檔案數量: {pass_value}\n"
                 )







