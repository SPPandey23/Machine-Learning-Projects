
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


def tune_logistic_regression(X_train, y_train):

    param_grid = {
        "C": [0.1, 1.0, 10.0],
        "solver": ["liblinear"]
    }

    grid = GridSearchCV(
        LogisticRegression(max_iter=1000),
        param_grid,
        cv=5
    )

    grid.fit(X_train, y_train)

    print("Best Logistic Regression Params:", grid.best_params_)
    return grid.best_estimator_


def tune_random_forest(X_train, y_train):

    param_grid = {
        "n_estimators": [10, 100, 200],
        "max_depth": [None, 5, 10],
        "min_samples_split": [2, 5]
    }

    random_search = RandomizedSearchCV(
        RandomForestClassifier(),
        param_grid,
        n_iter=10,
        cv=5,
        random_state=42
    )

    random_search.fit(X_train, y_train)

    print("Best Random Forest Params:", random_search.best_params_)
    return random_search.best_estimator_


def tune_knn(X_train, y_train):

    param_grid = {
        "n_neighbors": [3, 5, 7, 9],
        "weights": ["uniform", "distance"]
    }

    grid = GridSearchCV(
        KNeighborsClassifier(),
        param_grid,
        cv=5
    )

    grid.fit(X_train, y_train)

    print("Best KNN Params:", grid.best_params_)
    return grid.best_estimator_