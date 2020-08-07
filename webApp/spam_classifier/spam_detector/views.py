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
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        emailBody = request.POST['email_body']
        # emailBody = request.form['email_body']
        data = [emailBody]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        # return render(request ,'success.html',prediction=my_prediction)
        # return render(request, 'fail.html')
        print(my_prediction[0])
        print(type(my_prediction))
        return render(request, 'success.html', {"prediction": my_prediction[0]})
    else:
        return render(request, 'fail.html')
    # emailBody = request.POST.get("email_body")
    # print(emailBody)
    # data = [Email_body]
    # print(data)
    # email_series = pd.Series(emailBody)
    # vect = cv.transform(email_series)
    # my_prediction = classifier.predict(vect)
    # return render(request, 'success.html', prediction=my_prediction)
    # return render(request, 'success.html', {"prediction": my_prediction})

    # return HttpResponse('<h1>Page was found</h1>')