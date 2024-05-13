from src import *

def read_from_idx_(from_idx, args, pass_value, step_input):
    if from_idx >= 0:
        return args[from_idx]

    elif from_idx == -1:
        return pass_value

    elif from_idx == -2:
        return step_input

def concat(*kargs, _print=False):
    if _print:
        print(*kargs)
    return kargs

def begin_step(setting_PATH, ground_PATH=r'setting/essential_setup/base_config.yaml'):
    args = sp_setup_args(setting_PATH, ground_PATH)
    return {0: args}

def setup_step(args, setting_PATH, ground_PATH=r'setting/essential_setup/base_config.yaml'):
    step_input = (setting_PATH, ground_PATH)
    offset = 1
    blueprint = args[0]['sett_structure']['setup']
    pass_value = args[tuple(args.keys())[-1]]

    for idx, (from_idx, func) in enumerate(blueprint):

        if type(from_idx) == list:
            pass_value = func(*list(map(lambda x: args[x], from_idx)))

        elif from_idx == -1:
            pass_value = func(pass_value)

        elif from_idx == -2:
            pass_value = func(*step_input)

        else:
            pass_value = func(args[from_idx])

        args[idx + offset] = pass_value
    return args

def exmaple_step(args, INPUT):
    step_input = {'PATH': '', 'INPUT': INPUT}
    offset = 4
    blueprint = args[0]['sett_structure']['exmaple']
    pass_value = args[tuple(args.keys())[-1]]

    for idx, (from_idx, func) in enumerate(blueprint):
        if type(from_idx) == list:
            put_in = [read_from_idx_(i, args, pass_value, step_input) for i in from_idx]

        else:
            put_in = [read_from_idx_(from_idx, args, pass_value, step_input)]

        pass_value = func(*put_in)
        args[idx + offset] = pass_value
    return args

def evaluator_step(args, PATH, INPUT):
    step_input = {'PATH': PATH, 'INPUT': INPUT}
    offset = 9
    blueprint = args[0]['sett_structure']['evaluator']
    pass_value = args[tuple(args.keys())[-1]]

    for idx, (from_idx, func) in enumerate(blueprint):
        if type(from_idx) == list:
            put_in = [read_from_idx_(i, args, pass_value, step_input) for i in from_idx]

        else:
            put_in = [read_from_idx_(from_idx, args, pass_value, step_input)]

        pass_value = func(*put_in)
        args[idx + offset] = pass_value
    return pass_value


def output_step(args, df_list, foot_notes, files, test_PATH, save_PATH, save_check_PATH):
    step_input = {'df_list': df_list,
                  'foot_notes': foot_notes,
                  'files': files,
                  'test_PATH': test_PATH,
                  'save_PATH': save_PATH,
                  'save_check_PATH':save_check_PATH}
    offset = 17
    blueprint = args[0]['sett_structure']['output']
    pass_value = args[tuple(args.keys())[-1]]

    for idx, (from_idx, func) in enumerate(blueprint):
        if type(from_idx) == list:
            put_in = [read_from_idx_(i, args, pass_value, step_input) for i in from_idx]

        else:
            put_in = [read_from_idx_(from_idx, args, pass_value, step_input)]

        pass_value = func(*put_in)
        args[idx + offset] = pass_value

    return pass_value






