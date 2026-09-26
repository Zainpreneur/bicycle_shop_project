from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Customer model for both retail sales and repair services."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Bicycle(models.Model):
    """Bicycle model for tracking bikes brought in for repair."""
    class FrameType(models.TextChoices):
        ROAD = 'road', 'Road Bike'
        MOUNTAIN = 'mountain', 'Mountain Bike'
        HYBRID = 'hybrid', 'Hybrid Bike'
        ELECTRIC = 'electric', 'Electric Bike'
        CHILD = 'child', 'Child Bike'
        OTHER = 'other', 'Other'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bicycles')
    frame_type = models.CharField(max_length=20, choices=FrameType.choices)
    frame_size = models.CharField(max_length=20, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=50, blank=True)
    frame_number = models.CharField(max_length=100, unique=True, blank=True)
    acquired_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='in_repair', choices=[
        ('in_repair', 'In Repair'),
        ('ready', 'Ready for Pickup'),
        ('completed', 'Completed'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.brand} {self.model} ({self.customer})"


class RepairCategory(models.Model):
    """Categories for repair services (e.g., 'Mechanical', 'Electrical', 'Body')."""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class RepairService(models.Model):
    """Specific repair services offered."""
    category = models.ForeignKey(RepairCategory, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    estimated_time = models.IntegerField(help_text="Estimated minutes to complete")
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']
        unique_together = ['category', 'name']

    def __str__(self):
        return f"{self.category.name}: {self.name}"


class WorkOrder(models.Model):
    """Repair work order tracking a bicycle's repair progress."""
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        IN_PROGRESS = 'in_progress', 'In Progress'
        READY = 'ready', 'Ready for Pickup'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='work_orders')
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE, related_name='work_orders')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    problem_description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"WO #{self.id} - {self.bicycle} - {self.status}"


class WorkOrderItem(models.Model):
    """Individual line items within a work order."""
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='items')
    repair_service = models.ForeignKey(RepairService, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['repair_service__name']

    def __str__(self):
        return f"{self.repair_service.name} x {self.quantity}"


class ProductCategory(models.Model):
    """Categories for retail products."""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Retail products sold in the store."""
    class Condition(models.TextChoices):
        NEW = 'new', 'New'
        USED = 'used', 'Used'
        REFURBISHED = 'refurbished', 'Refurbished'

    class GenderTarget(models.TextChoices):
        MEN = 'men', 'Men'
        WOMEN = 'women', 'Women'
        UNISEX = 'unisex', 'Unisex'
        KIDS = 'kids', 'Kids'

    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    condition = models.CharField(max_length=20, choices=Condition.choices, default=Condition.NEW)
    gender_target = models.CharField(max_length=20, choices=GenderTarget.choices, default=GenderTarget.UNISEX)
    brand = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=20, blank=True)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)
    retail_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ['sku', 'category']

    def __str__(self):
        return f"{self.name} ({self.category})"

    @property
    def profit_margin(self):
        if self.retail_price == 0:
            return 0
        return round(((self.retail_price - self.cost_price) / self.retail_price) * 100, 2)


class Sale(models.Model):
    """Sales transaction record."""
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('mobile', 'Mobile Payment'),
        ('credit', 'Credit'),
    ])
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-sale_date']

    def __str__(self):
        return f"Sale #{self.id} - {self.total} - {self.sale_date.date()}"


class SaleItem(models.Model):
    """Individual items within a sale."""
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # price at time of sale
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ['product__name']

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    @property
    def line_total(self):
        return self.price * self.quantity

    @property
    def discount_amount(self):
        return (self.price * self.quantity * self.discount_percent) / 100
