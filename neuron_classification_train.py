import numpy as np
from sklearn.externals import joblib
from collections import defaultdict
from sklearn.neural_network import MLPClassifier

if __name__=="__main__":
    train_feature = []
    train_label = []
    test_feature = []

    for i, line in enumerate(open("train.txt")):
        fields = line.strip().split(" ")        
        train_label.append(fields[0])
        
        f_fields = fields[1].strip().split(",")
        train_feature.append(map(float, f_fields))
   
#    for i, line in enumerate(open("test.txt")):
#        fields = line.strip().split(" ")
        
#        f_fields = fields[0].strip().split(",")
#        test_feature.append(map(float, f_fields))

    train_feature = np.array(train_feature)
#    test_feature = np.array(test_feature)

    #print max(max(feats) for feats in test_feature)
    
    print test_feature
    counter = 0
    dw_n = defaultdict()
    dn_w = defaultdict()
    train_label_num = []
    for label in train_label:
        if label not in dw_n:
            dw_n[label] = counter
            counter+=1
        train_label_num.append(dw_n[label])
    
    for word in dw_n:
        dn_w[dw_n[word]] = word
    
#    print "classes", d

    train_label_num=np.array(train_label_num)

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(45, 40, 33, 30, 25), random_state=1)
    
    clf.fit(train_feature, train_label_num)
    
    joblib.dump(clf, "neuron_savemodel.pkl")
    joblib.dump(dn_w, "dict.pkl")

   # result = clf2.predict(test_feature)
   # f = open("result.csv", "w")
   # for res in result:
   #     f.write(dn_w[res])
   #     f.write("\n")
