from django import forms


class AuctionListingForm(forms.Form):
    title = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'title:'
        }
        )
    )
    description = forms.CharField(
        label='Description',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Describe the product',
            'rows': '3'
        }
        )
    )


    starting_bid = forms.DecimalField(
        label='Starting Bid',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Starting bid',
            'min': '0.01',
            'max': '99999999999.99',
            'step': '0.01'
        }
        )
    )
    category = forms.CharField(
        label='Category',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'autocomplete': 'on',
            'placeholder': 'Category (optional)'
        }
        )
    )
    image_url = forms.URLField(
        label='Image URL',
        required=False,
        initial='https://us.123rf.com/450wm/jovanas/jovanas1609/jovanas160900216/62250462-no-horse-traffic-sign.jpg?ver=6',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'Image URL (optional)',
        }
        )
    )
