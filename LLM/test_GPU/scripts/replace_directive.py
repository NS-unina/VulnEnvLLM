import re


def replace_expose(output: str, port_numbers: str) -> str:
    """
    Replace the "EXPOSE" command in the Dockerfile with the right port numbers.
    Args:
        output (str): The original output which is actually a dockerfile.
        port_numbers (str): The right port numbers.
    Returns:
        str: The improved dockerfile.
    """
    expose_pattern = re.compile(r"EXPOSE \d+")
    if port_numbers.strip() != "":
        if expose_pattern.search(output):
            # Replace it with "EXPOSE " + port_numbers
            output = expose_pattern.sub(f"EXPOSE {port_numbers}", output)
        else:
            # If there is no EXPOSE command, add it at the end of the Dockerfile
            output += f"\nEXPOSE {port_numbers}"
    return output

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