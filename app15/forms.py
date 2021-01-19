from django.forms import ModelForm
from .models import Person


class PersonEntryForm(ModelForm):
    class Meta:
        model = Person
        fields = ['pid', 'full_name', 'contact_address']
    