win_pts = 6
draw_pts = 3

rock = 1
paper = 2
sissors = 3

# part 1
def match_pts(opponent, protagonist):
    if opponent == protagonist:
        return draw_pts
    elif opponent == rock and protagonist == paper:
        return win_pts
    elif opponent == paper and protagonist == sissors:
        return  win_pts
    elif opponent == sissors and protagonist == rock:
        return win_pts
    return 0

total_score = 0
key = {'A': rock, 'B': paper, 'C': sissors, 'X': rock, 'Y': paper, 'Z': sissors}
with open('input.txt') as fh:
    for line in fh:
        moves = line.split()
        opp, pro = key[moves[0]], key[moves[1]]
        total_score += match_pts(opp, pro)
        total_score += pro
print(total_score)

# part 2
total_score = 0
key = {'A': rock, 'B': paper, 'C': sissors, 'X': 0, 'Y': draw_pts, 'Z': win_pts}
with open('input.txt') as fh:
    for line in fh:
        moves = line.split()
        opp, outcome = key[moves[0]], key[moves[1]]
        total_score += outcome
        if outcome == draw_pts:
            total_score += opp
        elif outcome == win_pts:
            # need to win
            if opp == rock:
                total_score += paper
            elif opp == paper:
                total_score += sissors
            else:
                total_score += rock
        else:
            # lose
            if opp == rock:
                total_score += sissors
            elif opp == paper:
                total_score += rock
            else:
                total_score += paper
print(total_score)
