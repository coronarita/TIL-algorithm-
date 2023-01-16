def solution(sides):
    sides = sorted(sides)
    return (sides[1]+sides[0]) - (sides[1]-sides[0]) - 1