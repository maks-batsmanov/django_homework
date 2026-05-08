from django import forms
from .models import Product
from django.core.exceptions import ValidationError

forbidden_words = [
        'казино',
        'криптовалюта',
        'крипта',
        'биржа',
        'дешево',
        'бесплатно',
        'обман',
        'полиция',
        'радар'
    ]

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание товара'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена в рублях'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Название',
            'description': 'Описание',
            'image': 'Изображение',
            'category': 'Категория',
            'price': 'Цена (₽)',
        }


    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError(f'Имя содержит запрещенное слово "{name}"!')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError(f'Описание содержит запрещенное слово "{description}"!')
        return description


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)