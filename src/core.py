import time
import ast
from src import *

def main(config, debug):
    args = input_args(config, debug)
    Evaluator(args.config, args.debug)

def input_args(default = "setting/pe1.yaml", debug = False):
    parser = argparse.ArgumentParser()
    parser.add_argument("-config", help = "input setting yaml path", default=default)
    parser.add_argument("-debug", help=" ", default=debug)
    args = parser.parse_args()
    return args

def Evaluator(PATH, debug):
    start_time = time.monotonic()
    logging.basicConfig(level=logging.INFO,
                        format='%(message)s')

    args = begin_step(PATH)
    file = glob.glob(f"{args[0]['sett_']['test_path']}{args[0]['sett_']['find_path']}")
    if len(file) == 0 and not debug:
        logging.error(f"Error: glob() can't find any test file, please check you test_path")
        return None

    pipeline = setup_step(args, PATH)

    input_dim = pipeline[list(pipeline.keys())[-2]],
    info = pipeline[1]
    mode = pipeline[0]['sett_']['mode']
    test_input = pipeline[0]['sett_']['test_input']
    test_PATH = pipeline[0]['sett_']['test_path']

    ut_logging_begin(info, input_dim)

    if mode in ['mp', 'multi']:
        _core = multi_processing
    elif mode in ['sigle', 'sp']:
        _core = sigle_processing

    dfs = []
    for in_v in tqdm(test_input, position=0, leave=True, ascii=True):

        in_v = [i.replace('/*', '*') if type(i) == str else i  for i in in_v]
        pipeline = exmaple_step(pipeline, in_v)
        if debug:
            print(pipeline[list(pipeline.keys())[-2]],pipeline[list(pipeline.keys())[-1]])
        else:
            df, foot_notes = _core(file=file, pipeline=pipeline, in_v=in_v)
            dfs.append(df)

    if debug: return None

    pass_value = output_step(pipeline, dfs,
                    foot_notes, file, test_PATH,
                    info['save_csv_PATH'],
                    info['save_check_PATH'])

    ut_print_end(info, pass_value, start_time)

def multi_processing(file, pipeline, in_v):

    with Pool(12) as pool:
        output = pool.starmap(evaluator_step,tqdm(zip(repeat(pipeline),
                                                      file,
                                                      repeat(in_v)
                                                      ), leave=True, ascii=True,
                                                total=len(file), position=0))

    output_ls = [i[0] for i in output]
    foot_note = [i[1] for i in output]
    df = pd.DataFrame(output_ls)
    exmaple_dir = pipeline[list(pipeline.keys())[-1]]

    exmaple_format = {"輸入":len(exmaple_dir[0]), "輸出": len(exmaple_dir[1])}
    check_format = [f"評分-{_key}{_type} {_idx}" for _key, _len in exmaple_format.items() for _type in type_format[_key] for _idx in range(_len)]
    df.columns = base_format + check_format

    return df, foot_note

def sigle_processing(file, pipeline, in_v):
    output_ls = []
    foot_note = []
    for fi in tqdm(file):
        output_l, output_fn = evaluator_step(pipeline.copy(), fi, in_v)
        output_ls.append(output_l)
        foot_note.append(output_fn)

    df = pd.DataFrame(output_ls)
    exmaple_dir = pipeline[list(pipeline.keys())[-1]]

    exmaple_format = {"輸入":len(exmaple_dir[0]), "輸出": len(exmaple_dir[1])}
    check_format = [f"評分-{_key}{_type} {_idx}" for _key, _len in exmaple_format.items() for _type in type_format[_key] for _idx in range(_len)]

    df.columns = base_format + check_format
    return df, foot_note