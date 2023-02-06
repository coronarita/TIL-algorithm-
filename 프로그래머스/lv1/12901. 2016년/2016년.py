def solution(a, b):
    answer = ''
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU',]
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    gap = sum(month[:a]) + b-1 
    
    return day[gap%7]