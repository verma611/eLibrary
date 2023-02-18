from django import forms
from .models import Book

class BookSearch(forms.Form):
    BookName = forms.CharField(max_length=10000)




#class BookSearch(forms.ModelForm):
#    class Meta:
#        model = Book
#        fields = ['text']
#        labels = {'text': ''}

