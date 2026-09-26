from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, Count, Avg, F
from django.http import JsonResponse
from django.core import signing

from .models import (
    Customer, Bicycle, RepairCategory, RepairService,
    WorkOrder, WorkOrderItem, ProductCategory, Product, Sale, SaleItem
)
from .forms import CustomerForm, BicycleForm, RepairServiceForm, ProductForm, SaleForm


class IndexView(LoginRequiredMixin, View):
    """Home/dashboard page."""
    def get(self, request):
        customers = Customer.objects.count()
        bicycles = Bicycle.objects.count()
        work_orders = WorkOrder.objects.count()
        active_orders = WorkOrder.objects.filter(status='in_repair').count()
        products = Product.objects.filter(is_active=True).count()
        total_sales = Sale.objects.count()

        context = {
            'customers': customers,
            'bicycles': bicycles,
            'work_orders': work_orders,
            'active_orders': active_orders,
            'products': products,
            'total_sales': total_sales,
        }
        return render(request, 'repairstore/index.html', context)


# --- Customer Views ---

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'repairstore/customer_list.html'
    context_object_name = 'customers'
    ordering = ['name']


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'repairstore/customer_form.html'
    success_url = reverse_lazy('repairstore:customer_list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'repairstore/customer_form.html'
    success_url = reverse_lazy('repairstore:customer_list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'repairstore/customer_confirm_delete.html'
    success_url = reverse_lazy('repairstore:customer_list')


# --- Bicycle Views ---

class BicycleListView(LoginRequiredMixin, ListView):
    model = Bicycle
    template_name = 'repairstore/bicycle_list.html'
    context_object_name = 'bicycles'
    ordering = ['-created_at']


class BicycleCreateView(LoginRequiredMixin, CreateView):
    model = Bicycle
    form_class = BicycleForm
    template_name = 'repairstore/bicycle_form.html'
    success_url = reverse_lazy('repairstore:bicycle_list')


class BicycleUpdateView(LoginRequiredMixin, UpdateView):
    model = Bicycle
    form_class = BicycleForm
    template_name = 'repairstore/bicycle_form.html'
    success_url = reverse_lazy('repairstore:bicycle_list')


class BicycleDeleteView(LoginRequiredMixin, DeleteView):
    model = Bicycle
    template_name = 'repairstore/bicycle_confirm_delete.html'
    success_url = reverse_lazy('repairstore:bicycle_list')


# --- Repair Category Views ---

class RepairCategoryListView(LoginRequiredMixin, ListView):
    model = RepairCategory
    template_name = 'repairstore/repair_category_list.html'
    context_object_name = 'categories'


class RepairCategoryCreateView(LoginRequiredMixin, CreateView):
    model = RepairCategory
    fields = ['name', 'description']
    template_name = 'repairstore/repair_category_form.html'
    success_url = reverse_lazy('repairstore:repair_category_list')


class RepairCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = RepairCategory
    fields = ['name', 'description']
    template_name = 'repairstore/repair_category_form.html'
    success_url = reverse_lazy('repairstore:repair_category_list')


# --- Repair Service Views ---

class RepairServiceListView(LoginRequiredMixin, ListView):
    model = RepairService
    template_name = 'repairstore/repair_service_list.html'
    context_object_name = 'services'


class RepairServiceCreateView(LoginRequiredMixin, CreateView):
    model = RepairService
    fields = ['category', 'name', 'description', 'estimated_time', 'base_price']
    template_name = 'repairstore/repair_service_form.html'
    success_url = reverse_lazy('repairstore:repair_service_list')


class RepairServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = RepairService
    fields = ['category', 'name', 'description', 'estimated_time', 'base_price']
    template_name = 'repairstore/repair_service_form.html'
    success_url = reverse_lazy('repairstore:repair_service_list')


# --- Work Order Views ---

class WorkOrderListView(LoginRequiredMixin, ListView):
    model = WorkOrder
    template_name = 'repairstore/work_order_list.html'
    context_object_name = 'work_orders'
    ordering = ['-created_at']


class WorkOrderCreateView(LoginRequiredMixin, CreateView):
    model = WorkOrder
    fields = ['customer', 'bicycle', 'status', 'problem_description', 'notes']
    template_name = 'repairstore/work_order_form.html'
    success_url = reverse_lazy('repairstore:work_order_list')

    def form_valid(self, form):
        form.instance.status = WorkOrder.Status.NEW
        return super().form_valid(form)


class WorkOrderUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkOrder
    fields = ['status', 'problem_description', 'notes']
    template_name = 'repairstore/work_order_form.html'
    success_url = reverse_lazy('repairstore:work_order_list')


class WorkOrderDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkOrder
    template_name = 'repairstore/work_order_confirm_delete.html'
    success_url = reverse_lazy('repairstore:work_order_list')


class WorkOrderDetailView(LoginRequiredMixin, View):
    """Detail view for a work order with its items."""
    def get(self, request, pk):
        work_order = get_object_or_404(WorkOrder, pk=pk)
        items = work_order.items.all()
        context = {
            'work_order': work_order,
            'items': items,
        }
        return render(request, 'repairstore/work_order_detail.html', context)


# --- Product Category Views ---

class ProductCategoryListView(LoginRequiredMixin, ListView):
    model = ProductCategory
    template_name = 'repairstore/product_category_list.html'
    context_object_name = 'categories'


class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    fields = ['name', 'description']
    template_name = 'repairstore/product_category_form.html'
    success_url = reverse_lazy('repairstore:product_category_list')


class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    fields = ['name', 'description']
    template_name = 'repairstore/product_category_form.html'
    success_url = reverse_lazy('repairstore:product_category_list')


# --- Product Views ---

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'repairstore/product_list.html'
    context_object_name = 'products'
    ordering = ['name']


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'repairstore/product_form.html'
    success_url = reverse_lazy('repairstore:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'repairstore/product_form.html'
    success_url = reverse_lazy('repairstore:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'repairstore/product_confirm_delete.html'
    success_url = reverse_lazy('repairstore:product_list')


# --- Sale Views ---

class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'repairstore/sale_list.html'
    context_object_name = 'sales'
    ordering = ['-sale_date']


class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'repairstore/sale_form.html'
    success_url = reverse_lazy('repairstore:sale_list')


class SaleUpdateView(LoginRequiredMixin, UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'repairstore/sale_form.html'
    success_url = reverse_lazy('repairstore:sale_list')


class SaleDeleteView(LoginRequiredMixin, DeleteView):
    model = Sale
    template_name = 'repairstore/sale_confirm_delete.html'
    success_url = reverse_lazy('repairstore:sale_list')


# --- API / JSON Endpoints ---

def api_dashboard_stats(request):
    """API endpoint for dashboard statistics."""
    from django.db.models import F
    stats = {
        'customers': Customer.objects.count(),
        'bicycles': Bicycle.objects.count(),
        'work_orders': WorkOrder.objects.count(),
        'active_repairs': WorkOrder.objects.filter(status='in_repair').count(),
        'products': Product.objects.filter(is_active=True).count(),
        'total_sales': Sale.objects.count(),
        'low_stock': Product.objects.filter(quantity_in_stock__lte=F('reorder_level')).count(),
    }
    return JsonResponse(stats)


def api_customer_list(request):
    """API endpoint for customer list."""
    customers = Customer.objects.values('id', 'name', 'email', 'phone')[:50]
    return JsonResponse({'data': list(customers)})


def api_product_list(request):
    """API endpoint for product list."""
    products = Product.objects.filter(is_active=True).values('id', 'name', 'sku', 'retail_price', 'quantity_in_stock')[:50]
    return JsonResponse({'data': list(products)})


def api_recent_sales(request):
    """API endpoint for recent sales."""
    sales = Sale.objects.select_related('customer').order_by('-sale_date')[:10]
    data = []
    for s in sales:
        data.append({
            'id': s.id,
            'date': s.sale_date.isoformat(),
            'total': str(s.total),
            'customer': s.customer.name if s.customer else 'Walk-in',
            'payment': s.payment_method,
        })
    return JsonResponse({'data': data})