from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris = load_iris()

'''
print "\n".join(iris.feature_names)
print "\n".join(iris.target_names)
print iris.data[0]
print iris.target[0]
'''

# training data
# removes testing_data entires form iris.data and iris.target
test_idx = [0, 50, 100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis = 0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print test_data
print test_target
print clf.predict(test_data)