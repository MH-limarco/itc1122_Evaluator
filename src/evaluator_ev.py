from src import *
from difflib import get_close_matches
from itertools import repeat
import codecs, json

def ev_command_run(input_, args, exmaple=False):
    path, _input = input_["PATH"], input_['INPUT']
    if exmaple: #and len(path) == 0
        path = args['sett_']['exmaple_path']

    cmd_setting = args['sett_ground'].cmd_setting
    timeout = args['sett_'].get('timeout')
    if timeout is not None:
        cmd_setting['timeout'] = timeout

    try:
        std = ut_cmd_run([f'{sys.executable}', f'{path}'], _input, cmd_setting)
        return std
    except subprocess.TimeoutExpired:
        return "Timeout"

def ev_read_footnote(input_):
    r = re.compile(r'[\',"]{3}([\s\S]*?[\',"]{3})|.*(#.*)')
    py_txt = codecs.open(input_['PATH'], 'r', encoding='utf-8', errors='ignore')
    notes = re.findall(r, py_txt.read())

    notes = [note[0][-3:] + note[0] if note[0] != '' else note[1] for note in notes]
    notes = '\n'.join(notes)

    return notes, len(notes.replace('#', '').replace('\n', ' ').replace('\'', '').replace('"', '').split())

def ev_info_extract(std, args, in_dim, cut_off=-1):
    if std == 'Timeout':
        return [], []
    stdout = std.stdout
    re_format = re.compile(args['sett_']['re_format'])
    col_num, nan_value = args['sett_']['least_col'], args['sett_']['nan_value']

    stdout = stdout.split('\n')
    if len(stdout[-1]) == 0:
        stdout = stdout[:-1]

    stdout = '\n'.join(stdout)
    if len(stdout) > 0:
        stdin = stdout.split(':')[:in_dim]
        stdout = stdout.replace(':'.join(stdin), '').split('\n')

        stdin = dict(zip(stdin, repeat(0)))
        stdout[0] = stdout[0].replace(':'.join(stdin), '')

        value_extract = lambda x: re.findall(re_format, x)
        values = [i[0] if len(i) > 0 else str(nan_value) for i in map(value_extract, stdout)]
        values = [i[0] if type(i) is not str else i for i in values]
        strings = [line.replace(value if type(value)==str else str(value), '').replace(':', '') for line, value in zip(stdout, values)]

        gen_len_val = max(max(len(strings), col_num) - len(values), 0)
        gen_len_str = max(max(len(values), col_num) - len(strings), 0)

        _zip = zip(strings+ [f'ex_{str(_gen)}' for _gen in range(gen_len_str)],
                                                            values + [nan_value] * gen_len_val)

        return stdin, {(s.replace('\n','') if len(s.replace(' ','')) > 0
                                            else str(idx)): v for idx, (s, v) in enumerate(_zip)}
    return [], []

##
def ev_rename_key_(target_dir, str_setting):
    str_arr, str_group = str_setting
    for key in tuple(target_dir):
        for _str in str_arr:
            check = get_close_matches(_str, key.lower().split(' '), 1, cutoff=0.6)
            if len(check) > 0:
                match = _str
                for _group in str_group:
                    if match in _group:
                        match = _group[0]
                target_dir[match] = target_dir.pop(key)
                break
            else:
                continue
    return target_dir

def ev_keyword_extract(std_dir, keyword):
    stdin_dir, stdout_dir = std_dir
    stdin_dir = ev_rename_key_(stdin_dir, keyword['in_dir'])
    stdout_dir = ev_rename_key_(stdout_dir, keyword['out_dir'])
    return [stdin_dir, stdout_dir]

##
def ev_error_check(std, args):
    if std == 'Timeout':
        return [std], False
    error = ut_get_error_type(std.stderr)
    format = ut_format_check(std.args[1], args['sett_'].get('file_format'))
    return error, format


