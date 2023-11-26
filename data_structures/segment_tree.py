class SegmentTree:
    def __init__(self, arr, fn):
        self._arr = arr
        self._tree = []
        self._fn = fn
        self._last_index = len(arr)-1
        self._construct(arr, 0, self._last_index, 0)

    def _construct(self, arr, left, right, pos):
        while pos >= len(self._tree):
            self._tree.append(None)
        if left == right:
            self._tree[pos] = arr[left]
            return

        mid = (left+right)//2
        self._construct(arr, left, mid, 2*pos+1)
        self._construct(arr, mid+1, right, 2*pos+2)
        self._tree[pos] = self._fn(self._tree[2*pos+1], self._tree[2*pos+2])

    def update(self, index, value):
        if index < 0:
            index += self._last_index + 1
        if not (0 <= index <= self._last_index):
            raise IndexError(f'Index out of range for array length {self._last_index+1}')
        self._update(index, value, 0, self._last_index, 0)
        self._arr[index] = value

    def _update(self, index, value, left, right, pos):
        if left == right:
            self._tree[pos] = value
            return

        mid = (left+right)//2
        if index <= mid:
            self._update(index, value, left, mid, 2*pos+1)
        else:
            self._update(index, value, mid+1, right, 2*pos+2)
        self._tree[pos] = self._fn(self._tree[2*pos+1], self._tree[2*pos+2])

    def range(self, left, right):
        return self._range(left, right, 0, self._last_index, 0)

    def _range(self, leftq, rightq, left, right, pos):
        if rightq < left or right < leftq:
            return None
        if leftq <= left <= right <= rightq:
            return self._tree[pos]

        mid = (left+right)//2
        left_res = self._range(leftq, rightq, left, mid, 2*pos+1)
        right_res = self._range(leftq, rightq, mid+1, right, 2*pos+2)
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return self._fn(left_res, right_res)

    def view_tree(self):
        print(self._tree)

    def get_arr(self):
        return self._arr


class SumSegmentTree(SegmentTree):
    def __init__(self, arr):
        super().__init__(arr, lambda x, y: x+y)


class MinSegmentTree(SegmentTree):
    def __init__(self, arr):
        super().__init__(arr, min)


class MaxSegmentTree(SegmentTree):
    def __init__(self, arr):
        super().__init__(arr, max)
