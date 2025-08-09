from StarClasic import strassen_secuencial
from StraHIlos import strassen_paralelo
import numpy as np

if __name__ == "__main__":
    size = 128  # Cambia a 125, 512, 1024 
    A = np.random.randint(0, 10, (size, size))
    B = np.random.randint(0, 10, (size, size))

    C_seq = strassen_secuencial(A, B)
    C_par = strassen_paralelo(A, B)

    print("¿Son iguales las matrices resultantes?:", np.allclose(C_seq, C_par))
