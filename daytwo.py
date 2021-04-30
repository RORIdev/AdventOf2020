def readfile():
    with open("inputs/2.txt") as f:
        content = f.readlines()
    return content


def validate_one(_str) -> bool:
    # i could've regex'd but meh. AoC.
    (condition, _pass) = (_str.split(":")[0].split(' '), _str.split(":")[1].strip())
    (_min, _max, letter) = (int(condition[0].split('-')[0]), int(condition[0].split('-')[1]), condition[1])
    _count = _pass.count(letter)
    return _min <= _count <= _max

def validate_two(_str) -> bool:
    (condition, _pass) = (_str.split(":")[0].split(' '), _str.split(":")[1].strip())
    (idx, iidx, letter) = (int(condition[0].split('-')[0]), int(condition[0].split('-')[1]), condition[1])
    (a, b) = (_pass[idx-1], _pass[iidx-1])
    if a == letter and b != letter:
        return True
    elif b == letter and a != letter:
        return True
    else:
        return False


def solve():
    data = readfile()
    one = [validate_one(x) for x in data]
    two = [validate_two(x) for x in data]
    print(f'[Advent of Code | Day 2 (Part 1)] Solution : {one.count(True)}')
    print(f'[Advent of Code | Day 2 (Part 2)] Solution : {two.count(True)}')

