from multiprocessing import Pool
from pathlib import Path
from tqdm import tqdm
import logging, warnings, time, sys, os, re
import pandas as pd

type_format = {"輸入":["字串"], "輸出": ["字串","數值"]}
base_format = ["學號","檔案名稱","注腳字數","錯誤信息","評分-檔案格式","評分-輸入數量","評分-輸出數量"]

os_dir = {"posix":"Linux or Mac", "nt":"windows"}
mp_dir = dict.fromkeys(['mp', 'multi', 'multiprocessing'], '並行')
sp_dir = dict.fromkeys(['sp', 'single', 'singleprocessing'], '單核')
mode_dir = {**mp_dir, **sp_dir}

mode_dir = {"mp":"並行","sigle":"單核"}

warnings.simplefilter("ignore")

from .ulits import *
from .read_setting_rs import *
from .setup_sp import *
from .evaluator_ev import *
from .output_op import *

from .framework import *
from .core import *


