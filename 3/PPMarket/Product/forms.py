from django import forms
from .models import Product, ProductCategory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all())
    min_price = forms.FloatField(label='Min price')
    max_price = forms.FloatField(label='Max price')