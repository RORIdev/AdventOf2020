# I'll need to make a finite Y-tape. Something alike a piston feed tape.
# The right term for it is a circular buffer.
# The idea is to implement wrap-around logic instead of cloning the thing over and over
# Again i'm bad with algorithms. That's just how it is

import collections
from functools import reduce


def readfile():
    with open("inputs/3.txt") as f:
        content = f.readlines()
    return content


def gen_buffer(size) -> collections.deque:
    dq = collections.deque(maxlen=size)
    for i in range(size):
        dq.append(i)
    return dq


# pure state monad
def __state_get_nex_state(state, offset, dq) -> (int, int):
    x, y = state
    offset_x, offset_y = offset
    if x + offset_x >= len(dq):
        wrapped_x = (x+offset_x) - len(dq)
        return dq[wrapped_x], y + offset_y
    else:
        return dq[x + offset_x], y + offset_y


def is_tree_at_pos(pos, _map) -> bool:
    x, y = pos
    return _map[y][x] == '#'


def solve_for(_map, offset) -> int:
    dq = gen_buffer(len(_map[0]))
    count = 0
    state = (0, 0)
    while state[1] != len(_map)-1:
        state = __state_get_nex_state(state, offset, dq)
        if is_tree_at_pos(state, _map):
            count += 1

    return count


def solve_one(_map) -> int:
    return solve_for(_map, (3, 1))


def solve_two(_map) -> int:
    offsets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    solutions = [solve_for(_map, x) for x in offsets]
    return reduce((lambda x, y: x * y), solutions)


def solve():
    _map = [list(ln.strip()) for ln in readfile()]
    one = solve_one(_map)
    two = solve_two(_map)
    print(f'[Advent of Code | Day 3 (Part 1)] Solution : {one}')
    print(f'[Advent of Code | Day 3 (Part 2)] Solution : {two}')
