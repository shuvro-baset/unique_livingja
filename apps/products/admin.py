from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ['name', 'brand', 'sku', 'price', 'main_category', 'sub_category', 'sup_category', 'add_category',
                    'is_featured', ]
    search_fields = ["name", 'brand', 'sku', ]
    list_editable = ['price', 'main_category', ]


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ['name']
    search_fields = ["name"]


class SubCategoryResource(resources.ModelResource):
    class Meta:
        model = SubCategory


class SubCategoryAdmin(ImportExportModelAdmin):
    resource_class = SubCategoryResource
    list_display = ['name']
    search_fields = ["name"]


class SupCategoryResource(resources.ModelResource):
    class Meta:
        model = SupCategory


class SupCategoryAdmin(ImportExportModelAdmin):
    resource_class = SupCategoryResource
    list_display = ['name']
    search_fields = ["name"]


class AddCategoryResource(resources.ModelResource):
    class Meta:
        model = AddCategory


class AddCategoryAdmin(ImportExportModelAdmin):
    resource_class = AddCategoryResource
    list_display = ['name']
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)
admin.site.register(HomeSlider)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(SupCategory, SupCategoryAdmin)
admin.site.register(AddCategory, AddCategoryAdmin)
