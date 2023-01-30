
def solution(lines):
    sets = []
    for l in lines: 
        sets.append(set(range(l[0], l[1])))
    return len(sets[0]&sets[1] | sets[1]&sets[2] | sets[2]&sets[0])
