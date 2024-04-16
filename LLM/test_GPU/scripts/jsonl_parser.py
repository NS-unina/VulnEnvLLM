import json
from os import chdir, path

def read_jsonl(filename: str) -> list:
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

def write_jsonl(inputs: list, outputs: list, codellama_outputs: list, filename: str) -> None:
    chdir(path.dirname(path.realpath(__file__)))
    filename = path.abspath(filename)
    with open(filename, 'w') as file:
        for i in range(len(inputs)):
            data = {"input" : inputs[i], "output" : outputs[i], "codellama_output" : codellama_outputs[i]}
            file.write(json.dumps(data) + '\n')