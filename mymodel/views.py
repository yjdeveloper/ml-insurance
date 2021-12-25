from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd

# Load the model
model = pickle.load(open('mymodel/pkl/insuranceprediction.sav','rb'))

# Create your views here.
def index(request):
    return render(request, 'mymodel/index.html')

def predict(request):
    # Get user data

    # Checking 
    if request.method == "POST":
        age = int(request.POST.get('age'))
        sex = request.POST.get('gender')
        bmi = float(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = request.POST.get('smoker')
        region = request.POST.get('region')

        # Predict
        list1 = [age, sex, bmi, children, smoker, region]
        print(list1)
        data = pd.DataFrame([list1], columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

        pred = model.predict(data)
        expenses  = pred[0]
        # print(data)
        # print(expenses)
        context = {
            'data' : list1,
            'pred' : expenses
        }

        return render(request, 'mymodel/index.html', context)
