# Matrix Multiplication Suite (Strassen + Threading + Cache)

Este proyecto implementa una solución optimizada para multiplicación de matrices, incluyendo:

- **Multiplicación clásica** (`n x m` con `m x p`)
- **Algoritmo de Strassen** (versión secuencial y paralela con hilos)
- **Manejo de tamaños no potencia de 2** (padding)
- **Estructuras de caché LRU y MRU** como ejemplo de optimización de memoria
---
## 📂 Estructura
/app.py # Punto de entrada principal
/requirements.txt # Dependencias
/strassen # Implementaciones de Strassen
/cache # LRU y MRU cache## 🚀 Ejecución
```
git clone https://github.com/tuusuario/matrix-suite.git
cd matrix-suite
pip install -r requirements.txt
python app.py
```
---
⚡ Algoritmos
* Clásico: O(n³)

* Strassen: O(n^2.81)

Secuencial para matrices cuadradas pequeñas

Paralelo con hilos para matrices grandes

📊 Benchmarks (ejemplo)
Tamaño	Clásico (s)	Strassen Secuencial (s)	Strassen Paralelo (s)
128x128	0.02	0.015	0.012
512x512	0.45	0.35	0.22
---
Licencia
MIT
Santiago Potes , Materia Sistemas Operativos. UTP
