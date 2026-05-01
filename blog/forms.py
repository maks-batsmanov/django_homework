from django import forms
from .models import BlogEntry

class AddEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['heading', 'content', 'preview', 'publication_attribute']

        widgets = {
            'heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Текст статьи'}),
            'preview': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'publication_attribute': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'heading': 'Заголовок',
            'content': 'Статья',
            'preview': 'Изображение',
            'publication_attribute': 'Опубликовать'
        }
