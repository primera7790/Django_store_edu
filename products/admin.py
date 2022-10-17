from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'category')
    search_fields = ('name',)


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0