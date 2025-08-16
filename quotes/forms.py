from django import forms
from .models import Quote, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'born', 'bio']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'tags']
