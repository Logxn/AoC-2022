"""
Check if line is input or output

if input -> check if cd or ls
            cd -> keep track of current directory
            ls -> get the all output until next input line
if output -> ignore
"""

puzzle_input = []
current_directory = []
seen_files = []
directoy_sizes = {}




def remove_new_lines(uncleaned_challenge_input) -> []:
    cleaned_challenge_input = []
    for line in uncleaned_challenge_input:
        clean_line = line.replace('\n', '')
        cleaned_challenge_input.append(clean_line)
    return cleaned_challenge_input


def handle_cd_command(cd_command):
    directory_to_change = cd_command[2]

    if directory_to_change == '/':
        current_directory.append('/home')
    elif directory_to_change == '..':
        del current_directory[-1]
    else:
        current_directory.append(f'/{directory_to_change}')


def get_output(index) -> []:
    outputs = []
    for i in range(index + 1, len(puzzle_input)):
        possible_outpout = puzzle_input[i]

        if possible_outpout.split()[0] == '$':
            break

        outputs.append(possible_outpout)

    return outputs


def handle_list_command(index):
    full_directory = ''.join(current_directory)
    outputs = get_output(index)

    for output in outputs:
        file_type = output.split()[0]
        file_name = output.split()[1]
        full_path = f'{full_directory}/{file_name}'

        # We dont care about directories.
        # We will probably move into them later anways
        if not file_type.isnumeric():
            continue

        # We handled this file before
        # Probably we used ls in a folder where we have been before
        if full_path in seen_files:
            print('[duplicate]')
            continue

        seen_files.append(full_path)

        if full_directory not in directoy_sizes:
            directoy_sizes[full_directory] = file_type
        else:
            directoy_sizes[full_directory] += file_type

    # print(f'CMD - LS: {full_directory} -> {outputs}')


def handle_linux_commands(index, linux_command):
    # CD command consists of 3 parts:
    # $ -> Linux Prefix
    # cd -> Change directory
    # xxx -> Name of directory

    if len(linux_command) < 3:
        handle_list_command(index)
    else:
        handle_cd_command(linux_command)


def main():
    global puzzle_input
    solution = 0

    with open('input.txt', 'r') as file:
        puzzle_input = remove_new_lines(file.readlines())

        for i in range(0, len(puzzle_input)):
            current_line = puzzle_input[i].split()

            # We received input
            if current_line[0] == '$':
                handle_linux_commands(i, current_line)

        for key, value in directoy_sizes.items():
            file_size = int(value)
            if file_size <= 100000:
                solution += file_size
                print(f'{key} -> {value}')

        print(solution)


main()
