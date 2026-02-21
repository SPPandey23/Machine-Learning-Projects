# models.py

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


def train_logistic_regression(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    print("Logistic Regression trained")
    return model


def train_random_forest(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    print("Random Forest trained")
    return model


def train_knn(X_train, y_train):
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    print("KNN trained")
    return model