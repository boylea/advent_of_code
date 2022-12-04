highest = 0
highests = [0,0,0]
current_elf = 0
elf_count = 0

# Avoiding loading whole input into memory to analyze, 
# although the input here is not actually large enough
# for that to be an issue
with open('input.txt') as fh:
    for line in fh:
        calories = line.strip()
        if calories:
            current_elf += int(calories)
        else:
            highest = max(highest, current_elf) # part 1
            if current_elf > highests[0]: # part 2
                highests[0] = current_elf
                highests.sort()
            current_elf = 0
            elf_count += 1

print('single highest', highest)
print('top three', highests, sum(highests))
print('elf count', elf_count)