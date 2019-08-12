'''
Creating Ham Dataframe from ham folder
'''

import os
import pandas as pd

for root, dirs, files in os.walk('./ham', topdown=True):
    content = []
    for name in files:
        newPath = os.path.join(root, name)
        with open(newPath,'r',encoding = "latin1") as file:
            contentOfFile = file.read()
            content.append(contentOfFile)

data = {'Message': content, 'Class': 'ham'}
df = pd.DataFrame(data)
df.to_csv('ham.csv',index = False)
