# Requires: python -m pip install scikit-learn
try:
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
except ImportError:
    raise SystemExit("Install dependency: python -m pip install scikit-learn")

X = [[1,50],[2,55],[2,65],[3,70],[4,80],[5,85],[6,90],[7,95],[1,45],[4,75]]
y = ["Needs Support","Needs Support","Needs Support","Pass","Pass","Pass","Pass","Pass","Needs Support","Pass"]

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y)
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Predictions:", predictions.tolist())
    print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
