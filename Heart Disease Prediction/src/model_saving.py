import joblib
def save_model(model, X_train, file_path):

    feature_info = {}

    for col in X_train.columns:
        feature_info[col] = {
            "dtype": str(X_train[col].dtype),
            "unique_values": X_train[col].unique().tolist()
        }

    package = {
        "model": model,
        "feature_info": feature_info
    }

    joblib.dump(package, file_path)
    print("Model saved successfully")