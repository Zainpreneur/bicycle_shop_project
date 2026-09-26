from django.contrib import admin

from .models import Customer, Bicycle, RepairCategory, RepairService, WorkOrder, WorkOrderItem, ProductCategory, Product, Sale, SaleItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['created_at']


@admin.register(Bicycle)
class BicycleAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer', 'status', 'frame_type']
    search_fields = ['brand', 'model', 'frame_number', 'customer__name']
    list_filter = ['status', 'frame_type']
    raw_id_fields = ['customer']

    def name(self, obj):
        return f"{obj.brand} {obj.model}"
    name.short_description = 'Brand/Model'


@admin.register(RepairCategory)
class RepairCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(RepairService)
class RepairServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_price', 'estimated_time', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'category__name']


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'bicycle', 'customer', 'status', 'total_price', 'created_at']
    search_fields = ['bicycle__frame_number', 'customer__name', 'status']
    list_filter = ['status', 'created_at']
    raw_id_fields = ['customer', 'bicycle']


@admin.register(WorkOrderItem)
class WorkOrderItemAdmin(admin.ModelAdmin):
    list_display = ['work_order', 'repair_service', 'quantity', 'price']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'sku', 'retail_price', 'quantity_in_stock', 'is_active']
    search_fields = ['name', 'sku', 'brand', 'category__name']
    list_filter = ['condition', 'is_active', 'gender_target']
    raw_id_fields = ['category']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total', 'payment_method', 'sale_date']
    list_filter = ['payment_method', 'sale_date']
    search_fields = ['customer__name', 'payment_method']
    raw_id_fields = ['customer']


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ['sale', 'product', 'quantity', 'price', 'line_total']
    search_fields = ['sale__id', 'product__name']
