from django import forms
from .models import Customer, Bicycle, RepairCategory, RepairService, Product, Sale


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields = ['customer', 'frame_type', 'frame_size', 'brand', 'model', 'year', 'color', 'frame_number', 'acquired_date']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'frame_type': forms.Select(attrs={'class': 'form-control'}),
            'frame_size': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'frame_number': forms.TextInput(attrs={'class': 'form-control'}),
            'acquired_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class RepairCategoryForm(forms.ModelForm):
    class Meta:
        model = RepairCategory
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class RepairServiceForm(forms.ModelForm):
    class Meta:
        model = RepairService
        fields = ['category', 'name', 'description', 'estimated_time', 'base_price']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estimated_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'base_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'sku', 'description', 'condition', 'gender_target', 'brand', 'color', 'size', 'cost_price', 'retail_price', 'quantity_in_stock', 'reorder_level', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'gender_target': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'retail_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_in_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'reorder_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'payment_method', 'notes']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }