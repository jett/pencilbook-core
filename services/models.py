from django.db import models
from tenants.models import TenantAwareModel

# Create your models here.
class Category(TenantAwareModel):

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(TenantAwareModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    categories = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name