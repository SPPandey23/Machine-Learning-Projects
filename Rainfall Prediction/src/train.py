import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from src.data_loader import load_data, preprocess_data, get_X_y
from src.model import create_pipeline

def train():
    
    df = load_data()
    df = preprocess_data(df)
    
    X, y = get_X_y(df)
    
    print(f"Data shape: {df.shape}")
    

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    pipeline = create_pipeline()
    
    pipeline.fit(X_train, y_train)
    
   
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))
    
    print("Saving model to model.joblib...")
    joblib.dump(pipeline, 'model.joblib')
    print("Model saved successfully.")

if __name__ == "__main__":
    train()
