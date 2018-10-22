from django import forms

class PortfolioForm(forms.Form):
    password = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'id':'password-input', 'style':'border-radius:8px;line-height:26px;font-size:18px;'}),
        required=True,
        max_length=50
    )

class CalenderForm(forms.Form):
    pk = forms.IntegerField(
        label='主キー',
        widget=forms.NumberInput(attrs={'type':'hidden', 'id':'promo-id'}),
    )
    
    startDate = forms.DateField(
        label='開始日',
        widget=forms.DateInput(attrs={'type':'date', 'id':'promo-start'}),
        required=True,
    )

    endDate = forms.DateField(
        label='終了日',
        widget=forms.DateInput(attrs={'type':'date', 'id':'promo-end'}),
        required=True
    )

    content = forms.CharField(
        label='内容',
        widget=forms.TextInput(attrs={'id':'promo-content'}),
        required=True,
        max_length=50
    )

