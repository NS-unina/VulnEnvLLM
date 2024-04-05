from get_port import get_ports
from get_ubuntu_version import get_ubuntu_version
from replace_directive import remove_useless_directive, replace_from, replace_expose



def improve_result(prompt: str, output: str) -> str:
    """
    Improve the result by adjusting the right Ubuntu versions and the right exposed port number.
    Args:
        prompt (str): The original prompt formatted as "Generate a dockerfile of <package_name> <package_version> ...".
        output (str): The original output which is actually a dockerfile.
    Returns:
        str: The improved dockerfile.
    """
    splitted = prompt.split(" ")
    package_name = splitted[4].lower()
    package_version: str | None = (
        splitted[5] if len(splitted) > 5 and not splitted[5].isalpha else None
    )

    ubuntu_version: str = get_ubuntu_version(package_name, package_version)
    port_numbers: str = get_ports(package_name)

    output = replace_expose(output, port_numbers)
    output = replace_from(output, ubuntu_version)
    output = remove_useless_directive(output)

    return output


if __name__ == "__main__":
    prompt = "Generate a dockerfile of openssh-client 1:8.2p1-4ubuntu0.11"
    output = 'FROM ubuntu:20.04\nCOPY example2.txt /run/var/example.txt\nADD https://example.com/test.txt ./test.txt\nRUN apt-get update && apt-get install -y openssh-client\nADD example.conf ./example.conf\nCMD ["bash"]'
    improved_output = improve_result(prompt, output)
    print(improved_output)
