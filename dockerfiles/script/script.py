import os

def remove_trailing_newlines(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if(file_path.endswith(".DS_Store")):
                continue
            with open(file_path, 'r') as f:
                lines = f.readlines()
            with open(file_path, 'w') as f:
                for i in range(len(lines)):
                    if i != len(lines) - 1:  # If it's not the last line
                        f.write(lines[i])
                    else:  # If it's the last line
                        f.write(lines[i].rstrip('\r\n'))

# Specifica la directory da cui iniziare la ricerca
remove_trailing_newlines("../with-llms")
remove_trailing_newlines("../fixed")
