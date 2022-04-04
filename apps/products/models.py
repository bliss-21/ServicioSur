from itertools import product
from django.db import models
# import de models.py de apps.business
from ..business.models import Business

# Clase Tipo Producto
class ProductType(models.Model):
    """Son los distintos tipos de productos que se pueden almacenar en la BD

    Attributes:
        type_product: Nombre del producto.
    """
    #no sé si dejarlo Charfield, dependerá de cuantos tipos de productos ofrezcamos pero ahí vemos.
    type_product =  models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.type_product

    class Meta:
        """Clase que usa Django para configurar el modelo.

        docs: https://docs.djangoproject.com/en/4.0/ref/models/options/

        Attributes:
            verbose_name = Un nombre legible por humanos para el objeto, en singular.
            verbose_name_plural = El nombre plural del objeto.
            ordering = El orden predeterminado para el objeto, para usar al obtener listas de objetos, puede ser por mas de un atributo, asd o desc
            permissions = Permisos adicionales para ingresar en la tabla de permisos al crear este objeto.
        """
        verbose_name = "Tipo de Producto"
        verbose_name_plural = "Tipos de Productos"
        ordering = ["type_product"]


# Clase Producto
class Product(models.Model):
    """Son los distintos productos que se pueden almacenar en la BD

    Attributes:
        product_name:  Nombre del producto.
        value: valor del producto.
        unit:  cantidad de productos.
        active: Si el producto está  activo en el sistema.
        deleted: Si el producto ha sido borrado del sistema.
        create_datetime: Fecha y hora en la que fue ingresado el producto en el sistema.
        modification_date: fecha y hora de la modificación del producto en el sistema.
    """
    
    product_name =  models.CharField(max_length=255, null=False, blank=False)
    value = models.IntegerField(null=False, blank=False)
    unit = models.IntegerField(null=False, blank=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    modification_date = models.DateTimeField(auto_now_add=True, blank=True)

    #foreign keys:
    business = models.ForeignKey(Business, on_delete=models.PROTECT, null=True, blank=True)
    type_product = models.ForeignKey(ProductType, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.product_name

    class Meta:
        """Clase que usa Django para configurar el modelo.

        docs: https://docs.djangoproject.com/en/4.0/ref/models/options/

        Attributes:
            verbose_name = Un nombre legible por humanos para el objeto, en singular.
            verbose_name_plural = El nombre plural del objeto.
            ordering = El orden predeterminado para el objeto, para usar al obtener listas de objetos, puede ser por mas de un atributo, asd o desc
            permissions = Permisos adicionales para ingresar en la tabla de permisos al crear este objeto.
        """
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["product_name"]
