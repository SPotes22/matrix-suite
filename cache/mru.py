from collections import OrderedDict

class MRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Retornar -1 si la clave no está en la caché
        
        # Mover el elemento al final para marcarlo como el más recientemente usado
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache.pop(key)  # Eliminar el valor viejo

        elif len(self.cache) >= self.capacity:
            # Eliminar el **más recientemente usado** (el último elemento insertado)
            self.cache.popitem(last=True)
        
        # Insertar el nuevo elemento
        self.cache[key] = value

    def __repr__(self):
        return f"MRUCache({self.cache})"

# Prueba de la caché MRU
cache = MRUCache(3)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
print(cache)  # MRUCache(OrderedDict([(1, 'A'), (2, 'B'), (3, 'C')]))

cache.get(2)  # Accede al elemento 2
print(cache)  # MRUCache(OrderedDict([(1, 'A'), (3, 'C'), (2, 'B')]))

cache.put(4, "D")  # Se reemplaza el más recientemente usado (2)
print(cache)  # MRUCache(OrderedDict([(1, 'A'), (3, 'C'), (4, 'D')]))
