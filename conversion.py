'''
Creating Dataset from folder
'''

import os
import pandas as pd

class Conversion:
    
    def convertFilesIntoCSV(self, name_dataset):
        for root, dirs, files in os.walk('./' + name_dataset , topdown=True):
            content = []
            for name in files:
                newPath = os.path.join(root, name)
                with open(newPath,'r',encoding = "latin1") as file:
                    contentOfFile = file.read()
                    content.append(contentOfFile)
        data = {'Message': content, 'Class': name_dataset}
        # Converting the dictionary into DataFrame
        df = pd.DataFrame(data)
        # index = False otherwise, it will create an additional column of index.
        df.to_csv(name_dataset + '.csv',index = False)

