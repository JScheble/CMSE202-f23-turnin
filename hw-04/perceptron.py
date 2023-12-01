# Code generated by ChatGPT (GPT-4); Accessed on November 9, 2023 via chat.openai.com
# Prompt: Produce an implementation of the perceptron classifier as a Python class

import numpy as np

class Perceptron(object):
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.learning_rate = learning_rate  # Learning rate
        self.n_iters = n_iters              # Number of iterations over the training set
        self.activation_func = self._unit_step_func
        self.weights = None                 # Weights after fitting
        self.bias = None                    # Bias after fitting

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                
                # Perceptron update rule
                update = self.learning_rate * (y_[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def _unit_step_func(self, x):
        return np.where(x > 0, 1, 0)

# Example usage:
if __name__ == "__main__":
    from sklearn.model_selection import train_test_split
    from sklearn import datasets
    import matplotlib.pyplot as plt

    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    # Iris dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # Binary classification, so let's take only two classes
    X = X[y != 2]
    y = y[y != 2]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    p = Perceptron(learning_rate=0.01, n_iters=1000)
    p.fit(X_train, y_train)
    predictions = p.predict(X_test)

    print("Perceptron classification accuracy", accuracy(y_test, predictions))