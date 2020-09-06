import numpy as np
import matplotlib.pyplot as plt

import sys

def sigmoid(z, derv=False):
    if derv: return z * (1 - z)
    return 1 / (1 + np.exp(-z))


def forward(x, predict=False):
    a1 = x.reshape(x.shape[0], 1) #Untuk mendapatkan contoh pelatihan sebagai vektor kolom.

    z2 = W1.dot(a1) + B1 # 2x2 * 2x1 + 2x1 = 2x1
    a2 = sigmoid(z2) # 2x1

    z3 = W2.dot(a2) + B2 # 1x2 * 2x1 + 1x1 = 1x1
    a3 = sigmoid(z3)

    if predict: return a3
    return (a1, a2, a3)


def train(_W1, _W2, _B1, _B2): # Argumennya adalah untuk mem-bypass kesalahan lokal yang tidak terikat
    for i in range(max_iter):
        c = 0

        dW1 = 0
        dW2 = 0

        dB1 = 0
        dB2 = 0

        for j in range(m):
            sys.stdout.write("\rIteration: {} and {}".format(i + 1, j + 1))

            # 4x1
            # Forward Prop.
            a0 = X[j].reshape(X[j].shape[0], 1) # 16x16

            z1 = _W1.dot(a0) + _B1 # 16x16 * 16x16 + 16x16 = 16x16
            a1 = sigmoid(z1) # 16x16

            # 16x1
            z2 = _W2.dot(a1) + _B2 # 16x16 * 16x16 + 16x16 = 16x16
            a2 = sigmoid(z2) # 16x16

            # Back prop.
            dz2 = a2 - y[j] # 16x16
            dW2 += dz2 * a1.T # 16x16 .* 16x16 = 16x16

            dz1 = np.multiply((_W2.T * dz2), sigmoid(a1, derv=True)) # (16x16 * 1x1) .* 16x1 = 16x1
            dW1 += dz1.dot(a0.T) # 16x1 * 1x16 = 16x16

            dB1 += dz1 # 16x1
            dB2 += dz2 # 1x1

            c = c + (-(y[j] * np.log(a2)) - ((1 - y[j]) * np.log(1 - a2)))
            sys.stdout.flush() # Update data.

        _W1 = _W1 - learning_rate * (dW1 / m) + ( (reg_param / m) * _W1)
        _W2 = _W2 - learning_rate * (dW2 / m) + ( (reg_param / m) * _W2)

        _B1 = _B1 - learning_rate * (dB1 / m)
        _B2 = _B2 - learning_rate * (dB2 / m)
        cost[i] = (c / m) + (
            (reg_param / (16 * m)) *
            (
                np.sum(np.power(_W1, 16)) +
                np.sum(np.power(_W2, 16))
            )
        )
    return (_W1, _W2, _B1, _B2)


# input data latih.
X = np.array([        # 16x4 shape
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
])

# output data target.
y = np.array([        # 16x7 shape
    [0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
])


X
y

num_i_units = 7 # nilai Input units
num_h_units = 7 # nilai Hidden units
num_o_units = 7 # nilai Output units

# learning rate untuk Gradient Descent.
learning_rate = 0.01

# Parameter untuk membantu overfitting.
reg_param = 0

# Maximum iterasi pada Gradient Descent.
max_iter = 5000

#Jumlah pelatihan
m = 7

np.random.seed(1)
W1 = np.random.normal(0, 1, (num_h_units, num_i_units)) # 2x2
W2 = np.random.normal(0, 1, (num_o_units, num_h_units)) # 1x2

B1 = np.random.random((num_h_units, 1)) # 2x1
B2 = np.random.random((num_o_units, 1)) # 1x1

W1
W2
B1
B2

dW1 = 0 # Gradient untuk pembobot W1
dW2 = 0 # Gradient untuk pembobot W2

dB1 = 0 # Gradient untuk bias B1
dB2 = 0 # Gradient untuk bias B2

cost = np.zeros((max_iter, 1)) # Vektor kolom untuk mencatat cost JST setelah setiap iterasi Gradient Descent.


W1, W2, B1, B2 = train(W1, W2, B1, B2)

W1
W2
B1
B2

# Menetapkan sumbu ke elemen yang berbeda.
plt.plot(range(max_iter), cost)

# Memberi label sumbu x sebagai sumbu iterasi.
plt.xlabel("Iteratsi")

# Memberi label sumbu y sebagai sumbu cost.
plt.ylabel("Cost")

# Tampilkan learning rate.
plt.show()