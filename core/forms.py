from core import models
from django import forms


class IdeaForm(forms.ModelForm):       

    class Meta:
        model = models.Idea
        fields = ["title", "slug", "problem", "solution",
                  "is_publish", "address", "phone", "website"]