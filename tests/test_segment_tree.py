import pytest
from data_structures.segment_tree import *
from random import randint, seed, shuffle

seed(123)

N = 10000

def generate_arr_update_pairs(n):
    arr = [randint(-N, N) for _ in range(n)]
    perm = list(range(n))
    shuffle(perm)
    updates = [(index, value) for index, value in zip(perm, (randint(-N, N) for _ in range(n)))]
    return arr, updates


ARR_UPDATES = (generate_arr_update_pairs(n) for n in [1, 4, 5, 6, 7, 16, 17, 24, 25, 31])

def loop_array_sum(st, arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            assert st.range(i, j) == sum(arr[i:j+1])

@pytest.mark.parametrize("arr_updates", ARR_UPDATES)
def test_sum_segment_tree(arr_updates):
    arr, updates = arr_updates
    st = SumSegmentTree(arr.copy())
    loop_array_sum(st, arr)
    for index, value in updates:
        st.update(index, value)
        arr[index] = value
        loop_array_sum(st, arr)
