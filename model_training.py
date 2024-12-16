from sklearn.linear_model import LogisticRegression # type: ignore
from sklearn.svm import SVC # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.metrics import accuracy_score, confusion_matrix # type: ignore

def train_models(X_train, y_train):
    # Logistic Regression
    log_reg = LogisticRegression(max_iter=1000, solver='lbfgs')  # Ensure solver is specified for compatibility
    log_reg.fit(X_train, y_train)

    # Support Vector Machine
    svm = SVC(kernel='linear', probability=True)  # Added `probability=True` for compatibility with some metrics
    svm.fit(X_train, y_train)

    return log_reg, svm

