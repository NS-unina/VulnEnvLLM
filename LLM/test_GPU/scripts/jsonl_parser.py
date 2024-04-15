import json

def read_jsonl(filename: str) -> list:
    input_list = []
    output_list = []
    with open(filename, 'r') as file:
        for line in file:
            data = json.loads(line)
            input_list.append(data['input'])
            output_list.append(data['output'])
    return [input_list, output_list]

def write_jsonl(columns_lists: list, column_names: list, filename: str) -> None:
    with open(filename, 'w') as file:
        for row in column_list:
            data = dict(zip(column_names, row, strict=True))
            file.write(json.dump(data, file) + '\n')