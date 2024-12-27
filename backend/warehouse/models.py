from django.db import models

from shortuuid.django_fields import ShortUUIDField

from supplier.models import Supplier


class Warehouse(models.Model):
    name = models.CharField(max_length=144)
    location = models.CharField(max_length=255)
    sku = ShortUUIDField(
        max_length=10, db_index=True, unique=True, alphabet="01234abcde"
    )

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=144)
    description = models.CharField(max_length=255)
    sku = ShortUUIDField(
        max_length=10, db_index=True, unique=True, alphabet="12345abcde"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="product_supplier"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=144)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to="product/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    can_supply = models.BooleanField(default=False)
    sku = ShortUUIDField(
        max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij"
    )

    def activeProduct(self) -> object:
        return Product.objects.filter(is_active=True)

    def __str__(self) -> str:
        return f"{self.supplier.user.username} can supplies {self.name} from {self.category.title}"
