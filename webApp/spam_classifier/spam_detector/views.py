from django.shortcuts import render
import os
import pickle
import pandas as pd
from django.views.generic import TemplateView


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ML_MODEL_DIR = os.path.join(BASE_DIR, 'ml_models')


cv = pickle.load(open(os.path.join(ML_MODEL_DIR, 'count-transform.pkl'),'rb'))

classifier = pickle.load(open(os.path.join(ML_MODEL_DIR, 'spam-or-ham-classifier.pkl'),'rb'))

def indexPage(request):
    return render(request, 'classifier.html')

def predict(request):
    if request.method == 'POST':
        emailBody = request.POST['email_body']
        data = [emailBody]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        return render(request, 'result.html', {"prediction": my_prediction[0]})
    else:
        return render(request, 'fail.html')
