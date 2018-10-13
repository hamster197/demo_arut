from .models import zvonok
from django import forms
from django.core.exceptions import ValidationError


class zvn_form(forms.ModelForm):
    class Meta:
        model = zvonok
        fields = ('tel','client_name', 'raion', 'subj', 'cena', 'client_name', 'prim')

    def clean(self):
        cleaned_data = super(zvn_form, self).clean()
        if len(str(cleaned_data['tel']))!=10:
                raise ValidationError('Неверный номер телефона!' , code='invalid')

class zvn_form_edit(forms.Form):
    coment = forms.CharField(label='Коментарий:')
    date_pr_call = forms.DateTimeField(label='Перезвонить в:')
    #class Meta:
    #    model = zvonok
    #    fields = ('coment','prezvonit',)

class new_zvn_form(forms.ModelForm):#(forms.Form):
    class Meta:
        fields = ('tel',)
        model = zvonok
    #tel = forms.IntegerField(label='Номер телефона1', help_text='9881451100')
    #def clean(self):
    #    cleaned_data = super(new_zvn_form, self).clean()
    #    if len(str(cleaned_data['tel']))!=10:
    #            raise ValidationError('Неверный номер телефона!' , code='invalid')