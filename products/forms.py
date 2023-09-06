from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image_1 = forms.ImageField(label='Image', required=False,
                               widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_list = [(c.id, str(c)) for c in categories]

        self.fields['category'].choices = category_list
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
