# Requires: python -m pip install scikit-learn
try:
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.neural_network import MLPClassifier
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score
except ImportError:
    raise SystemExit("Install dependency: python -m pip install scikit-learn")

if __name__ == "__main__":
    X, y = make_classification(n_samples=300, n_features=6, n_informative=4,
                               n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    model = make_pipeline(StandardScaler(),
                          MLPClassifier(hidden_layer_sizes=(8, 4), max_iter=1500, random_state=42))
    model.fit(X_train, y_train)
    print("Test accuracy:", round(accuracy_score(y_test, model.predict(X_test)) * 100, 2), "%")
