from django.contrib import admin
from .models import products,Category,Articles,Banners
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('position','title','slug')
    list_filter=(['status'])
    search_fields=("title",'slug')
    prepopulated_fields={'slug':('title',)}

class ProductsAdmin(admin.ModelAdmin):
    list_display=('title','slug','category_to_str',)
    list_filter=('status','publish')
    search_fields=("title",'description')
    prepopulated_fields={'slug':('title',)}
    ordering=['status','-publish']

    def category_to_str(self,obj):
        return "، ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = "دسته بندی"

class ArticlesAdmin(admin.ModelAdmin):
    list_display=('title','category_to_str',)
    list_filter=(['status'])
    search_fields=("title",'description')

    def category_to_str(self,obj):
        return "، ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = "دسته بندی"

class BannersAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=("title",)

    def category_to_str(self,obj):
        return "، ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = "دسته بندی"


admin.site.register(Category,CategoryAdmin)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(products,ProductsAdmin)
admin.site.register(Banners,BannersAdmin)