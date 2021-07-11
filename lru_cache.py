"""
This LRU cache implementation is built on top of Python's built in OrderedDict data structure. OrderedDict itself is implemented as a hash table, maintaining an average time complexity of O(1) across lookup, insertion, and deletion.

Space complexity is constrained by the cache capacity set at initialization and is defined as O(n).
"""

from collections import OrderedDict


class LruCache:
    """Least Recently Used Cache"""

    def __init__(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError(f"Capacity must be an int: received {capacity}")
        elif capacity <= 0:
            raise ValueError("Capacity must be > 0: received {capacity}")

        self.cache = OrderedDict()
        self.capacity = capacity

    def __repr__(self):
        print(self.cache)

    def get(self, key):
        if key not in self.cache:
            return -1

        value = self.cache.pop(key)
        self.cache[key] = value

        return value

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value


# Test Helper

def cyan(start, end=""):
    print("\033[96m{}\033[00m{}" .format(start, end))


print("\nInit LRU_Cache...")
cache = LruCache(5)

print("Set values: (1, 1), (2, 2), (3, 3), (4, 4)\n")
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)

# return 1
cyan("Test 1: expect cache.get(1) == 1")
assert cache.get(1) == 1, "    Failed: cache.get(1)"
print("1: PASS\n")

# return 1
cyan("Test 1: expect cache.get(2) == 2")
assert cache.get(2) == 2, "    Failed: cache.get(2)"
print("2: PASS\n")

# return -1  (9 is not in the cache)
cyan("Test 3: expect cache.get(9) == -1")
assert cache.get(9) == -1, "    Failed: cache.get(9)"
print("3: PASS\n")

print("\nSet values: (5, 5), (6, 6)\n")
cache.set(5, 5)
cache.set(6, 6)

# return 5
cyan("\nTest 4: expect cache.get(5) == 5")
assert cache.get(5) == 5, "    Failed: cache.get(5, 5)"
print("4: PASS\n")

# return 6
cyan("Test 5: expect cache.get(6) == 6")
assert cache.get(6) == 6, "    Failed: cache.get(6, 6)"
print("5: PASS\n")

# return -1 (hit capacity & 3 was least recently used)
cyan("Test 6: expect cache.get(3) == -1")
assert cache.get(3) == -1, "    Failed: cache.get(3)"
print("6: PASS\n")


try:
    cyan("Test 7: expect ValueError for negative capacity")
    cache = LruCache(-1)
    print("7: Fail — expected ValueError for negative capacity")
except ValueError:
    print("Capacity must be greater than 0!")
    print("7: PASS\n")

try:
    cyan("Test 8: expect TypeError for invalid parameter")
    cache = LruCache(None)
    print("8: Fail — expected TypeError")
except TypeError:
    print("Capacity must be an integer!")
    print("8: PASS\n")
