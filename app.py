import os
import sys
import numpy as np

# Ajustar path para importar desde raíz
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from strassen.strassen_seq import strassen_secuencial
from strassen.strassen_threads import strassen_paralelo
from strassen.utils import pad_matrix, unpad_matrix
from cache.lru import LRUCache
from cache.mru import MRUCache


def multiply_matrices(A, B, parallel_threshold=128):
    """
    Multiplica matrices A y B seleccionando automáticamente el mejor método.
    - Usa multiplicación clásica para matrices no cuadradas.
    - Usa Strassen para matrices cuadradas, secuencial o paralelo según el tamaño.
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError("El número de columnas de A debe coincidir con el número de filas de B.")

    # Caso no cuadrado → multiplicación clásica
    if A.shape[0] != A.shape[1] or B.shape[0] != B.shape[1]:
        print("[INFO] Usando multiplicación clásica (matrices no cuadradas)")
        return A @ B

    n = A.shape[0]
    # Asegurar potencia de 2
    padded_size = 1 << (n - 1).bit_length()
    A_padded = pad_matrix(A, n)
    B_padded = pad_matrix(B, n)

    if n < parallel_threshold:
        print("[INFO] Usando Strassen secuencial")
        result = strassen_secuencial(A_padded, B_padded)
    else:
        print("[INFO] Usando Strassen paralelo")
        result = strassen_paralelo(A_padded, B_padded)

    return unpad_matrix(result, n)


if __name__ == "__main__":
    # Ejemplo de uso
    size = 256
    A = np.random.randint(0, 10, (size, size))
    B = np.random.randint(0, 10, (size, size))

    C = multiply_matrices(A, B, parallel_threshold=128)
    print("Resultado shape:", C.shape)
    print("Resultado ejemplo (5x5):\n", C[:5, :5])

    # Ejemplo de uso de cachés
    print("\n[TEST] LRU Cache:")
    lru = LRUCache(3)
    lru.put(1, 'A')
    lru.put(2, 'B')
    lru.put(3, 'C')
    print(lru.cache)
    lru.get(2)
    lru.put(4, 'D')
    print(lru.cache)

    print("\n[TEST] MRU Cache:")
    mru = MRUCache(3)
    mru.put(1, "A")
    mru.put(2, "B")
    mru.put(3, "C")
    print(mru)
    mru.get(2)
    mru.put(4, "D")
    print(mru)

