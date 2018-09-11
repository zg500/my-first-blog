# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from BallbearingSite.models import UserProfileInfo,ContactUs,Parts
# from django.core import validators
# from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from import_export import resources
from ckeditor.widgets import CKEditorWidget
from dal import autocomplete

from ajax_select.fields import AutoCompleteSelectMultipleField



class UploadFileForm(forms.Form):
    docfile = forms.FileField(label=_("Enter your filled downloaded file"))

class ExportSpec(resources.ModelResource):
    class Meta:
        model = Parts

# class PartsForm(forms.ModelForm):
#         class Meta():
#             model=Parts
#             fields=('partname','pic','description','price')

class StocksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StocksForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style']= 'width:60%'
    class Meta():
        model=Parts
        fields=('car','partname','description','pic','price')
        help_texts = {
            'price' : ('تومان'),
            }
        widgets = {
            'car': autocomplete.Select2(url='BallbearingSite:stock_autocomplete'),
        }

        def __init__(self, *args, **kwargs):
          super(StocksForm, self).__init__(*args, **kwargs)
          for visible in self.visible_fields():
             visible.field.widget.attrs['class'] = 'form-control'

class UserForm(forms.ModelForm):

    username=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%', 'white-space':'nowrap'}),label=_('username'))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style': 'width:60%'}),label=_('password'))
    password_repeat=forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control','style': 'width:60%'}),label=_('password_repeat'))
    email=forms.EmailField( widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%', 'white-space':'nowrap'}),label=_('email'))
    first_name=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%', 'white-space':'nowrap'}),label=_('firstname'))
    last_name=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%', 'white-space':'nowrap'}),label=_('lastname'))
    error_css_class = 'error'
    class Meta():
        model=User
        fields=('username','password','password_repeat','email','first_name','last_name')
        help_texts = {
            'username': None,
        }
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u"این پست الکترونیکی قبلا ثبت گردیده است")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(u"نام کاربری قبلا ثبت شده است!")
        return username

    def clean_password_repeat(self):
        cleaned_data = super(UserForm, self).clean()
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if password != password_repeat:
                raise forms.ValidationError(u"رمزعبور و تکرار آن یکسان نیستند")
        return self.cleaned_data



# class':'form-control is a bootstrap class for making textboxes responsive, if we didnt need it also wouldnt need to write line 2-7 bellow
class UserProfileInfoForm(forms.ModelForm):
    # CHOICES = (('0','خریدار'),
    #                    ('1','فروشنده'),
    #                    ('2','هردومورد'))
    # is_seller = forms.CharField(widget=forms.Select(choices=CHOICES),label=_('title'))
    companyname=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%', 'white-space':'nowrap'}),label=_('companyname'))
    cellphone = forms.CharField(  widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%'}),label=_('cellphone'))
    tel = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%'}),label=_('tel'))
    state=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%'}),label=_('state'))
    city=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:60%'}),label=_('city'))
    address=forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control' ,'style': 'width:100%'}),label=_('address'))
    error_css_class = 'error'

    class Meta():
        model=UserProfileInfo
        fields=('companyname','tel','cellphone','state','city','address')

    # def clean(self):
    #     cleaned_data = super(UserProfileInfoForm, self).clean()
    #     seller = cleaned_data.get("is_seller")
    #     companyname = self.cleaned_data.get('companyname')
    #     tel = self.cleaned_data.get('tel')
    #     address = self.cleaned_data.get('address')
    #
    #     co=ad=te=False
    #     if  seller!="0" and companyname=="":
    #         co=True
    #     if  seller!="0" and address=="":
    #         ad=True
    #     if  seller!="0" and tel=="":
    #         te=True
    #     if co or ad or te :
    #         raise forms.ValidationError({"is_seller":["برای فروشنده ، تکمیل گزینه های نام شرکت ، آدرس و شماره تلفن الزامیست"]})
    #     return cleaned_data

class SendEmailForm(forms.Form):
    subject=forms.CharField(label=_("subject"))
    message=forms.CharField(widget=forms.Textarea,label=_("message"))


class ContactUsForm(forms.ModelForm):
    class Meta():
        model=ContactUs
        fields=('title','cellphone','email','content')
