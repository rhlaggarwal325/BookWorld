from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

class BookSearch(forms.Form):
    genres = (
        ('Fantasy','Fantasy'),
        ('Science Fiction','Science Fiction'),
        ('Action','Action'),
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Horror','Horror'),
        ('Romance','Romance'),
        ('History','History'),
        ('Literary','Literary'),
        ('Biography', 'Biography')
    )
    languages = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Arabic', 'Arabic'),
        ('French', 'French'),
        ('Persian', 'Persian'),
        ('Sanskrit', 'Sanskrit')
    )
    genre = forms.MultipleChoiceField(choices=genres, widget=forms.CheckboxSelectMultiple, required=False)
    language = forms.MultipleChoiceField(choices=languages,widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        fields = ('genre','language')