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


        labels = {
            'name': 'Название',
            'description': 'Описание',
            'image': 'Изображение',
            'category': 'Категория',
            'price': 'Цена (₽)',
        }

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Описание товара'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Цена в рублях'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })


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

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError(f'Цена не может быть меньше 0 "{price}"!')
        return price



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)