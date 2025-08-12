# Code Review for lru.py

The code implements a Least Recently Used (LRU) cache using Python's `OrderedDict` from the `collections` module.  Let's break it down step by step:

**1. `LRUCache` Class:**

   - **`__init__(self, capacity: int)`:**  This is the constructor.
     - `self.cache = OrderedDict()`:  It initializes the cache using an `OrderedDict`.  An `OrderedDict` remembers the order in which items were inserted. This is crucial for LRU behavior.
     - `self.capacity = capacity`:  It stores the maximum number of items the cache can hold.

   - **`get(self, key: int) -> int`:** This method retrieves a value from the cache given a `key`.
     - `if key not in self.cache:`:  If the `key` isn't in the cache, it returns `-1`, indicating a cache miss.
     - `self.cache.move_to_end(key)`:  If the `key` *is* in the cache, this is the key to LRU.  `move_to_end(key)` moves the item associated with that `key` to the *end* of the `OrderedDict`. This marks it as the most recently used item.
     - `return self.cache[key]`:  Finally, it returns the value associated with the `key`.

   - **`put(self, key: int, value: int) -> None`:**  This method inserts a `key`-`value` pair into the cache.
     - `if key in self.cache:`: If the `key` is already present in the cache:
       -`self.cache.move_to_end(key)`: The element is moved to the end, marking it as recently used.
     - `elif len(self.cache) >= self.capacity:`: If the cache is full (reached its capacity):
       - `self.cache.popitem(last=False)`: This removes the *least recently used* item.  `popitem(last=False)` removes the *first* item from the `OrderedDict` (the one that was inserted earliest and hasn't been accessed recently).
     - `self.cache[key] = value`:  Regardless of whether an eviction occurred, the new `key`-`value` pair is inserted into the cache (at the end, making it the most recently used item).

**2. Usage Example:**

   - `lru = LRUCache(3)`: Creates an LRUCache with a capacity of 3.
   - `lru.put(1, 'A')`, `lru.put(2, 'B')`, `lru.put(3, 'C')`: Inserts three key-value pairs. The cache is now full: `{1: 'A', 2: 'B', 3: 'C'}`. The order represents the insertion order.
   - `lru.get(2)`: Accesses key `2`. This makes `2` the most recently used, so the `OrderedDict` becomes `{1: 'A', 3: 'C', 2: 'B'}`.
   - `lru.put(4, 'D')`:  Tries to insert `4: 'D'`. The cache is full, so the *least recently used* item (which is `1: 'A'`) is evicted.  Then, `4: 'D'` is inserted, resulting in `{3: 'C', 2: 'B', 4: 'D'}`.

**In Summary:**

The code implements an LRU cache, a data structure that efficiently stores a limited number of key-value pairs.  When the cache is full and a new item needs to be inserted, the least recently used item is evicted to make space.  The `OrderedDict` is cleverly used to track the order of use, making the LRU implementation concise and efficient.  The `get()` operation updates the order when an item is accessed, and the `put()` operation evicts the least recently used item when the capacity is reached.
