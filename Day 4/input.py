with open('input.txt', 'r') as f:
    lines = f.readlines()

    for index, line in enumerate(lines):
        lines[index] = line.replace('\n', '')

    count = 0
    for line in lines:
        pairs = line.split(',')
        first_range = pairs[0]
        second_range = pairs[1]

        first_min = int(first_range.split('-')[0])
        first_max = int(first_range.split('-')[1])

        second_min = int(second_range.split('-')[0])
        second_max = int(second_range.split('-')[1])

        ## Succeedings
        if first_min == first_max and (first_min <= second_max and first_max >= second_min):
            count += 1
            continue

        if second_min == second_max and (second_min <= first_max and second_max > first_min):
            count += 1
            continue

        if second_min >= first_min and second_max <= first_max:
            count += 1
            continue

        if first_min >= second_min and first_max <= second_max:
            count += 1
            continue
        
    print(count)

    count = 0
    for line in lines:
        pairs = line.split(',')
        first_range = pairs[0]
        second_range = pairs[1]

        first_min = int(first_range.split('-')[0])
        first_max = int(first_range.split('-')[1])

        second_min = int(second_range.split('-')[0])
        second_max = int(second_range.split('-')[1])

        ## Succeedings
        if first_min == first_max and (first_min <= second_max and first_max >= second_min):
            count += 1
            continue

        if second_min == second_max and (second_min <= first_max and second_max > first_min):
            count += 1
            continue

        if second_min >= first_min and second_max <= first_max:
            count += 1
            continue

        if first_min >= second_min and first_max <= second_max:
            count += 1
            continue

        ## Part Two

        if second_min <= first_max and second_max > first_max:
            count += 1
            continue

        if first_min <= second_max and first_max > second_max:
            count += 1
            continue
    print(count)
        
