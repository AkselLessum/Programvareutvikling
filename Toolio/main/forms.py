from django import forms
from django.forms import widgets

from .models import ad

AD_TYPES = [
    ("normalAd", "Annonse"),
    ("requestAd", "Ønskes leid")
]
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

class DateInput(forms.DateInput):
    input_type = "date"

class createAdForm(forms.ModelForm):
    #error_css_class = 'error-field'
    #required_css_class = 'required-field'
    
    # Type's widget forms.RadioSelect has the attribute onchange, which gives the type-inputs this as a function call
    type = forms.ChoiceField(choices=AD_TYPES, widget=forms.RadioSelect(attrs={"onchange":"changeForm(this.id)"}))
    title = forms.CharField(label="Tittel", max_length=100, widget=forms.TextInput(attrs={"placeholder": "Toolio"}), label_suffix='')
    category = forms.ChoiceField(label = "Kategori", choices = options)
    date = forms.DateField(widget=DateInput(), label="Produktet er ledig frem til")
    price = forms.IntegerField(label="Pris", widget=widgets.NumberInput(attrs={"style":"border-radius: 0 !important;"}),min_value=0)
    description = forms.CharField(label="Beskrivelse", widget=forms.Textarea(attrs={"placeholder": "Beskriv verktøyet", "rows": 3}), max_length=500, label_suffix='')
    image = forms.FileField(label="Bilde av redskapet", required=False, label_suffix='')

    class Meta:
        model = ad
        fields = ['type', 'title', 'category', 'date', 'price', 'description', 'image']


class editAdForm(forms.ModelForm):
    title = forms.CharField(label="Tittel", max_length=100, label_suffix='')
    category = forms.ChoiceField(label = "Katerogi", choices = options)
    date = forms.DateField(widget=DateInput(), label="Produktet er ledig frem til",label_suffix='')
    price = forms.IntegerField(label="Pris", widget=widgets.NumberInput(attrs={"style":"border-radius: 0 !important;"}), label_suffix='', min_value=0)
    description = forms.CharField(label="Beskrivelse",widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}), max_length=500, label_suffix='')
    image = forms.FileField(label="Bilde av redskapet", required=False, label_suffix='')
    isRented = forms.BooleanField(widget=forms.CheckboxInput, label="Utleid", required=False, label_suffix='')

    class Meta:
        model = ad
        fields = ('title', 'category', 'date', 'price','description',  'image', 'isRented')



class editAdFormWanted(forms.ModelForm): # Edit "ønsket leid", no image in fields
    title = forms.CharField(label="Tittel", max_length=100, label_suffix='')
    category = forms.ChoiceField(label = "Katerogi", choices = options)
    date = forms.DateField(widget=DateInput(), label="Ønsker å leie til",label_suffix='')
    price = forms.IntegerField(label="Budsjett", widget=widgets.NumberInput(attrs={"style":"border-radius: 0 !important;"}), label_suffix='', min_value=0)
    description = forms.CharField(label="Beskrivelse",widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}), max_length=500, label_suffix='')

    class Meta:
        model = ad
        fields = ('title', 'category', 'date', 'price','description')