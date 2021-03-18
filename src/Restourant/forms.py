from django import forms
from .models import *


class SuggestionsForm(forms.ModelForm):

    class Meta:
        model = Suggestions
        fields = "__all__"

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user