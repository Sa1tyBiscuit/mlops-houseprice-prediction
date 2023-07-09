from django.shortcuts import render
from django.db import models
import numpy as np
import pickle

# our home page view


class Result(models.Model):
    result = models.CharField(max_length=100)


def home(request):
    return render(request, 'index.html')

# /Users/bingxian/Desktop/resale_flats_price_prediction/resale_flat_web/resale_flat_prediction_web/
# custom method for generating predictions


def getPredictions(flat_size):

    model = pickle.load(open(
        "resale_flat_prediction_web/model.sav", "rb"))
    prediction = model.predict([[flat_size]])[0]

    if prediction > 0:

        result = f"{np.exp(prediction):.2f} dollars"
        return result
    else:
        return "negative prices, invalid value"


# our result page view
def result(request):
    size = int(request.GET['flat_size'])

    result = getPredictions(size)
    result_obj = Result(result=result)
    result_obj.save()

    return render(request, 'index.html', {'result': result})
