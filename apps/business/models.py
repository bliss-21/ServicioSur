from django.db import models

# Region > Province > Commune

class Region(models.Model):
    """Representa las regiones en las que está dividida un país.

    Attributes:
        name: Nombre de la región.
    """
    
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        """Clase que usa Django para configurar el modelo.

        docs: https://docs.djangoproject.com/en/4.0/ref/models/options/

        Attributes:
            verbose_name = Un nombre legible por humanos para el objeto, en singular.
            verbose_name_plural = El nombre plural del objeto.
            ordering = El orden predeterminado para el objeto, para usar al obtener listas de objetos, puede ser por mas de un atributo, asd o desc
            permissions = Permisos adicionales para ingresar en la tabla de permisos al crear este objeto.
        """
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ["name"]

class Province(models.Model):
    """Representa las provincias que puede contener una región del país.

    Attributes:
        name: Nombre de la provincia.
        region: Relación de la región a la que pertenece la provincia.
    """
    name = models.CharField(max_length=255, null=False, blank=False)

    #foreign keys:
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        """Clase que usa Django para configurar el modelo.

        docs: https://docs.djangoproject.com/en/4.0/ref/models/options/

        Attributes:
            verbose_name = Un nombre legible por humanos para el objeto, en singular.
            verbose_name_plural = El nombre plural del objeto.
            ordering = El orden predeterminado para el objeto, para usar al obtener listas de objetos, puede ser por mas de un atributo, asd o desc
            permissions = Permisos adicionales para ingresar en la tabla de permisos al crear este objeto.
        """
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ["name"]

class Commune(models.Model):
    """Representa las comunas que puede contener una provincia de la región.

    Attributes:
        name: Nombre de la comuna.
        province: Relación de la provincia en la que se encuentra la comuna. 
        region: Relación de la región en la que se encuentra la comuna.
    """
    name = models.CharField(max_length=255, null=False, blank=False)

    #foreign keys:
    province = models.ForeignKey(Province, on_delete=models.PROTECT, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        """Clase que usa Django para configurar el modelo.

        docs: https://docs.djangoproject.com/en/4.0/ref/models/options/

        Attributes:
            verbose_name = Un nombre legible por humanos para el objeto, en singular.
            verbose_name_plural = El nombre plural del objeto.
            ordering = El orden predeterminado para el objeto, para usar al obtener listas de objetos, puede ser por mas de un atributo, asd o desc
            permissions = Permisos adicionales para ingresar en la tabla de permisos al crear este objeto.
        """
        verbose_name = "Camuna"
        verbose_name_plural = "Comunas"
        ordering = ["name"]

class Business(models.Model):
    """Representa una empresa a la que se prestan servicios. 

    Attributes:
        name: Nombre empresa.
        rut: Rol único tributario de la empresa.
        address = Indica la dirección  de las oficinas que tiene registrada la empresa.
        address_number = Numero asociado a la dirección .
        create_datetime = Fecha y hora en la que fue ingresada la empresa en el sistema.
        active = Si la empresa está  activa en el sistema.
        deleted = Si la empresa ha sido borrada del sistema.
        province: Relación de la provincia en la que se encuentra la comuna. 
        region: Relación de la región en la que se encuentra la comuna.
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    rut = models.CharField(max_length=50, null=True, blank=True)
    direccion  = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address_number = models.CharField(max_length=10, null=True, blank=True)
    create_datetime=models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True)  
    deleted = models.BooleanField(default=False)  

    #foreign keys:
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=False, blank=False)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, null=False, blank=False)
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        """Clase que usa Django para configurar el modelo.

        docs: https://docs.djangoproject.com/en/4.0/ref/models/options/

        Attributes:
            verbose_name = Un nombre legible por humanos para el objeto, en singular.
            verbose_name_plural = El nombre plural del objeto.
            ordering = El orden predeterminado para el objeto, para usar al obtener listas de objetos, puede ser por mas de un atributo, asd o desc
            permissions = Permisos adicionales para ingresar en la tabla de permisos al crear este objeto.
        """
        verbose_name = "Negocio"
        verbose_name_plural = "Negocios"
        ordering = ["create_datetime"]