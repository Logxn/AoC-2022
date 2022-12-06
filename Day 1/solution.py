with open('input.txt', 'r') as f:
    lines = f.readlines()
    elf_backpacks = []

    c = 0
    for value in lines:
        if value == '\n':
            elf_backpacks.append(c)
            c = 0
            continue;
        c += int(value.replace('\n', ''))

    elf_backpacks.sort(reverse=True)
    print(elf_backpacks[0])

    ## Part 2
    print(elf_backpacks[0] + elf_backpacks[1] + elf_backpacks[2])
