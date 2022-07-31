
from django.forms import ModelForm
from .models import Supplier, User
from django import forms

class CountryModelForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['country']

"""
Remember Generating EID,BID,INO should follow ID +CHAR+ID+CHAR, because of the possibility of generating the user id future
"""