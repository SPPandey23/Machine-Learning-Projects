import pandas as pd
import matplotlib.pyplot as plt


def plot_feature_importance(model, feature_names):

    if hasattr(model, "feature_importances_"):

        importance = model.feature_importances_

        df = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importance
        }).sort_values("Importance", ascending=False)

        df.plot(kind="bar", x="Feature", y="Importance")
        plt.title("Feature Importance")
        plt.xticks(rotation=90)
        plt.show()

    else:
        print("This model does not support feature importance")