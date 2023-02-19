from django import forms
from .models import ad

AD_TYPES = [
    ("normalAd", "Annonse"),
    ("requestAd", "Ønskes leid")
]

class DateInput(forms.DateInput):
    input_type = "date"

class createAdForm(forms.Form):
    # Type's widget forms.RadioSelect has the attribute onchange, which gives the type-inputs this as a function call
    type = forms.ChoiceField(choices=AD_TYPES, widget=forms.RadioSelect(attrs={"onchange":"changeForm(this.id)"}))
    title = forms.CharField(label="Tittel", max_length=100)
    date = forms.DateField(widget=DateInput(), label="Dato produktet er ledig til:")
    price = forms.IntegerField(label="Pris")
    description = forms.CharField(label="Beskrivelse", widget=forms.Textarea, max_length=500)
    image = forms.FileField(label="Bilde av redskapet", required=False)

    class Meta:
        model = ad
        fields = ('type', 'title', 'date', 'price', 'description', 'image')


class editAdForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 40})
    )

    class Meta:
        model = ad
        fields = ('title', 'description', 'price', 'image')



class editAdFormWanted(forms.ModelForm): # Edit "ønsket leid", no image in fields
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 40})
    )

    class Meta:
        model = ad
        fields = ('title', 'description', 'price')