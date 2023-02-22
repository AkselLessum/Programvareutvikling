from django import forms
from django.forms import widgets

from .models import ad

AD_TYPES = [
    ("normalAd", "Annonse"),
    ("requestAd", "Ønskes leid")
]

class DateInput(forms.DateInput):
    input_type = "date"

class createAdForm(forms.ModelForm):
    #error_css_class = 'error-field'
    #required_css_class = 'required-field'
    
    # Type's widget forms.RadioSelect has the attribute onchange, which gives the type-inputs this as a function call
    type = forms.ChoiceField(choices=AD_TYPES, widget=forms.RadioSelect(attrs={"onchange":"changeForm(this.id)"}))
    title = forms.CharField(label="Tittel", max_length=100, widget=forms.TextInput(attrs={"placeholder": "Toolio"}))
    date = forms.DateField(widget=DateInput(), label="Produktet er ledig frem til")
    price = forms.IntegerField(label="Pris", widget=widgets.NumberInput)
    description = forms.CharField(label="Beskrivelse", widget=forms.Textarea(attrs={"placeholder": "Beskriv verktøyet", "rows": 3}), max_length=500)
    image = forms.FileField(label="Bilde av redskapet", required=False)

    class Meta:
        model = ad
        fields = ('type', 'title', 'date', 'price', 'description', 'image')


class editAdForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}))
    isRented = forms.BooleanField(widget=forms.CheckboxInput, label="Utleid", required=False)

    class Meta:
        model = ad
        fields = ('title', 'description', 'price', 'image', 'isRented')



class editAdFormWanted(forms.ModelForm): # Edit "ønsket leid", no image in fields
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 40})
    )

    class Meta:
        model = ad
        fields = ('title', 'description', 'price')