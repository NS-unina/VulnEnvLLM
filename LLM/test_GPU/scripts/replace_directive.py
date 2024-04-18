import re


def remove_useless_directive(input_string: str) -> str:
    lines = input_string.split("\n")
    output_lines = []

    for line in lines:
        if line.startswith("MAINTAINER ") or line.startswith("LABEL "):
            continue  # Skip these lines
        if not (line.startswith("ADD ") or line.startswith("COPY ")):
            output_lines.append(line)
        else:
            # Check if there is a valid URL after ADD or COPY
            url = re.search(r"(https?://[^\s]+)", line)
            if url:
                output_lines.append(line)
            else:
                output_lines.append(f"# {line}")

    return "\n".join(output_lines)

def clean_output(output: str) -> str:
    pattern = re.compile(r'(?i)(?<=```dockerfile)(.*?)(?=```)', re.DOTALL)
    match = pattern.search(output)
    if match:
        return match.group(1).strip()
    else:
        return output