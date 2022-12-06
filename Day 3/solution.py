with open('input.txt', 'r') as f:
    lines = f.readlines()
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priorities = []
    # Remove line-breaks
    for index, rucksack in enumerate(lines):
        lines[index] = rucksack.replace('\n', '')

    # Logic
    for rucksack in lines:
        # Split rucksack in two compartements
        first_compartement, second_compartement = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        
        # Find common character
        common = list(set(first_compartement) & set(second_compartement))
        # print(f'{first_compartement}:{second_compartement} - Common: {common} <-> {rucksack}')

        priorities.append(alpha.index(common[0])+1)
    print(sum(priorities))

    # Logic Part II
    counter = 0
    rucksacks = []
    priorities = []
    for rucksack in lines:
        rucksacks.append(rucksack)
        counter += 1
        
        if counter == 3:
            matches = {x for x in rucksacks[0] if x in rucksacks[1] and x in rucksacks[2]}
            
            print(f'{matches} -> {rucksacks[0]} - {rucksacks[1]} - {rucksacks[2]}')
            priorities.append(alpha.index(''.join(matches))+1)

            counter = 0
            rucksacks.clear()
    print(sum(priorities))
