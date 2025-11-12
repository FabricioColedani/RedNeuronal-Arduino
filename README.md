# 🚗 Proyecto: Coche Arduino con Inteligencia Artificial  
**Actividad del 05/11/2025**

Implementación y análisis del proyecto original:  

👉 [Programa un coche Arduino con Inteligencia Artificial](https://www.aprendemachinelearning.com/programa-un-coche-arduino-con-inteligencia-artificial/)
  
---

## 🧠 1. Arquitecturas observadas

### 🔸 Red neuronal (software)
- **Arquitectura base (original):** `2 → 3 → 4`
  - 2 entradas (sensores)
  - 3 neuronas ocultas
  - 4 salidas (motores)
- **Arquitectura extendida (actividad):** `4 → 6 → 5`
  - Se agregaron **2 entradas nuevas** y **1 salida adicional**
  - Activación `tanh`, entrenamiento por descenso de gradiente
  - Entrenamiento en Python/Colab, ejecución en Arduino (solo propagación hacia adelante)

### 🔸 Arquitectura hardware
- **Arduino UNO** como unidad de control
- **Sensor ultrasónico + servo**: detección de obstáculos en distintas direcciones
- **Módulo L298N**: control de motores DC
- **Red neuronal embebida**: ejecución directa de las operaciones `W·X + b` en Arduino
- **Flujo:** sensores → normalización → red neuronal → señales PWM → motores

---

## 🧩 2. Enfoques de resolución de problemas

- **Aprendizaje supervisado:** se parte de una tabla de verdad pequeña con salidas esperadas.
- **Red neuronal feed-forward:** se ajustan pesos para generalizar los patrones de control.
- **Entrenamiento externo:** en Colab/Python para ahorrar recursos en Arduino.
- **Forward en microcontrolador:** sólo se cargan los pesos finales para inferencia.
- **Diseño híbrido:** mezcla reglas lógicas + aprendizaje supervisado.
- **Iteración práctica:** se entrena, prueba en simulador Wokwi, y se ajustan pesos según el comportamiento.

---

## ⚙️ 3. Entrenamiento de la red neuronal

Se ejecutó el entrenamiento en Python replicando la estructura del Colab original.

- **Versión original:** `2 → 3 → 4`, 1200 epochs, costo ↓ de 1.73 a 0.07  
- **Versión extendida:** `4 → 6 → 5`, 2500 epochs, costo ↓ de 1.53 a 0.02  
- Activación `tanh`, tasa de aprendizaje `0.03`, error cuadrático medio (MSE)

Archivos generados:
- `entranamiento.py` — script reproducible de entrenamiento
- `resumen.json` — resumen de resultados y predicciones
- `tablas.json` — tablas de verdad por integrante

---

## 🔄 4. Simulación con nuevas entradas y salidas

### Cambios realizados:
- **Nuevas entradas:**  
  1. `sensor_luz` (-1 = oscuro, 0 = medio, 1 = claro)  
  2. `sensor_inclinacion` (-1 = izquierda, 0 = nivel, 1 = derecha)
- **Nueva salida:** `motor5` (alerta o indicador)

### Ejemplos de prueba:
| Entrada simulada | Salida predicha (bin) |
|------------------|----------------------|
| `[0, -1, -1, 0]` | `[0, 1, 0, 1, 1]` |
| `[1, 0, 1, 1]`   | `[0, 1, 1, 1, 0]` |

---

## 👥 5. Tablas de verdad por integrante del equipo

Cada miembro generó una variante en la regla de la quinta salida (`motor5`):

| Integrante | Regla aplicada | Descripción |
|-------------|----------------|-------------|
| **Fabricio Coledani** | `1` si `sensor_luz == -1` **y** obstáculo centro | Alerta por oscuridad + obstáculo |
| **Dillan Perez Diaz** | Siempre `0` | No usa la salida extra |
| **Benjamin Zazúa y Noel Chimbo** | `1` si `sensor_luz == -1` **o** `sensor_inclinacion != 0` | Más sensible (oscuridad o inclinación) |
| **Tomas Urquia** | `1` si `sensor_inclinacion == 1` | Alerta por inclinación derecha |
| **Nicolas Moreno** | `1` si `sensor_luz == 1` **y** `sensor_inclinacion == 0` | Activa solo en luz óptima y nivelado |

👉 Las tablas están en este archivo excel
- https://docs.google.com/spreadsheets/d/1aK1TvannO47bVlOhl1PU8Wm3iS7VhvXVB0-cDoDJx3Q/edit?usp=sharing.

---

## 🧰 Archivos del repositorio

| Archivo | Descripción |
|----------|-------------|
| `entrenamiento.py` | Script de entrenamiento de la red |
| `resumen.json` | Resultados y predicciones |
| `README.md` | Este resumen |

---

## 🧾 8. Autores
- Fabricio Coledani, Dillan Perez, Nicolas Moreno, Tomas Urquia, Noel Chimbo y Benjamin Zazúa
- Carrera: Programación Full Stack – Universidad Provincial de Córdoba
- Fecha: 05/11/2025
