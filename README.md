# pe-Evaluator: Automatic code grading script based on modular framework

[中文]() |

pe-Evaluator is an automated code grading framework based on the Python language, featuring an open modular framework. Among various automation frameworks, it uniquely incorporates an open modular approach to further enhance maintainability and flexibility. The design goal of pe-Evaluator is to be flexible, easy to use, and maintainable.

This is presented as my first practical exercise, and feedback or issues are welcome on GitHub.

<p ="center">
  <img src="assets/modular.png" alt="erf" width="100%">
</p>

* [**Documentation**](#Documentation)
* [**Introduction to structure**](#introduction-to-structure)
* [**Customize your process**](#customize-your-process)
* [**main results**](#main-results)
* [**getting started**](#getting-started)


## <div align="center">Documentation</div>

See below for a quickstart and usage example

<details open>
<summary>Preliminaries</summary>

### Environment
This project is based on a [**Python>=3.10**](https://www.python.org/) environment with Windows 11 & Ubuntu 20.04.

### Package install
```bash
pip install numpy
pip install pandas
```

For alternative installation methods including [Conda](https://anaconda.org/conda-forge/pandas), and Git.

</details>

<details open>
<summary>Usage</summary>

### CLI

pe-Evaluator may be used directly in the Command Line Interface (CLI) with a python command:

```bash
python main.py -c pe1.py
```

`-config` Description of the location of the file

### Python

pe-Evaluator can also be used in a Python environment from within pe_Evaluator and accepts the same arguments as in the CLI example above:

```python
from src.core import main

if __name__ == '__main__':
    config = "setting/pe1.yaml" ##Description of the location of the file
    main(config)    ##run script
```
python
</details>

## <div align="center">Introduction to structure</div>

|                |                                                                      ⭐instruction⭐                                                                        |
|:--------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:|
|   Setup-step   |                                           Read YAML, construct the framework used and initialize variables                                            |
|  Exmaple-step  |                    Execute the template script. Extract information and construct a dictionary with the template script responses.                    |
| Evaluator-step | Execute all content requiring grading within the file, and compare the extracted content against the template. Finally, produce the grading results.  |
|  Output-step   |                                             Summarize all experimental results and organize the findings.                                             |


## <div align="center">Architecture example</div>
<p = "center">
  <img src="assets/Architecture_diagram.png" alt="erf" width="100%">
</p>

#### Here is the architecture example for `cfg/structure_pe1` and `cfg/structure_pe1`.
You can build your own structure.yaml according to your requirements

## Customize your process ##

<details open>
<summary>setting.yaml</summary>

### Create a setting yaml.

You need to customize your configuration file so that the script knows where your architecture files are, where to input and output, and the settings for execution.

|                 |              example               | definition                                                                               |
|:---------------:|:----------------------------------:|:-----------------------------------------------------------------------------------------|
|       cfg       |       cfg/structure_pe1.yaml       | Architecture file PATH                                                                   |
|     timeout     |                 3                  | time-out time                                                                            |
|      mode       |                 mp                 | {mp:parallel, sigle:single-core} -(default single-core)                                  |
|     cpu_num     |                 -1                 | Number of cores called when setting parallel mode - (half the default number of threads) |
|    test_path    | data/1122_H210301-PE1上傳區-20240314  | Requires scoring file PATH                                                               |
|  exmaple_path   |       exmaple/exmaple_pe1.py       | exmaple PATH                                                                             |
| save_check_path |           check_file/pe1           | abnormal file directory                                                                  | 
|  save_csv_path  |       output/exmaple_pe1.csv       | Rating .csv PATH                                                                         |
|    nan_value    |               -99999               | Missing values                                                                           |
|    least_col    |                 -1                 | Minimum number of columns                                                                |
|   file_format   |                .py                 | Required file format                                                                     |
|   test_input    | [[4.3], [5], [6.2], [7.2], [3.5]]  | Input data available for evaluate                                                        |
|    find_path    |                 -                  | glob - Search formula                                                                    |
|    re_format    |                 -                  | re format for value extraction                                                           |
</details>

### Create a structure yaml.
<details open>
<summary>structure.yaml</summary>

</details>








