from multiprocessing import Pool
from tqdm import tqdm
import logging, warnings, time, sys, os, re
import pandas as pd

type_format = {"輸入":["字串"], "輸出": ["字串","數值"]}
base_format = ["學號","檔案名稱","注腳字數","錯誤信息","評分-檔案格式","評分-輸入數量","評分-輸出數量"]

os_dir = {"posix":"Linux or ios", "nt":"windows"}
mode_dir = {"mp":"並行","sigle":"單核"}

warnings.simplefilter("ignore")

from .ulits import *
from .read_setting_rs import *
from .setup_sp import *
from .evaluator_ev import *
from .output_op import *

from .framework import *
from .core import *


