
def problem_01(input):
    invalid_id_sum = 0
    for id_range_str in input.strip().split(','):
        id_range = [ int(x) for x in id_range_str.split('-') ]
        for id in range(id_range[0], id_range[1] + 1):
            id_str = str(id)
            if id_str[0:(len(id_str) // 2)] == id_str[(len(id_str) // 2):len(id_str)]:
                invalid_id_sum += id
    return invalid_id_sum

def problem_02(input):
    invalid_id_sum = 0
    for id_range_str in input.strip().split(','):
        id_range = [ int(x) for x in id_range_str.split('-') ]
        for id in range(id_range[0], id_range[1] + 1):
            id_str = str(id)
            midpoint = (len(id_str) // 2)
            for num_chars in range(1, midpoint + 1):
                if len(id_str.replace(id_str[0:num_chars], '')) == 0:
                    invalid_id_sum += id
                    break
    return invalid_id_sum
