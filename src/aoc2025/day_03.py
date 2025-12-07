
def problem_01(input):
    max_joltage_sum = 0
    for bank in input.strip().split('\n'):
        max_left = 0
        max_right = 0
        idx = len(bank) - 2
        while idx > -1:
            if int(bank[idx]) >= max_left:
                max_right = max_left
                max_left = int(bank[idx])
            idx -= 1
        max_right = max(max_right, int(bank[len(bank) - 1]))
        max_joltage_sum += max_left * 10 + max_right
    return max_joltage_sum

def problem_02(input):
    max_joltage_sum = 0
    for bank in input.strip().split('\n'):
        digits = [ int(bank[x]) for x in range(len(bank) - 12, len(bank)) ]
        idx = len(bank) - 13
        while idx > -1:
            if int(bank[idx]) >= digits[0]:
                digits.insert(0, int(bank[idx]))
                idx_2 = 1
                while idx_2 < 12:
                    if digits[idx_2] >= digits[idx_2 + 1]:
                        idx_2 += 1
                    else:
                        digits.pop(idx_2)
                        break
                if len(digits) == 13:
                    digits.pop(12)
            idx -= 1
        digits.reverse()
        max_joltage_sum += sum([ digits[x] * 10 ** x for x in range(0, 12) ])
    return max_joltage_sum
