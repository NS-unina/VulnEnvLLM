import json
from os import chdir, path

def read_jsonl(filename: str) -> list:
    """
    Read a JSONL file and return a list of input and output values.

    Args:
        filename (str): The path to the JSONL file.

    Returns:
        list: A list containing two lists - input_list and output_list.
              input_list contains the 'input' values from the JSONL file.
              output_list contains the 'output' values from the JSONL file.
    """
    chdir(path.dirname(path.realpath(__file__)))
    filename = path.abspath(filename)
    input_list = []
    output_list = []
    with open(filename, 'r') as file:
        for line in file:
            data = json.loads(line)
            input_list.append(data['input'])
            output_list.append(data['output'])
    return [input_list, output_list]

import json
from os import chdir, path

def write_jsonl(inputs: list, outputs: list, codellama_outputs: list, filename: str) -> None:
    """
    Write data to a JSONL file.

    Args:
        inputs (list): A list of input column values.
        outputs (list): A list of output column values.
        codellama_outputs (list): A list of codellama output column values.
        filename (str): The name of the output file.

    Returns:
        None
    """
    chdir(path.dirname(path.realpath(__file__)))
    filename = path.abspath(filename)
    with open(filename, 'w') as file:
        for i in range(len(inputs)):
            data = {"input" : inputs[i], "output" : outputs[i], "codellama_output" : codellama_outputs[i]}
            file.write(json.dumps(data) + '\n')