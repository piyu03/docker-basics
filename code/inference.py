import pickle
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import metrics

print(sklearn.__version__)
filename = 'rf.pkl'
# pickle.dump(clf, open(filename, 'wb'))

# some time later...

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
# X_test = pd.read_csv("testing.csv", delimiter=";")
sample=[[50000.0,31,2,3,1,0,0]]
y_pred = loaded_model.predict(sample)
print(y_pred)