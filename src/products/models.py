from django.db import models
from django.urls import reverse

def upload_product_image(instance, filename):
    Klass = instance.__class__
    id_ = Klass.objects.count()
    return f"products/{id_}/{filename}" # "products/{id_}/{filename}".format(id_=id_, filename=filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    #image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=9.99)

    def __str__(self):
        return self.title

    def get_api_url(self):
        return reverse("products-api:detail", kwargs={"id": self.id})
