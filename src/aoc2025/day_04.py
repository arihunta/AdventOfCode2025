from queue import Queue

__offsets = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
]

def problem_01(input):
    map = [ list(row) for row in input.strip().split('\n') ]
    accessible = 0
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == '@':
                neighbours = __get_neighbours(x, y, map)
                if sum([ 1 if map[ny][nx] == '@' else 0 for nx, ny in neighbours ]) < 4:
                    accessible += 1
    return accessible

def problem_02(input):
    map = [ list(row) for row in input.strip().split('\n') ]
    offsets = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]
    removed = 0
    reprocess_queue = Queue()

    # first pass
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == '@':
                neighbours = __get_neighbours(x, y, map)
                if sum([ 1 if map[ny][nx] == '@' else 0 for nx, ny in neighbours ]) < 4:
                    removed += 1
                    map[y][x] = '.'
                    for nx, ny in neighbours:
                        if map[ny][nx] == '@':
                            reprocess_queue.put([nx, ny])

    # now reprocess removed ones
    while not reprocess_queue.empty():
        x, y = reprocess_queue.get()
        if map[y][x] == '@':
            neighbours = __get_neighbours(x, y, map)
            if sum([ 1 if map[ny][nx] == '@' else 0 for nx, ny in neighbours ]) < 4:
                removed += 1
                map[y][x] = '.'
                for nx, ny in neighbours:
                    if map[ny][nx] == '@':
                        reprocess_queue.put([nx, ny])

    return removed

def __get_neighbours(x, y, map):
    return [ [ x + dx, y + dy ] for dx, dy in __offsets if __is_in_range(x + dx, y + dy, map) ]

def __is_in_range(x, y, list):
    y_clamped = min(max(y, 0), len(list) - 1)
    return y_clamped == y and min(max(x, 0), len(list[y]) - 1) == x

