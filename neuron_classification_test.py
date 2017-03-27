#load stored training model
from sklearn.externals import joblib
import numpy as np

if __name__ =="__main__":
    clf = joblib.load("neuron_savemodel.pkl")
    dn_w = joblib.load("dict.pkl")
    test_feature = []
    
    #print dn_w
    
    ids = [] 
    for i, line in enumerate(open("test.txt")):
        fields = line.strip().split(" ")
        ids.append(fields[0]) # id
        f_fields = fields[1].strip().split(",")
        test_feature.append(map(float, f_fields))
    
    test_feature = np.array(test_feature)
    result = clf.predict(test_feature)
    f = open("result.csv", "wt")
    
    f.write("id,cuisine\n")
    for i, res in enumerate(result):
        f.write(ids[i])
        f.write(",")
        f.write(dn_w[res])
        f.write("\n") 
