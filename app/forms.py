from .models import Profile
from django import forms
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio']