import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import pickle

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

test = pd.read_csv('test.csv')


prediction = vectoriser.transform(test['Message'])

'''
################################################################
print(prediction.shape)
print(test['Message'].shape)
# print(vectoriser.transform(test['Message'][0]))
# print(prediction)
print(type(test['Message']))

abc = test['Message'][0]
abc_series = pd.Series(abc)
print(abc_series.shape)
# print(prediction)
print(vectoriser.transform(abc_series))
print(type(vectoriser.transform(abc_series)))

################################################################
'''

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

print(accuracy)