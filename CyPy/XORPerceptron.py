import numpy as np

class Perceptron:
    def __init__(self, n_inputs, lr=0.1, epochs=2):
        self.w = np.zeros(n_inputs)
        self.b = 0
        self.lr = lr
        self.epochs = epochs

    def predict(self, x):
        return 1 if np.dot(x, self.w) + self.b >= 0 else 0

    def fit(self, X, y):
        for _ in range(self.epochs):
            for xi, yi in zip(X, y):
                err = yi - self.predict(xi)
                self.w += self.lr * err * xi
                self.b += self.lr * err


X_and = np.array([[0,0],[0,1],[1,0],[1,1]])
y_and = np.array([0, 0, 0, 1])

p = Perceptron(n_inputs=2, lr=0.1, epochs=2)
p.fit(X_and, y_and)

print("AND results:")
for xi in X_and:
    print(f"  {xi} -> {p.predict(xi)}")


X_xor = np.array([[0,0],[0,1],[1,0],[1,1]])
y_xor = np.array([0, 1, 1, 0])

p2 = Perceptron(n_inputs=2, lr=0.1, epochs=100)
p2.fit(X_xor, y_xor)

print("\nSingle perceptron on XOR (will fail):")
for xi, yi in zip(X_xor, y_xor):
    print(f"  {xi} -> got {p2.predict(xi)}, expected {yi}")


# XOR needs an extra layer - just hardcode two AND/OR perceptrons and combine
def xor_network(x):
    # x[0] OR x[1]
    or_w = np.array([1.0, 1.0])
    or_b = -0.5
    or_out = 1 if np.dot(x, or_w) + or_b >= 0 else 0

    # NAND
    nand_w = np.array([-1.0, -1.0])
    nand_b = 1.5
    nand_out = 1 if np.dot(x, nand_w) + nand_b >= 0 else 0

    combined = np.array([or_out, nand_out])
    and_w = np.array([1.0, 1.0])
    and_b = -1.5
    return 1 if np.dot(combined, and_w) + and_b >= 0 else 0

print("\nXOR via 2-layer combo:")
for xi, yi in zip(X_xor, y_xor):
    print(f"  {xi} -> got {xor_network(xi)}, expected {yi}")