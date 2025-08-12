# Code Review for mru.py

This code implements a **Most Recently Used (MRU) cache** using Python's `OrderedDict` from the `collections` module.  Let's break down the code step by step:

**1. `MRUCache` Class:**

   - `__init__(self, capacity: int)`: This is the constructor.
     - `self.cache = OrderedDict()`: Initializes the cache as an ordered dictionary. `OrderedDict` remembers the order in which keys were inserted.  This is crucial for the MRU implementation.
     - `self.capacity = capacity`: Stores the maximum number of key-value pairs the cache can hold.

   - `get(self, key: int) -> int`: Retrieves a value from the cache.
     - `if key not in self.cache:`: Checks if the key exists in the cache. If not, it returns `-1` indicating a cache miss.
     - `value = self.cache.pop(key)`: If the key is found, it removes the key-value pair from its current position in the `OrderedDict`.
     - `self.cache[key] = value`:  Inserts the key-value pair back into the `OrderedDict`. Because it's being inserted *after* being popped, it becomes the *most recently used* element.  This updates the order in the cache to reflect that this element was just accessed.
     - `return value`: Returns the retrieved value.

   - `put(self, key: int, value: int)`: Inserts or updates a key-value pair in the cache.
     - `if key in self.cache:`: Checks if the key already exists.
       - `self.cache.pop(key)`: If the key exists, it removes the old value.  This ensures that the new value is inserted at the correct (MRU) position.
     - `elif len(self.cache) >= self.capacity:`: Checks if the cache is full.
       - `self.cache.popitem(last=True)`: If the cache is full, it removes the *most recently used* item.  `popitem(last=True)` removes the *last* element inserted (the MRU element) from the `OrderedDict`.  This makes space for the new element.
     - `self.cache[key] = value`: Inserts the new key-value pair into the `OrderedDict`. Because it is inserted, it becomes the most recently used.

   - `__repr__(self)`:  A special method that defines how the `MRUCache` object is represented as a string, making it easier to debug.

**2. How the MRU Logic Works:**

   - The `OrderedDict` is the key to the MRU implementation.
   - **`get()`**:  When an element is accessed using `get()`, it's moved to the *end* of the `OrderedDict`, making it the most recently used.
   - **`put()`**: When a new element is inserted or an existing one is updated, it's placed at the *end* of the `OrderedDict`. If the cache is full, the `popitem(last=True)` method removes the *last* element that was inserted/updated which is considered the most recently used.

**3. Example Usage (Provided in the Code):**

   - `cache = MRUCache(3)`: Creates an MRU cache with a capacity of 3.
   - `cache.put(1, "A")`, `cache.put(2, "B")`, `cache.put(3, "C")`: Adds three elements to the cache.  At this point, the cache is `OrderedDict([(1, 'A'), (2, 'B'), (3, 'C')])`.  The most recently used is 3.
   - `cache.get(2)`: Accesses the element with key 2. This moves the key-value pair (2, "B") to the end of the `OrderedDict`, so it becomes the most recently used. The cache becomes `OrderedDict([(1, 'A'), (3, 'C'), (2, 'B')])`.
   - `cache.put(4, "D")`:  Adds a new element with key 4.  Since the cache is full, the *most recently used* element (2) is removed. The new element (4, "D") is added to the end, resulting in `OrderedDict([(1, 'A'), (3, 'C'), (4, 'D')])`.

**In Summary:**

This code implements an MRU cache using an `OrderedDict` to efficiently keep track of the order in which elements are accessed. `get()` operations promote accessed elements to the end, and `put()` operations either insert new elements at the end or remove existing elements and insert them again at the end. When the cache is full, the last inserted element is removed to make room for new entries, implementing the MRU eviction policy.  The `__repr__` method gives a clear representation of the cache's contents for debugging.
