# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Cars(models.Model):
    checking= ((_('pending'),_('pending')),
               (_('reject'),_('reject')),
               (_('approved'),_('approved')),
               (_('expired'),_('expired')),                )
    carname=models.CharField(max_length=128,verbose_name=_('carname'))
    confirm=models.CharField(choices=checking,max_length=12,verbose_name=_('confirmation'), default=_('pending'))
    def __str__(self):
        return str(self.carname)
    class Meta:
        verbose_name=_('car')
        verbose_name_plural=_('cars')
        ordering = ('carname',) #For sorting alphabetically

class Parts(models.Model):
    user=models.ForeignKey(User, null=True)
    car=models.ForeignKey(Cars, null=True,verbose_name=_('car') )
    partname=models.CharField(max_length=128,verbose_name=_('partname'))
    description=models.CharField(blank=True,null=True,max_length=264,verbose_name=_('description'))
    pic=models.ImageField(blank=True,null=True,verbose_name=_('pic'),upload_to = 'stocks', default = 'stocks/nopic.jpg')
    price=models.PositiveIntegerField(blank=True,null=True,verbose_name=_('price'))
    date=models.DateTimeField(auto_now_add = True,verbose_name=_('date'))
    checking= ((_('pending'),_('pending')),
           (_('reject'),_('reject')),
           (_('approved'),_('approved')),
           (_('expired'),_('expired')),
                )
    confirm=models.CharField(choices=checking,max_length=12,verbose_name=_('confirmation'), default=_('pending'))
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name=_('Part')
        verbose_name_plural=_('Parts')
    def get_absolute_url(self):
        return reverse('BallbearingSite:detailadvertisement' ,kwargs={'id':self.id})

# class StocksName(models.Model):
#     name=models.CharField(max_length=128,verbose_name=_('stockname'))
#     def __str__(self):
#         return str(self.name)
#     class Meta:
#         verbose_name=_('StocksName')
#         verbose_name_plural=_('StocksNames')

# class Stocks(models.Model):
#     user=models.ForeignKey(User, null=True,related_name='stockdetails')
#     name=models.CharField(max_length=128,verbose_name=_('stockname'))
#     # pic=models.ImageField(blank=True,null=True,verbose_name=_('pic'))
#     # number=models.CharField(blank=True,null=True,max_length=64,verbose_name=_('number'))
#     # pasvand=models.CharField(blank=True,null=True,max_length=12,verbose_name=_('pasvand'))
#     # brand=models.CharField(max_length=64, validators=[
#         # RegexValidator(regex='^[A-Z]*$',message=_(u'brand must be in Capital letter'),)]
#         # ,verbose_name=_('brand'))
#     comment=models.CharField(blank=True,null=True,max_length=264,verbose_name=_('comment'))
#     price=models.PositiveIntegerField(blank=True,null=True,verbose_name=_('price'))
#     date=models.DateTimeField(auto_now_add = True,verbose_name=_('date'))
#     # confirmation=models.NullBooleanField(blank=True,null=True,verbose_name=_('confirmation'))
#     checking= ((_('pending'),_('pending')),
#            (_('reject'),_('reject')),
#            (_('approved'),_('approved')),
#            (_('expired'),_('expired')),
#                 )
#     confirm=models.CharField(choices=checking,max_length=12,verbose_name=_('confirmation'), default=_('pending'))
#     def __str__(self):
#         return str(self.id)
#     class Meta:
#         verbose_name=_('Stock')
#         verbose_name_plural=_('Stocks')
#     def get_absolute_url(self):
#         return reverse('BallbearingSite:mystocks' )


class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,related_name='profile')
    # firstname=models.CharField(max_length=128,verbose_name=_('firstname'))
    # lastname=models.CharField(max_length=128,verbose_name=_('lastname'))
    farsi_regex = RegexValidator(regex='^[0-9 آ-ی ء چ ._,/-]*$', message=_(u"Enter in Farsi letters"))
    companyname=models.CharField(blank=True,null=True,validators=[farsi_regex],max_length=128,verbose_name=_('companyname'))
    phone_regex = RegexValidator(regex=r'^\d{11,11}$', message=_(u"Phone number must be 11 digit."))
    cellphone = models.CharField(validators=[phone_regex], max_length=17,verbose_name=_('cellphone'))
    tel = models.CharField(blank=True,null=True,validators=[phone_regex], max_length=17,verbose_name=_('tel'))
    state=models.CharField(validators=[farsi_regex],max_length=128,verbose_name=_('state'))
    city=models.CharField(validators=[farsi_regex],max_length=128,verbose_name=_('city'))
    address=models.CharField(blank=True,null=True,validators=[farsi_regex],max_length=264,verbose_name=_('address'))
    # is_seller=models.CharField( max_length=2,verbose_name=_('sell'))
    def __str__ (self):
        return self.user.username

    class Meta:
        verbose_name=_('UserProfileInfo')
        verbose_name_plural=_('UserProfileInfos')


class Posts(models.Model):
    # owner=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_('Owner'))
    owner=models.CharField(blank=True,null=True,max_length=64,verbose_name=_('Owner'))
    title=models.CharField(_('title'),max_length=70)
    content=RichTextUploadingField(_('content'),config_name='default')
    updateDateTime=models.DateTimeField(_('create date'),auto_now_add=True,auto_now=False)
    createDateTime=models.DateTimeField(_('update date'),auto_now_add=False,auto_now=True)
    class Meta:
        verbose_name=_('Post')
        verbose_name_plural=_('Posts')
    def __str__ (self):
        return self.title
    def get_absolute_url(self):
        return reverse('BallbearingSite:detail' ,kwargs={'id':self.id})

class ContactUs(models.Model):
    title=models.CharField(_('title'),max_length=70)
    content=RichTextUploadingField(_('content'),config_name='default')
    phone_regex = RegexValidator(regex=r'^\d{11,11}$', message=_(u"Phone number must be 11 digit."))
    cellphone = models.CharField(validators=[phone_regex],blank=True,null=True, max_length=17,verbose_name=_('cellphone'))
    email=models.EmailField(max_length=264,verbose_name=_('email'))
    createDateTime=models.DateTimeField(_('update date'),auto_now_add=False,auto_now=True)
    class Meta:
        verbose_name=_('Message')
        verbose_name_plural=_('Messages')
    def __str__ (self):
        return self.title


class ExpireDays(models.Model):
    days=models.PositiveIntegerField(blank=True,null=True,verbose_name=_('expiredays'))
    class Meta:
        verbose_name=_('ExpireDay')
        verbose_name_plural=_('ExpireDays')
    def __str__ (self):
        return str(self.days)

class SellerDesktop(models.Model):
    seller=models.ForeignKey(User, related_name='seller', blank=True, null=True)
    buyer=models.ForeignKey(User, related_name='buyer', blank=True, null=True)
    stock=models.ForeignKey(Parts, related_name='stocktoseller', blank=True, null=True)
    date=models.DateTimeField(auto_now_add = True,verbose_name=_('date'), blank=True, null=True)

    def __str__(self):
        return str(self.stock.partname) + '-sell:' + str(self.seller) + '-buy:' + str(self.buyer)
    class Meta:
        verbose_name=_('SellerDesktop')
        verbose_name_plural=_('SellerDesktop')
