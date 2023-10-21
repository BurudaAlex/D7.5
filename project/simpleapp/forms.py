from django import forms
from .models import Product
from django.core.exceptions import ValidationError
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'quantity',
            'category',
            'price',
        ]
    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        if description is not None and len(description) < 20:
            raise ValidationError({
                "description": "記述は20字以下入力が出来ません。"
            })

        name = cleaned_data.get("name")
        if name == description:
            raise ValidationError(
                "説明は名前と同一であってはなりません."
            )

        return cleaned_data