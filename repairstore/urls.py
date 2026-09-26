from django.urls import path
from . import views

app_name = 'repairstore'

urlpatterns = [
    # --- Home ---
    path('', views.IndexView.as_view(), name='index'),

    # --- Customer URLs ---
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/new/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    # --- Bicycle URLs ---
    path('bicycles/', views.BicycleListView.as_view(), name='bicycle_list'),
    path('bicycles/new/', views.BicycleCreateView.as_view(), name='bicycle_create'),
    path('bicycles/<int:pk>/edit/', views.BicycleUpdateView.as_view(), name='bicycle_edit'),
    path('bicycles/<int:pk>/delete/', views.BicycleDeleteView.as_view(), name='bicycle_delete'),

    # --- Repair Category URLs ---
    path('repair-categories/', views.RepairCategoryListView.as_view(), name='repair_category_list'),
    path('repair-categories/new/', views.RepairCategoryCreateView.as_view(), name='repair_category_create'),
    path('repair-categories/<int:pk>/edit/', views.RepairCategoryUpdateView.as_view(), name='repair_category_edit'),

    # --- Repair Service URLs ---
    path('repair-services/', views.RepairServiceListView.as_view(), name='repair_service_list'),
    path('repair-services/new/', views.RepairServiceCreateView.as_view(), name='repair_service_create'),
    path('repair-services/<int:pk>/edit/', views.RepairServiceUpdateView.as_view(), name='repair_service_edit'),

    # --- Work Order URLs ---
    path('work-orders/', views.WorkOrderListView.as_view(), name='work_order_list'),
    path('work-orders/new/', views.WorkOrderCreateView.as_view(), name='work_order_create'),
    path('work-orders/<int:pk>/', views.WorkOrderDetailView.as_view(), name='work_order_detail'),
    path('work-orders/<int:pk>/edit/', views.WorkOrderUpdateView.as_view(), name='work_order_edit'),
    path('work-orders/<int:pk>/delete/', views.WorkOrderDeleteView.as_view(), name='work_order_delete'),

    # --- Product Category URLs ---
    path('product-categories/', views.ProductCategoryListView.as_view(), name='product_category_list'),
    path('product-categories/new/', views.ProductCategoryCreateView.as_view(), name='product_category_create'),
    path('product-categories/<int:pk>/edit/', views.ProductCategoryUpdateView.as_view(), name='product_category_edit'),

    # --- Product URLs ---
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/new/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # --- Sale URLs ---
    path('sales/', views.SaleListView.as_view(), name='sale_list'),
    path('sales/new/', views.SaleCreateView.as_view(), name='sale_create'),
    path('sales/<int:pk>/edit/', views.SaleUpdateView.as_view(), name='sale_edit'),
    path('sales/<int:pk>/delete/', views.SaleDeleteView.as_view(), name='sale_delete'),

    # --- API JSON Endpoints ---
    path('api/dashboard-stats/', views.api_dashboard_stats, name='api_dashboard_stats'),
    path('api/customers/', views.api_customer_list, name='api_customer_list'),
    path('api/products/', views.api_product_list, name='api_product_list'),
    path('api/recent-sales/', views.api_recent_sales, name='api_recent_sales'),
]