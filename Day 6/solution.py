import re

with open('input.txt', 'r') as file:
    line = file.readline()

    possible_markers = re.findall('....', line)

    for possible_marker in possible_markers:
        if len(possible_marker) == len(set(possible_marker)):
            print(f'Possible unique marker: {possible_marker}')
            starting_pos = line.find(possible_marker)
            end_pos = starting_pos + 3  # 3 remaining characters of the 4 char marker + index fixing
            print(f'Possible ending position: {end_pos}')
            break

    for i in range(0, len(line)):
        sub_str = line[i:i+14]
        if len(sub_str) == len(set(sub_str)):
            print(f'Possible msg marker: {sub_str}')
            starting_pos = line.find(sub_str)
            end_pos = starting_pos + 14 
            print(f'Possible msg marker ending: {end_pos}')
            break
