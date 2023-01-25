def solution(numbers):
    
    num_list = {
        "one": 1, "two": 2, "three": 3,
        "four": 4, "five": 5, "six": 6,
        "seven" : 7, "eight": 8, "nine" : 9,    
        "zero": 0, 
    }
    while numbers.isalpha():
        for key, val in num_list.items():
            numbers = numbers.replace(key, str(num_list[key]))
    
    return int(numbers)
    