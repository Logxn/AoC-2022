import re

stacks = [['W', 'M', 'L', 'F'], ['B', 'Z', 'V', 'M', 'F'], ['H', 'V', 'R', 'S', 'L', 'Q'],
          ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'], ['L', 'S', 'W'], ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
          ['J', 'Q', 'C', 'P', 'N', 'R', 'F'], ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
          ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']]

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.replace('\n', '')

    for line in lines:
        numbers = re.findall(r'\d+', line)

        i = int(numbers[0])
        int_to_move = int(numbers[1])
        int_to_receive = int(numbers[2])

        popped = []
        for j in range(0, i):
            ''' Solution A
            popped = stack_to_move.pop()
            stack_to_receive.append(popped)
            '''

            popped.append(stacks[int_to_move - 1].pop())

        popped.reverse()
        for item in popped:
            stacks[int_to_receive - 1].append(item)

    print(''.join("{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(stacks[0][-1], stacks[1][-1], stacks[2][-1], stacks[3][-1],
                                                       stacks[4][-1], stacks[5][-1], stacks[6][-1], stacks[7][-1],
                                                       stacks[8][-1])))
