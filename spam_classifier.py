import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import pickle

class SpamClassifier:

    def saveModel(self):
        train = pd.read_csv('train.csv')
        vectoriser = CountVectorizer()
        count = vectoriser.fit_transform(train['Message'].values)

        # print(count)

        pickle.dump(vectoriser, open('count-transform.pkl', 'wb'))

        target = train['Class'].values

        # Model Build

        classifier = MultinomialNB()
        classifier.fit(count, target)

        # Creating the pickle file for Naive Bayes Model

        filename = 'spam-or-ham-classifier.pkl'
        pickle.dump(classifier, open(filename, 'wb'))

        print("Models are saved. Bye...\U0001F44B")

    def checkAccuracy(self):
        train = pd.read_csv('train.csv')
        vectoriser = CountVectorizer()
        count = vectoriser.fit_transform(train['Message'].values)

        target = train['Class'].values

        classifier = MultinomialNB()
        classifier.fit(count, target)

        test = pd.read_csv('test.csv')


        prediction = vectoriser.transform(test['Message'])

        predictionfromNaiveBayes = classifier.predict(prediction)

        prediction_ans = pd.read_csv('prediction_ans.csv')
        predictionfromNaiveBayes = {'Class': predictionfromNaiveBayes}
        predictionfromNaiveBayes = pd.DataFrame(predictionfromNaiveBayes)

        #for checking accuracy
        right = 0
        for i in range(prediction_ans.shape[0]):
            if str(prediction_ans['Class'][i]) == str(predictionfromNaiveBayes['Class'][i]):
                right = right+1
                
        #accuracy
        accuracy = right/prediction.shape[0]

        print("Accuracy of the test set: ",accuracy*100, "%")

obj = SpamClassifier()

# To check the accuracy of the test set
# obj.checkAccuracy()

obj.saveModel()