def ev_dir_check_(exmaple_dir_, test_dir_):
    if len(test_dir_) > 0:

        exmaple_dir = exmaple_dir_.copy()
        test_dir = test_dir_.copy()

        check_strings, check_values = {}, {}
        exmaple_key = {v: idx for idx, v in enumerate(list(exmaple_dir.keys()))}.copy()
        test_key = test_dir.keys()
        same_key = [i for i in test_key if i in exmaple_dir.keys()]

        for _key in same_key:
            check_strings[_key] = True
            try:
                check_values[_key] = abs(float(exmaple_dir[_key]) - float(test_dir[_key]))
            except:
                _exmaple_array = np.array([float(i) if type(i) == str else i for i in json.loads(exmaple_dir[_key])])
                try:
                    _test = json.loads(test_dir[_key].replace("'",''))
                    _test = [float(i) if type(i) == str else i for i in _test]
                    _test_array = np.array(_test)
                    check_values[_key] = np.mean(np.abs(_exmaple_array - _test_array))

                except:
                    check_values[_key] = 12546

            exmaple_dir.pop(_key)
            test_dir.pop(_key)

        for ex_key, _key in zip(tuple(exmaple_dir.keys()), tuple(test_dir.keys())):
            check_strings[ex_key] = False
            try:
                check_values[ex_key] = abs(float(exmaple_dir[ex_key]) - float(test_dir[_key]))
            except:
                try:
                    _exmaple_array = np.array(json.loads(exmaple_dir[ex_key]))
                    _test = json.loads(test_dir[_key])
                    _test_array = np.array(_test)
                    check_values[_key] = np.sum(np.abs(_exmaple_array - _test_array))
                except:
                    _exmaple_array = np.array(json.loads(exmaple_dir[ex_key]))
                    _test = json.loads(test_dir[_key])
                    check_values[_key] = 9999

            exmaple_dir.pop(ex_key)
            test_dir.pop(_key)

        for _key in exmaple_dir.keys():
            check_strings[_key] = False
            check_values[_key] = 99999

        check_strings = {_key: check_strings[_key] for _key in exmaple_key}


        check_strings = {_key: check_strings[_key] for _key in exmaple_key}

        return [len(test_dir) <= 0|len(exmaple_dir) <= 0], check_strings , check_values
    return False, [False]*len(exmaple_dir_), [False]*len(exmaple_dir_)
##
def ev_main_check(dirs_, args):
    in_check = list(ev_dir_check_(dirs_[0][0], dirs_[1][0])[:-1])
    out_check = list(ev_dir_check_(dirs_[0][1], dirs_[1][1]))

    if type(out_check[2]) == dict:
        offset_thr = dict(zip(out_check[2].keys(), args['sett_']['output_offset_thr']))
        out_check[2] = {key_:out_check[2][key_] <= offset_thr[key_] if key_ in offset_thr.keys() else True
                                                                            for key_ in out_check[-1].keys()}

        keys_ = list(out_check[1].keys())
        out_check[1] = list(map(lambda x: out_check[1][x], keys_))
        try:
            out_check[2] = list(map(lambda x: out_check[2][x], keys_))
        except:
            out_check[2] = [False] * len(keys_)

    if type(in_check[1]) == dict:
        in_check[1] = list(in_check[1].values())

    dirs_ = list(dirs_)
    dirs_[-1] = list(dirs_[-1])

    dirs_[-1][0] = '' if len(dirs_[-1][0]) < 1 else dirs_[-1][0]
    return list(dirs_[-1]) + in_check + out_check

def ev_output_formatting(input_, dirs_output, args, foot_note_out):
    format_ls = args['sett_ground'].format_ls
    dirs_output = [dirs_output[i] for i in format_ls]

    PATH = [input_['PATH'].split(f'{os.sep}')[-2].split('_')[0],
            input_['PATH'].split(f'{os.sep}')[-1]]

    out_ = ut_flatten([*PATH,foot_note_out[1],*dirs_output])

    return out_, [foot_note_out[0]]







