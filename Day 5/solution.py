import re

stack_one = ['W', 'M', 'L', 'F']
stack_two = ['B', 'Z', 'V', 'M', 'F']
stack_three = ['H', 'V', 'R', 'S', 'L', 'Q']
stack_four = ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J']
stack_five = ['L', 'S', 'W']
stack_six = ['F', 'V', 'P', 'M', 'R', 'J', 'W']
stack_seven = ['J', 'Q', 'C', 'P', 'N', 'R', 'F']
stack_eight = ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B']
stack_nine = ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.replace('\n', '')

    for line in lines:
        numbers = re.findall(r'\d+', line)

        i = int(numbers[0])
        int_to_move = int(numbers[1])
        int_to_receive = int(numbers[2])

        match int_to_move:
            case 1:
                stack_to_move = stack_one
            case 2:
                stack_to_move = stack_two
            case 3:
                stack_to_move = stack_three
            case 4:
                stack_to_move = stack_four
            case 5:
                stack_to_move = stack_five
            case 6:
                stack_to_move = stack_six
            case 7:
                stack_to_move = stack_seven
            case 8:
                stack_to_move = stack_eight
            case 9:
                stack_to_move = stack_nine

        match int_to_receive:
            case 1:
                stack_to_receive = stack_one
            case 2:
                stack_to_receive = stack_two
            case 3:
                stack_to_receive = stack_three
            case 4:
                stack_to_receive = stack_four
            case 5:
                stack_to_receive = stack_five
            case 6:
                stack_to_receive = stack_six
            case 7:
                stack_to_receive = stack_seven
            case 8:
                stack_to_receive = stack_eight
            case 9:
                stack_to_receive = stack_nine
    
        popped = []
        for j in range(0, i):
            ''' Solution A
            popped = stack_to_move.pop()
            stack_to_receive.append(popped)
            '''

            popped.append(stack_to_move.pop())

        popped.reverse()
        for item in popped:
            stack_to_receive.append(item)

    print(''.join("{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(stack_one[-1], stack_two[-1], stack_three[-1], stack_four[-1],
                                                       stack_five[-1], stack_six[-1], stack_seven[-1], stack_eight[-1],
                                                       stack_nine[-1])))
