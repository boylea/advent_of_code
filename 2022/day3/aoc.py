# priority key - index is the priority value (-1)
priorities = [chr(x) for x in range(ord('a'), ord('z')+1)] + [chr(x) for x in range(ord('A'), ord('Z')+1)]
print(priorities, len(priorities))

priority_sum = 0

priority_sum2 = 0
group_buffer = []

with open('input.txt') as fh:
    for line in fh:
        rucksack = line.strip()

        # part 1
        split_idx = len(rucksack)//2
        comp1 = set(rucksack[:split_idx])
        comp2 = set(rucksack[split_idx:])
        misplaced_item = comp1.intersection(comp2).pop()
        priority_sum += priorities.index(misplaced_item) + 1
        # print(misplaced_item, priorities.index(misplaced_item))

        # part 2
        group_buffer.append(set(rucksack))
        if len(group_buffer) == 3:
            badge = (set.intersection(*group_buffer)).pop()
            # print(badge)
            priority_sum2 += priorities.index(badge) + 1
            group_buffer = []

print(priority_sum)
print(priority_sum2)
