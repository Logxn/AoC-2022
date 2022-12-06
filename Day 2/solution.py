with open('input.txt', 'r') as f:
    lines = f.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.replace('\n', '')

    total_score = 0

    for current_round in lines:
        enemy_move = current_round.split(' ')[0]
        my_move = current_round.split(' ')[1]

        ''' Solution 1
        match enemy_move:
            case 'A': # Rock
                match my_move:
                    case 'X': # Rock -> DRAW
                        total_score += 1 + 3
                    case 'Y': # Paper -> WIN
                        total_score += 2 + 6
                    case 'Z': # Scissor -> LOSE
                        total_score += 3 + 0
            case 'B': # Paper
                match my_move:
                    case 'X': # Rock -> LOSE
                        total_score += 1 + 0
                    case 'Y': # Paper -> DRAW
                        total_score += 2 + 3
                    case 'Z': # Scissor -> WIN
                        total_score += 3 + 6
            case 'C': # Scissor
                match my_move:
                    case 'X': # Rock -> WIN
                        total_score += 1 + 6
                    case 'Y': # Paper -> LOSE
                        total_score += 2 + 0
                    case 'Z': # Scissor -> DRAW
                        total_score += 3 + 3
    '''

        match enemy_move:
            case 'A':  # Rock
                match my_move:
                    case 'X':  # Lose -> Scissor
                        total_score += 3 + 0
                    case 'Y':  # Draw -> Rock
                        total_score += 1 + 3
                    case 'Z':  # Win -> Paper
                        total_score += 2 + 6
            case 'B':  # Paper
                match my_move:
                    case 'X':  # Rock -> LOSE
                        total_score += 1 + 0
                    case 'Y':  # Paper -> DRAW
                        total_score += 2 + 3
                    case 'Z':  # Scissor -> WIN
                        total_score += 3 + 6
            case 'C':  # Scissor
                match my_move:
                    case 'X':  # Lose -> Paper
                        total_score += 2 + 0
                    case 'Y':  # Draw -> Scissor
                        total_score += 3 + 3
                    case 'Z':  # Win -> Rock
                        total_score += 1 + 6

    print(total_score)
