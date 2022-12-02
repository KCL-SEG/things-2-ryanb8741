"""Forms of the project."""

# Create your forms here.
from .models import Thing
from django import forms

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name", "description", "quantity"]
        widgets = {"description": forms.Textarea(), "quantity" : forms.NumberInput}
    
    def save(self):
        super().save(commit=False)
        thing = Thing.objects.create(
            name=self.cleaned_data.get("name"),
            description=self.cleaned_data.get("description"),
            quantity=self.cleaned_data.get("quantity"),
        )
        return thing