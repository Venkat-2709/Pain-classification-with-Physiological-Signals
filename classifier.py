import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import KFold


# Preprocessing the data.
def preprocess(x, y):
    encoder = LabelEncoder()
    y = y.values.reshape((-1, 1))
    y = encoder.fit_transform(y)
    scalar = StandardScaler()
    x = scalar.fit_transform(x)
    accuracy, precision, recall, matrix = classify(x, y)
    total_mat = np.array(0)
    for mat in matrix:
        mat = np.array(mat)
        total_mat = np.add(total_mat, mat)

    avg_mat = np.divide(total_mat, len(matrix))
    avg_acc = np.mean(accuracy)
    avg_pre = np.mean(precision)
    avg_rec = np.mean(recall)

    return avg_acc, avg_pre, avg_rec, avg_mat


# Training and testing the data using 10-fold Random Forest Classifier.
def classify(x, y):
    accuracy = []
    precision = []
    recall = []
    matrix = []
    print('Training and Testing for 10-Fold Cross Validation using Random Forest Classifier.')
    kf = KFold(n_splits=10, shuffle=True, random_state=0)
    for train_index, test_index in kf.split(x):
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]
        classifier = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=0)
        classifier.fit(x_train, y_train)
        y_pred = classifier.predict(x_test)
        accuracy.append(accuracy_score(y_test, y_pred))
        precision.append(precision_score(y_test, y_pred))
        recall.append(recall_score(y_test, y_pred))
        matrix.append(confusion_matrix(y_test, y_pred))

    return accuracy, precision, recall, matrix
