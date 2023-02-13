from django import forms

class DateInput(forms.DateInput):
    input_type = "date"

class createAdForm(forms.Form):
    adTypes = [("normalAd", "Annonse"),
                ("requestAd", "Ønskes leid")]

    type = forms.ChoiceField(choices=adTypes, widget=forms.RadioSelect)
    title = forms.CharField(label="Tittel", max_length=100)
    date = forms.DateField(widget=DateInput(), label="Velg dato produktet er ledig frem til:")
    price = forms.IntegerField(label="Pris")
    description = forms.CharField(label="Beskrivelse", widget=forms.Textarea, max_length=500)
    adImage = forms.FileField(label="Bilde av redskapet")
