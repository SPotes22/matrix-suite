from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Indica que la clave no está en la caché
        
        # Mueve el elemento al final para marcarlo como recientemente usado
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Mueve la clave al final, ya que fue usada recientemente
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Si la caché está llena, elimina el elemento menos recientemente usado (LRU)
            self.cache.popitem(last=False)  # `last=False` elimina el primer elemento

        # Inserta el nuevo valor en la caché
        self.cache[key] = value

# Uso de la caché LRU
lru = LRUCache(3)
lru.put(1, 'A')
lru.put(2, 'B')
lru.put(3, 'C')
print(lru.cache)  # {1: 'A', 2: 'B', 3: 'C'}

lru.get(2)  # Accedemos a 'A', lo vuelve más reciente
print(lru.cache)# 1a 3c 2b 
lru.put(4, 'D')  # Se elimina el menos usado (2: 'B')
print(lru.cache)  # {3: 'C', 2: 'B' , 4: 'D'}
