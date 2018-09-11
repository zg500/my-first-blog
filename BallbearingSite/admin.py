
from django.contrib import admin
from BallbearingSite.models import UserProfileInfo,Posts,ExpireDays,ContactUs,SellerDesktop,Parts,Cars

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# class ImportAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/BallbearingSite/Posts/change_list.html'

admin.site.register(SellerDesktop)

class CarsAdmin(admin.ModelAdmin):
    list_display=['carname','confirm']
    list_editable=["confirm",]
admin.site.register(Cars,CarsAdmin)


class PostsAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(PostsAdmin, self).get_changeform_initial_data(request)
        get_data['owner'] = request.user
        return get_data

admin.site.register(Posts,PostsAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display=['title','content','cellphone','email','createDateTime']
    readonly_fields = ('title','content','cellphone','email','createDateTime')
    def has_add_permission(self, request): # to remove add link in admin pannel
        return False
    class Meta:
        model= ContactUs
    class Media:
        css = {'all': ('css/style.css',)}
admin.site.register(ContactUs,ContactUsAdmin)


class UserProfileInfoModelAdmin(admin.ModelAdmin):
    list_display=["user","companyname","state"]
    # readonly_fields = ('user','companyname','state','city','address','tel','cellphone')
    list_filter=[ "state"]
    search_fields=["companyname","state"]
    # readonly_fields = ('user',)
    class Meta:
        model= UserProfileInfo
    class Media:
        css = {'all': ('css/style.css',)}
admin.site.register(UserProfileInfo,UserProfileInfoModelAdmin)


class ExpireDaysModelAdmin(admin.ModelAdmin):
     def has_add_permission(self, request): # to remove add link in admin pannel
         return False
     def get_actions(self, request):
        actions = super(ExpireDaysModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
            return actions
     class Media:
        css = {'all': ('css/style.css',)}     # css to make addanother button invisible for expiredays
admin.site.register(ExpireDays,ExpireDaysModelAdmin)



class PartsAdmin(admin.ModelAdmin):
    # readonly_fields = ("user","car","partname","pic","description","price","date")
    list_display=["id","user","car","partname","pic","description","price","date","confirm",'parts_cars']
    list_editable=["confirm",]
    # readonly_fields = ('date',)
    # list_filter=["user","name","date","confirm","pasvand"]
    # search_fields=["name","brand","number","pasvand","comment","price"]
    list_per_page = 50

    def parts_cars(self, instance): #For showing a field which is in other table and connected by foriegnkey
       return instance.car.confirm

    class Meta:
        model= Parts
admin.site.register(Parts,PartsAdmin)

# @admin.register(Stocks)
# class StocksAdmin(ImportExportModelAdmin):
#     list_display=["name","brand","number","pasvand","comment","price","confirm"]
#     list_editable=["confirm",]
#     readonly_fields = ('date',)
#     list_per_page = 50
#     pass
