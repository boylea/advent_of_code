
with open('input.txt') as fh:
    subroutine = fh.read()
print(subroutine)

n = 14
for i in range(n, len(subroutine)):
    window = set(subroutine[i-n:i])
    if len(window) == n:
        print(i, window)
        break
    