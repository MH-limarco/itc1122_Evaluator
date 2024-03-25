from src import *
#import src

import importlib
import argparse, copy, sys
from functools import partial

import yaml

#utils
def rs_read_yaml_(PATH, args=False):
    yml = yaml.safe_load(open(PATH, encoding='utf-8'))
    if args:
        parser = argparse.ArgumentParser()
        for key, value in yml.items():
            parser.add_argument(f'--{key}',default=value, type=str)
        return parser.parse_args(args = [])  ##Namespace()
    return yml  ##dict()

def rs_read_blueprint_(in_idx, func, args):
    module = importlib.import_module('src')
    func = getattr(module, func)
    defaults = ut_get_default_args(func)

    for key, value in zip(defaults.keys(), args):
        if value == '-d':
            pass
        else:
            defaults[key] = value

    return [in_idx, partial(func, **defaults)]

def rs_read_ground_setting_(ground_PATH):
    return rs_read_yaml_(ground_PATH, args=True)

def rs_read_setting_(setting_PATH):
    return rs_read_yaml_(setting_PATH, args=False)

def rs_read_structure_(structure_PATH):
    structure_ = rs_read_yaml_(structure_PATH, args=False)
    structure_['setup'] = [rs_read_blueprint_(in_idx, func, args) for in_idx, func, args in structure_['setup']]
    structure_['exmaple'] = [rs_read_blueprint_(in_idx, func, args) for in_idx, func, args in structure_['exmaple']]
    structure_['evaluator'] = [rs_read_blueprint_(in_idx, func, args) for in_idx, func, args in structure_['evaluator']]
    structure_['output'] = [rs_read_blueprint_(in_idx, func, args) for in_idx, func, args in structure_['output']]
    return structure_
