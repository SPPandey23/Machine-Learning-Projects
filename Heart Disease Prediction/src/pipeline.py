# pipeline.py
import matplotlib
matplotlib.use('Agg')

from src.data_ingestion import load_data
from src.eda import run_eda
from src.data_preprocessing import preprocess_data
from src.hyperparameter import (
    tune_logistic_regression,
    tune_random_forest,
    tune_knn
)
from src.model_evaluation import evaluate_model
from src.feature_importance import plot_feature_importance
from src.model_saving import save_model


def run_pipeline(data_path):

    print("Starting Pipeline...\n")

    df = load_data(data_path)

    run_eda(df)
    X_train, X_test, y_train, y_test = preprocess_data(df)

    print("\n--- Logistic Regression ---")
    lr_model = tune_logistic_regression(X_train, y_train)
    evaluate_model(lr_model, X_test, y_test)

    print("\n--- Random Forest ---")
    rf_model = tune_random_forest(X_train, y_train)
    evaluate_model(rf_model, X_test, y_test)
    plot_feature_importance(rf_model, X_train.columns)

    print("\n--- KNN ---")
    knn_model = tune_knn(X_train, y_train)
    evaluate_model(knn_model, X_test, y_test)

    save_model(rf_model, X_train, "best_model.joblib")

    print("\nPipeline Completed Successfully.")


if __name__ == "__main__":
    run_pipeline("D:/ks/heart.csv")