from django.shortcuts import render
from .forms import SpamForm
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

'''
Working Python Function
def predict(request):
    if request.method == 'POST':
        print(request.POST['email_body'])
        emailBody = request.POST['email_body']
        data = [emailBody]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        return render(request, 'result.html', {"prediction": my_prediction[0]})
    else:
        return render(request, 'fail.html')
'''

def predict(request):
    if request.method == 'POST':
        form = SpamForm(request.POST)
        if form.is_valid():
            print(request.POST['email_body'])
            emailBody = request.POST['email_body']
            data = [emailBody]
            vect = cv.transform(data).toarray()
            my_prediction = classifier.predict(vect)
            print(my_prediction)

        else:
            form = SpamForm()
        
        return render(request, 'predict.html', {"prediction": my_prediction[0]})

    else:
        return render(request, 'fail.html')
            

def formclass(request):
    if request.method == 'POST':
        form = SpamForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SpamForm()

    return render(request, 'resultFormClass.html', {'form': form})