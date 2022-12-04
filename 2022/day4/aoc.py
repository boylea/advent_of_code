
full_overlap_count = 0
any_overlap_count = 0
with open('input.txt') as fh:
    for line in fh:
        elf1, elf2 = line.split(',')
        range1 = [int(x) for x in elf1.split('-')]
        range2 = [int(x) for x in elf2.split('-')]
        if range1[0] == range2[0]:
            full_overlap_count +=1    
        elif range1[0] < range2[0]:
            if range1[-1] >= range2[-1]:
                full_overlap_count +=1
        else:
            if range2[-1] >= range1[-1]:
                full_overlap_count +=1

print(full_overlap_count)

# I have a tendency to not want to do things inefficiently from a computational standpoint,
# but at part 2 decided that maybe the point with this puzzles is more about dev time
# efficency
full_overlap_count = 0 # part1
partial_overlap_count = 0 # part2
with open('input.txt') as fh:
    for line in fh:
        elf1, elf2 = line.split(',')
        range1 = [int(x) for x in elf1.split('-')]
        range2 = [int(x) for x in elf2.split('-')]
        range1[-1] +=1
        range2[-1] +=1
        set1 = set(range(*range1))
        set2 = set(range(*range2))
        if set1.issubset(set2) or set2.issubset(set1):
            full_overlap_count +=1
        elif len(set1.intersection(set2)) > 0:
            partial_overlap_count += 1

print(full_overlap_count, full_overlap_count+partial_overlap_count)