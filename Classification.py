class sklearn:

   """

   Function: Provide 5 classification algorithms available on sklearn to perform classification tasks
             (Support Vector Machines, K-Nearest Neighbors, Decision Tree, Random Forest, Neural Networks, Gaussian Process Algorithms, All Models (performing the previous 5 classification algorithms)).

   """
    
    def Svm_model(self, DataSet, Label):

    """

    Function: Perform classification task using Support Vector Machine (SVM) algorithm.

    Parameters:

        DataSet: Input feature data, which can be a pandas DataFrame.

        Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

    """

        from sklearn.model_selection import train_test_split
        from sklearn import svm, metrics
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score, f1_score, recall_score
        import pandas as pd
        import numpy as np
        
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        svm_model = svm.SVC()
        svm_model.fit(train_feature, train_label)
        
        test_predict = svm_model.predict(test_feature)

        svm_model_acc = metrics.accuracy_score(test_label, test_predict)
        svm_model_f1 = f1_score(test_label, test_predict, average='weighted')
        svm_model_recall = recall_score(test_label, test_predict, average='weighted')
        
        print("支持向量機(Support Vector Machines)模型準確度：", svm_model_acc)
        print("支持向量機(Support Vector Machines)模型F1分數：", svm_model_f1)
        print("支持向量機(Support Vector Machines)模型Recall：", svm_model_recall)
        
        return 


    def KNeighbors_model(self, DataSet, Label):

    """

    Function: Perform classification task using K-Nearest Neighbors algorithm.

    Parameters:

        DataSet: Input feature data, which can be a pandas DataFrame.

        Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

    """
     
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score, f1_score, recall_score
        from sklearn import metrics
        import pandas as pd
        import numpy as np

        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        KNeighbors_model = KNeighborsClassifier(n_neighbors=2)
        KNeighbors_model.fit(train_feature, train_label)

        test_predict = KNeighbors_model.predict(test_feature)

        KNeighbors_model_acc = metrics.accuracy_score(test_label, test_predict)
        KNeighbors_model_f1 = f1_score(test_label, test_predict, average='weighted')
        KNeighbors_model_recall = recall_score(test_label, test_predict, average='weighted')

        print("最近的鄰居(Nearest Neighbors)模型準確度：", KNeighbors_model_acc)
        print("最近的鄰居(Nearest Neighbors)模型F1分數：", KNeighbors_model_f1)
        print("最近的鄰居(Nearest Neighbors)模型Recall：", KNeighbors_model_recall)

        return

    def DecisionTree_model(self, DataSet, Label):

    """

    Function: Perform classification task using the decision tree algorithm.

    Parameters:

        DataSet: Input feature data, which can be a pandas DataFrame.

        Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

    """

        from sklearn.model_selection import train_test_split
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score, f1_score, recall_score
        from sklearn import tree, metrics
        import pandas as pd
        import numpy as np
        
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        DecisionTree_model = tree.DecisionTreeClassifier()
        DecisionTree_model.fit(train_feature, train_label)

        test_predict = DecisionTree_model.predict(test_feature)

        DecisionTree_model_acc = metrics.accuracy_score(test_label, test_predict)
        DecisionTree_model_f1 = f1_score(test_label, test_predict, average='weighted')
        DecisionTree_model_recall = recall_score(test_label, test_predict, average='weighted')

        print("決策樹(Decision Trees)模型準確度：", DecisionTree_model_acc)
        print("決策樹(Decision Trees)模型F1分數：", DecisionTree_model_f1)
        print("決策樹(Decision Trees)模型Recall：", DecisionTree_model_recall)

        return

    def RandomForest_model(self, DataSet, Label):

    """

    Function: Perform classification task using Random Forest algorithm.

    Parameters:

        DataSet: Input feature data, which can be a pandas DataFrame.

        Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

    """

        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score, f1_score, recall_score
        from sklearn import metrics
        import pandas as pd
        import numpy as np
     
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)

        RandomForest_model = RandomForestClassifier(n_estimators=10)
        RandomForest_model.fit(train_feature, train_label)

        test_predict = RandomForest_model.predict(test_feature)

        RandomForest_model_acc =  metrics.accuracy_score(test_label, test_predict)
        RandomForest_model_f1 = f1_score(test_label, test_predict, average='weighted')
        RandomForest_model_recall = recall_score(test_label, test_predict, average='weighted')


        print("隨機森林(Forests of randomized trees)模型準確度：",RandomForest_model_acc)
        print("隨機森林(Forests of randomized trees)模型F1分數：", RandomForest_model_f1)
        print("隨機森林(Forests of randomized trees)模型Recall：", RandomForest_model_recall)

        return


    def MLP_model(self, DataSet, Label):

    """

    Function: Perform classification task using neural network algorithm.

    Parameters:

        DataSet: Input feature data, which can be a pandas DataFrame.

        Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

    """

        from sklearn.model_selection import train_test_split
        from sklearn.neural_network import MLPClassifier
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score, f1_score, recall_score
        from sklearn import metrics
        import pandas as pd
        import numpy as np

        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)

        MLP_model = MLPClassifier(solver='lbfgs', 
                                 alpha=1e-5,
                                 hidden_layer_sizes=(6, 2), 
                                )

        MLP_model.fit(train_feature, train_label)
        test_predict = MLP_model.predict(test_feature)

        MLP_model_acc =  metrics.accuracy_score(test_label, test_predict)
        MLP_model_f1 = f1_score(test_label, test_predict, average='weighted')
        MLP_model_recall = recall_score(test_label, test_predict, average='weighted')

        print ("神經網路(Neural Network models)模型準確度：",MLP_model_acc)
        print("神經網路(Neural Network models)模型F1分數：", MLP_model_f1)
        print("神經網路(Neural Network models)模型Recall：", MLP_model_recall)

        return


    def GaussianProcess_model(self, DataSet, Label):

    """

    Function: Perform classification tasks using Gaussian process algorithm.

    Parameters:

        DataSet: Input feature data, which can be a pandas DataFrame.

        Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

    """

        from sklearn.model_selection import train_test_split
        from sklearn.gaussian_process import GaussianProcessClassifier
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score, f1_score, recall_score
        from sklearn.gaussian_process.kernels import RBF
        from sklearn import metrics

        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)

        GaussianProcess_model = GaussianProcessClassifier()
        GaussianProcess_model.fit(train_feature, train_label)
 
        test_predict = GaussianProcess_model.predict(test_feature)

        GaussianProcess_model_acc  =  metrics.accuracy_score(test_label, test_predict)
        GaussianProcess_model_f1 = f1_score(test_label, test_predict, average='weighted')
        GaussianProcess_model_recall = recall_score(test_label, test_predict, average='weighted')

        print ("高斯過程(GaussianProcess)模型準確度：",GaussianProcess_model_acc)
        print("高斯過程(GaussianProcess)模型F1分數：", GaussianProcess_model_f1)
        print("高斯過程(GaussianProcess)模型Recall：", GaussianProcess_model_recall)

        return

    def All_model(self, DataSet, Label):

    """

    Function: Perform classification tasks using support vector machines, K-nearest neighbors, decision trees, random forests,               neural networks, Gaussian process algorithms, and calculate accuracy, F1 score, and recall score.

    Parameters:

        DataSet: Input feature data, which can be a pandas DataFrame.

        Label: Label data, which refers to the classification label corresponding to each feature data, and can be a pandas Series.

    """

        from sklearn.model_selection import train_test_split
        from sklearn import svm, metrics
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score, f1_score, recall_score
        import pandas as pd
        import numpy as np
           
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        svm_model = svm.SVC()
        svm_model.fit(train_feature, train_label)
        
        test_predict = svm_model.predict(test_feature)

        svm_model_acc = metrics.accuracy_score(test_label, test_predict)
        svm_model_f1 = f1_score(test_label, test_predict, average='weighted')
        svm_model_recall = recall_score(test_label, test_predict, average='weighted')
               
        from sklearn.neighbors import KNeighborsClassifier

        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)
        KNeighbors_model = KNeighborsClassifier(n_neighbors=2)
        KNeighbors_model.fit(train_feature, train_label)

        test_predict = KNeighbors_model.predict(test_feature)

        KNeighbors_model_acc = metrics.accuracy_score(test_label, test_predict)
        KNeighbors_model_f1 = f1_score(test_label, test_predict, average='weighted')
        KNeighbors_model_recall = recall_score(test_label, test_predict, average='weighted')

        from sklearn.metrics import confusion_matrix
        from sklearn import tree, metrics
        
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)

        DecisionTree_model = tree.DecisionTreeClassifier()
        DecisionTree_model.fit(train_feature, train_label)

        test_predict = DecisionTree_model.predict(test_feature)

        DecisionTree_model_acc = metrics.accuracy_score(test_label, test_predict)
        DecisionTree_model_f1 = f1_score(test_label, test_predict, average='weighted')
        DecisionTree_model_recall = recall_score(test_label, test_predict, average='weighted')

        from sklearn.metrics import confusion_matrix
        from sklearn.ensemble import RandomForestClassifier
   
        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)

        RandomForest_model = RandomForestClassifier(n_estimators=10)
        RandomForest_model.fit(train_feature, train_label)

        test_predict = RandomForest_model.predict(test_feature)

        RandomForest_model_acc =  metrics.accuracy_score(test_label, test_predict)
        RandomForest_model_f1 = f1_score(test_label, test_predict, average='weighted')
        RandomForest_model_recall = recall_score(test_label, test_predict, average='weighted')

        from sklearn.neural_network import MLPClassifier

        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)

        MLP_model = MLPClassifier(solver='lbfgs', 
                                 alpha=1e-5,
                                 hidden_layer_sizes=(6, 2), 
                                )
        MLP_model.fit(train_feature, train_label)

        MLP_model_acc =  metrics.accuracy_score(test_label, test_predict)
        MLP_model_f1 = f1_score(test_label, test_predict, average='weighted')
        MLP_model_recall = recall_score(test_label, test_predict, average='weighted')

        from sklearn.gaussian_process import GaussianProcessClassifier
        from sklearn.gaussian_process.kernels import RBF

        train_feature, test_feature, train_label, test_label = train_test_split(DataSet, Label,test_size=0.2)

        GaussianProcess_model = GaussianProcessClassifier()
        GaussianProcess_model.fit(train_feature, train_label)

        GaussianProcess_model_acc  =  metrics.accuracy_score(test_label, test_predict)
        GaussianProcess_model_f1 = f1_score(test_label, test_predict, average='weighted')
        GaussianProcess_model_recall = recall_score(test_label, test_predict, average='weighted')

        models = pd.DataFrame({
            'Model': ['支持向量機(Support Vector Machines)', 
                      '最近的鄰居(Nearest Neighbors)', 
                      '決策樹(Decision Trees)',
                      '隨機森林(Forests of randomized trees)', 
                      '神經網路(Neural Network models)',
                      '高斯過程(GaussianProcess)'
                     ],
            'Accuracy': [svm_model_acc,
                      KNeighbors_model_acc,
                      DecisionTree_model_acc,
                      RandomForest_model_acc,
                      MLP_model_acc,
                      GaussianProcess_model_acc, 
                      ],
            'F1_Score': [svm_model_f1,
                      KNeighbors_model_f1,
                      DecisionTree_model_f1,
                      RandomForest_model_f1,
                      MLP_model_f1,
                      GaussianProcess_model_f1, 
                      ],
            'Recall': [svm_model_recall,
                      KNeighbors_model_recall,
                      DecisionTree_model_recall,
                      RandomForest_model_recall,
                      MLP_model_recall,
                      GaussianProcess_model_recall, 
                      ]
                       })

        return models
