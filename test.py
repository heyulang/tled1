from sklearn import  datasets
from sklearn import  svm
clf = svm.svc(gamma=0.001,c=100.)
digits = datasets.load_digits()
clf.fit(digits.data[:-1],digits.target[:-1])
result=clf.predict(digits.data[-1])
pprint(resuli)