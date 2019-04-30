import numpy as np
from sklearn.svm import SVC

X = np.array([[0,0], [0, -1], [12,0]] )
y = np.array([-1, -1, 1])

clf = SVC(C = 1e5, kernel = 'linear')
clf.fit(X, y)

print(clf.intercept_, clf.coef_)