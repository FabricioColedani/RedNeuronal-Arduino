import numpy as np, json

# === Configuración ===
np.random.seed(42)
lr = 0.03
epochs = 2500
arch = [4, 6, 5]

# === Dataset de ejemplo ===
# Entradas: [distancia, direccion, sensor_luz, inclinacion]
X = np.array([
    [1,  1,  0,  0],
    [1,  0, -1,  0],
    [1, -1,  1,  1],
    [0,  1,  0, -1],
    [0,  0, -1,  0],
    [0, -1,  1,  1],
    [-1, 1,  0,  0],
    [-1, 0, -1,  0],
    [-1, -1, 1, -1]
])

# Salidas esperadas (4 motores + 1 salida extra)
Y = np.array([
    [1,0,0,1,0],
    [0,1,0,1,1],
    [1,0,1,0,0],
    [0,1,1,0,0],
    [1,0,0,1,1],
    [0,1,0,1,0],
    [1,0,1,0,0],
    [0,1,1,0,1],
    [1,0,0,1,0]
])

# === Inicialización de pesos ===
W1 = np.random.randn(arch[0], arch[1])
b1 = np.zeros((1, arch[1]))
W2 = np.random.randn(arch[1], arch[2])
b2 = np.zeros((1, arch[2]))

# === Funciones auxiliares ===
def tanh(x): return np.tanh(x)
def dtanh(x): return 1 - np.tanh(x)**2

# === Entrenamiento ===
for epoch in range(epochs):
    # Forward
    z1 = X @ W1 + b1
    a1 = tanh(z1)
    z2 = a1 @ W2 + b2
    a2 = tanh(z2)
    loss = np.mean((Y - a2)**2)

    # Backprop
    dz2 = (Y - a2) * dtanh(z2)
    dW2 = a1.T @ dz2
    db2 = np.sum(dz2, axis=0, keepdims=True)

    dz1 = dz2 @ W2.T * dtanh(z1)
    dW1 = X.T @ dz1
    db1 = np.sum(dz1, axis=0, keepdims=True)

    # Update
    W1 += lr * dW1
    b1 += lr * db1
    W2 += lr * dW2
    b2 += lr * db2

    if epoch % 500 == 0:
        print(f"Epoch {epoch}/{epochs}, loss={loss:.4f}")

# === Guardar resultados ===
resumen = {
    "arquitectura": arch,
    "loss_final": float(loss),
    "W1": W1.tolist(),
    "b1": b1.tolist(),
    "W2": W2.tolist(),
    "b2": b2.tolist()
}

with open("summary.json", "w") as f:
    json.dump(resumen, f, indent=2)

print("Entrenamiento completado. Resultados guardados en summary.json.")
