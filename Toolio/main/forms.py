from django import forms
from .models import Ad

AD_TYPES = [
    ("normalAd", "Annonse"),
    ("requestAd", "Ønskes leid")
]

class DateInput(forms.DateInput):
    input_type = "date"

class createAdForm(forms.ModelForm):
    type = forms.ChoiceField(choices=AD_TYPES, widget=forms.RadioSelect)
    title = forms.CharField(label="Tittel", max_length=100)
    date = forms.DateField(widget=DateInput(), label="Velg dato produktet er ledig frem til:")
    price = forms.IntegerField(label="Pris")
    description = forms.CharField(label="Beskrivelse", widget=forms.Textarea, max_length=500)
    image = forms.FileField(label="Bilde av redskapet")

    class Meta:
        model = Ad
        fields = ('type', 'title', 'date', 'price', 'description', 'image')


class editAdForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 40})
    )

    class Meta:
        model = Ad
        fields = ('title', 'description', 'price', 'image')


class editAdFormWanted(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 40})
    )

    class Meta:
        model = Ad
        fields = ('title', 'description', 'price')

