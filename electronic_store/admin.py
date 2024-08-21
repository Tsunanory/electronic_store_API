from django.contrib import admin
from .models import NetworkNode, Product


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'city', 'debt', 'supplier')
    list_filter = ('city', 'country')
    search_fields = ('name',)

    def clear_debt(self, queryset):
        queryset.update(debt=0)
    clear_debt.short_description = "Clear debt for selected network nodes"

    actions = [clear_debt]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('supplier')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
    search_fields = ('name', 'model')
