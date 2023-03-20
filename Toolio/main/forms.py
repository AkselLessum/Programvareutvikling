from django import forms
from django.forms import widgets

from .models import ad

# Define the available ad types.
AD_TYPES = [
    ("normalAd", "Annonse"),
    ("requestAd", "Ønskes leid")
]

# Define the available categories.
options = [
    ("Annet", "Annet"),
    ("Snekring og tømrerarbeid", "Snekring og tømrerarbeid"),
    ("Maling og overflatebehandling", "Maling og overflatebehandling"),
    ("Hagearbeid", "Hagearbeid"),   
    ("Rørleggerarbeid", "Rørleggerarbeid"),
    ("Elektrikerarbeid", "Elektrikerarbeid"),
    ("Bilreperasjon", "Bilrepereasjon"),
    ("Møbelmontering", "Møbelmontering"),
    ("Gulvlegging", "Gulvlegging"),
    ("Rengjøring", "Rengjøring")
]

# Define a custom widget for the date input field.
class DateInput(forms.DateInput):
    input_type = "date"

# Define a form for creating an ad.
class createAdForm(forms.ModelForm):
    type = forms.ChoiceField(choices=AD_TYPES, widget=forms.RadioSelect(attrs={"onchange":"changeForm(this.id)"}))
    title = forms.CharField(label="Tittel", max_length=100, widget=forms.TextInput(attrs={"placeholder": "Toolio"}), label_suffix='')
    category = forms.ChoiceField(label = "Kategori", choices = options)
    date = forms.DateField(widget=DateInput(), label="Produktet er ledig frem til")
    price = forms.IntegerField(label="Pris", widget=widgets.NumberInput(attrs={"style":"border-radius: 0 !important;"}))
    description = forms.CharField(label="Beskrivelse", widget=forms.Textarea(attrs={"placeholder": "Beskriv verktøyet", "rows": 3}), max_length=500, label_suffix='')
    image = forms.FileField(label="Bilde av redskapet", required=False, label_suffix='')

    class Meta:
        model = ad
        fields = ['type', 'title', 'category', 'date', 'price', 'description', 'image']

# Define a form for editing an ad.
class editAdForm(forms.ModelForm):
    # Define the form fields.
    title = forms.CharField(label="Tittel", max_length=100, label_suffix='')
    category = forms.ChoiceField(label = "Katerogi", choices = options)
    date = forms.DateField(widget=DateInput(), label="Produktet er ledig frem til",label_suffix='')
    price = forms.IntegerField(label="Pris", widget=widgets.NumberInput(attrs={"style":"border-radius: 0 !important;"}), label_suffix='')
    description = forms.CharField(label="Beskrivelse",widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}), max_length=500, label_suffix='')
    image = forms.FileField(label="Bilde av redskapet", required=False, label_suffix='')
    isRented = forms.BooleanField(widget=forms.CheckboxInput, label="Utleid", required=False, label_suffix='')

    class Meta:
        model = ad
        fields = ('title', 'category', 'date', 'price','description',  'image', 'isRented')

# Define a form for editing a "ønsket leid" ad.
class editAdFormWanted(forms.ModelForm):
    # Define the form fields.
    title = forms.CharField(label="Tittel", max_length=100, label_suffix='')
    category = forms.ChoiceField(label = "Katerogi", choices = options)
    date = forms.DateField(widget=DateInput(), label="Ønsker å leie til",label_suffix='')
    price = forms.IntegerField(label="Budsjett", widget=widgets.NumberInput(attrs={"style":"border-radius: 0 !important;"}), label_suffix='')
    description = forms.CharField(label="Beskrivelse",widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}), max_length=500, label_suffix='')

    class Meta:
        model = ad
        fields = ('title', 'category', 'date', 'price','description')