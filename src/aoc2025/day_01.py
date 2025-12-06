

def problem_01(input):
    zeros : int = 0
    pos : int = 50
    for instruction in input.strip().split('\n'):
        delta : int = int(instruction[1:]) * (-1 if instruction[0] == 'L' else 1)
        pos += delta
        while pos < 0:
            pos += 100
        while pos > 99:
            pos -= 100
        if pos == 0:
            zeros += 1
    return zeros

def problem_02(input):
    zeros : int = 0
    pos : int = 50
    started_at_zero = False
    for instruction in input.strip().split('\n'):
        prev_pos = pos
        delta : int = int(instruction[1:]) * (-1 if instruction[0] == 'L' else 1)
        pos += delta
        while pos < 0:
            pos += 100
            zeros += 1
        while pos > 99:
            pos -= 100
            zeros += 1
        if delta < 0 and pos == 0:
            zeros += 1
        if started_at_zero and delta < 0:
            zeros -= 1
        started_at_zero = pos == 0
    return zeros
