import numpy as np
np.random.seed(42)

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def load_mnist():
    """Load the MNIST dataset and return the training and testing sets.

    Returns:
        X_train (np.ndarray): Training data
        X_test (np.ndarray): Testing data
        y_train (np.ndarray): Training labels
        y_test (np.ndarray): Testing
    """

    # Load MNIST data from sklearn
    mnist = fetch_openml('mnist_784', as_frame=False, cache=True, version=1)
    X, y = mnist["data"], mnist["target"].astype(np.int)

    # Normalize the data
    X = X / 255.0

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # One-hot encode the labels
    encoder = OneHotEncoder(sparse=False)
    y_train = encoder.fit_transform(y_train.reshape(-1, 1))
    y_test = encoder.transform(y_test.reshape(-1, 1))

    return X_train, X_test, y_train, y_test

def initialize_parameters(input_size, hidden_size, output_size):
    """Initialize the weights and biases of the neural network.

    Args:
        input_size (int): Number of input features
        hidden_size (int): Number of units in the hidden layer
        output_size (int): Number of output units

    Returns:
        W1 (np.ndarray): Weights of the input layer
        b1 (np.ndarray): Biases of the input layer
        W2 (np.ndarray): Weights of the hidden layer
        b2 (np.ndarray): Biases of the hidden layer
    """
    # ====================
    # SEU CÓDIGO AQUI (~4 linhas)
    # ====================
    W1 = None
    b1 = None
    W2 = None
    b2 = None

    return W1, b1, W2, b2

# Forward pass
def forward(X, parameters):
    """Perform the forward pass of the neural network.

    Args:
        X (np.ndarray): Input data
        parameters (tuple): Weights and biases of the neural network

    Returns:
        Z1 (np.ndarray): Output of the first linear layer
        A1 (np.ndarray): Output of the first activation function
        Z2 (np.ndarray): Output of the second linear layer
        A2 (np.ndarray): Output of the second activation function
    """
    W1, b1, W2, b2 = parameters

    # ====================
    # SEU CÓDIGO AQUI (~4 linhas)
    # ====================
    Z1 = None
    A1 = None
    Z2 = None
    A2 = None
    
    return Z1, A1, Z2, A2

# Activation functions
def relu(Z):
    """Compute the ReLU activation function.

    Args:
        Z (np.ndarray): Output of the linear layer
    
    Returns:
        A (np.ndarray): Output of the activation function
    """
    # ====================
    # SEU CÓDIGO AQUI (1 linha)
    # ====================
    return 0

def relu_derivative(Z):
    """Compute the derivative of the ReLU activation function.

    Args:
        Z (np.ndarray): Output of the linear layer
    
    Returns:
        dA (np.ndarray): Derivative of the activation function
    """
    return Z > 0

def softmax(Z):
    """Compute the softmax activation function.

    Args:
        Z (np.ndarray): Output of the linear layer
    
    Returns:
        A (np.ndarray): Output of the activation function
    """
    # ====================
    # SEU CÓDIGO AQUI (~2 linhas)
    # ====================
    return 0

# Loss function
def cross_entropy_loss(y_true, y_pred):
    """Compute the cross-entropy loss.

    Args:
        y_true (np.ndarray): True labels
        y_pred (np.ndarray): Predicted labels

    Returns:
        loss (float): Loss value
    """
    # ====================
    # SEU CÓDIGO AQUI (~3 linhas)
    # ====================
    return 0

# Backward pass
def backward(X, y, W2, Z1, A1, A2):
    n_samples = X.shape[0]
    
    dZ2 = A2 - y
    dW2 = np.dot(A1.T, dZ2) / n_samples
    db2 = np.sum(dZ2, axis=0, keepdims=True) / n_samples
    dA1 = np.dot(dZ2, W2.T)
    
    dZ1 = dA1 * relu_derivative(Z1)
    dW1 = np.dot(X.T, dZ1) / n_samples
    db1 = np.sum(dZ1, axis=0, keepdims=True) / n_samples
    
    return dW1, db1, dW2, db2

def gradient_descent_step(X, y, parameters, learning_rate=0.01):
    """Perform one step of gradient descent.

    Args:
        X (np.ndarray): Input data
        y (np.ndarray): True labels
        parameters (tuple): Weights and biases of the neural network
        learning_rate (float): Learning rate for gradient descent

    Returns:
        parameters (tuple): Updated weights and biases
        loss (float): Loss value
    """
    W1, b1, W2, b2 = parameters
    # ====================
    # SEU CÓDIGO AQUI (~7 linhas)
    # ====================

    return (W1, b1, W2, b2), 0

def accuracy(y_true, y_pred):
    """Compute the accuracy of the model.

    Args:
        y_true (np.ndarray): True labels
        y_pred (np.ndarray): Predicted labels

    Returns:
        accuracy (float): Accuracy value
    """
    # ====================
    # SEU CÓDIGO AQUI (1 linha)
    # ====================
    return 0
    