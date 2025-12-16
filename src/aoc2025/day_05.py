from queue import Queue


def problem_01(input):
    sections = input.strip().split('\n\n')
    ranges = [ FreshRange(int(line.split('-')[0]), int(line.split('-')[1])) for line in sections[0].strip().split('\n') ]
    ingredients = [ int(line) for line in sections[1].strip().split('\n') ]
    matches = 0
    for ingredient in ingredients:
        for range in ranges:
            if range.contains(ingredient):
                matches += 1
                break
    return matches

def problem_02(input):
    sections = input.strip().split('\n\n')
    ranges = [ FreshRange(int(line.split('-')[0]), int(line.split('-')[1])) for line in sections[0].strip().split('\n') ]
    ranges.sort()
    consolidated_ranges = []
    last_range = None
    for idx in range(0, len(ranges)):
        if last_range is None:
            last_range = ranges[idx]
        else:
            if last_range.overlaps(ranges[idx]):
                last_range = last_range.merge(ranges[idx])
            else:
                consolidated_ranges.append(last_range)
                last_range = ranges[idx]
    consolidated_ranges.append(last_range)

    return sum([ range.size() for range in consolidated_ranges ])


class FreshRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, other):
        return self.contains(other.start) or self.contains(other.end)

    def merge(self, other):
        if not self.overlaps(other):
            raise Exception(f"Can't merge non-overlapping ranges {self} and {other}")
        return FreshRange(min(self.start, other.start), max(self.end, other.end))

    def contains(self, integer):
        return integer >= self.start and integer <= self.end

    def size(self):
        return (self.end - self.start) + 1

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __lt__(self, other):
        if self.start == other.start:
            return self.end < other.end
        return self.start < other.start

    def __repr__(self):
        return f"FreshRange[{self.start},{self.end}]"


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, other):
        if other < self:
            if self.left == None:
                self.left = other
            else:
                self.left.add(other)
        else:
            if self.right == None:
                self.right = other
            else:
                self.right.add(other)

    def size(self):
        return 1 + max(
            0 if self.right == None else self.right.size(),
            0 if self.left == None else self.left.size()
        )
        
