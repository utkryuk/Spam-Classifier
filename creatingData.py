import numpy as np
import pandas as pd
from conversion import Conversion


obj = Conversion()

obj.convertFilesIntoCSV('ham')
obj.convertFilesIntoCSV('spam')

ham = pd.read_csv('ham.csv')
spam = pd.read_csv('spam.csv')


Class =[]
Content = []
for i in range(ham.shape[0]):
    Class.append('ham')
    Content.append(ham['Message'][i])
    
for i in range(spam.shape[0]):
    Class.append('spam')
    Content.append(spam['Message'][i])


data = {'Message': Content, 'Class': Class}
data = pd.DataFrame(data)

data = data.iloc[np.random.permutation(len(data))] #mixing spam and ham messages

#splitting into train and test data
from sklearn.model_selection import train_test_split
train, test = train_test_split(data,test_size= 0.2,random_state =42)


prediction_ans = test['Class']
prediction_ans = {'Class': prediction_ans}
prediction_ans = pd.DataFrame(prediction_ans)

del test['Class']

#creating train, test
train.to_csv('train.csv',index = False)
test.to_csv('test.csv',index = False)
prediction_ans.to_csv('prediction_ans.csv',index = False)
