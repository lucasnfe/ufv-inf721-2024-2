import learn
import numpy as np 

# Test initialize_parameters
W1, b1, W2, b2 = learn.initialize_parameters(784, 4, 10)
print("-> Testing initialize_parameters")
print("W1:", W1.shape)
print(W1)

print("b1:", b1.shape)
print(b1)

print("W2:", W2.shape)
print(W2)

print("b2:", b2.shape)
print(b2)

# Test relu
print()
print("-> Testing relu")
a = learn.relu(np.array([[-1, 0, 1], [-2, 0, 2]]))
print("a:", a)

# Test softmax
print()
print("-> Testing softmax")
a = learn.softmax(np.array([[1, 2, 3], [4, 5, 6]]))
print("a:", a)

# Test forward
print()
print("-> Testing forward")
X = np.random.randn(2, 784)
parameters = (W1, b1, W2, b2)
Z1, A1, Z2, A2 = learn.forward(X, parameters)
print("Z1:", Z1.shape)
print(Z1)

print("A1:", A1.shape)
print(A1)

print("Z2:", Z2.shape)
print(Z2)

print("A2:", A2.shape)
print(A2)

# Test cross_entropy_loss
print()
print("-> Testing cross_entropy_loss")
y_true = np.array([[0, 1, 0], [1, 0, 0]])
y_pred = np.array([[0.1, 0.6, 0.3], [0.3, 0.4, 0.3]])
loss = learn.cross_entropy_loss(y_true, y_pred)
print("loss:", loss)

# Test gradient_descent_step
print()
print("-> Testing gradient_descent_step")
X = np.random.randn(2, 784)
y = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]])
parameters = (W1, b1, W2, b2)
parameters, loss = learn.gradient_descent_step(X, y, parameters, learning_rate=0.01)
print("loss:", loss)
print("W1:", parameters[0].shape)
print(parameters[0])

print("b1:", parameters[1].shape)
print(parameters[1])

print("W2:", parameters[2].shape)
print(parameters[2])

print("b2:", parameters[3].shape)
print(parameters[3])

# Test accuracy
print()
print("-> Testing accuracy")
y_true = np.array([[0, 1, 0], [1, 0, 0]])
y_pred = np.array([[0.1, 0.6, 0.3], [0.3, 0.4, 0.3]])
acc = learn.accuracy(y_true, y_pred)
print("acc:", acc)

