from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# import de models.py de apps.business
from ..business.models import Business

class UserProfile(models.Model):
    """Representa el perfil de usuario en el sistema

    El perfil de usuario sirve para identificar las características del
    usuario, tanto como los atributos del usuario en sí como los de la empresa
    a la que pertenece el usuario, junto con otros datos propios del perfil.

    Attributes:
        user: Es el usuario al que pertenece el perfil del usuario.
        business: Empresa a la que pertenece el usuario.
        deleted: Representa de manera digital si el perfil del usuario está activo.
    """

    deleted = models.BooleanField(default=False)

    #foreign keys:
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    business = mode.ForeignKey(Business, on_delete=models.PROTECT, null=True, blank=True)

    def is_active(self):
        """Indica si el perfil de usuario está  activo.

            El Modelo UserProfile en sí no posee un atributo propio que indique que está 
            activo, es su defecto usa el estado del usuario asociado como indicador
            propio para verificar si el perfil está activo.

            Args:
            self:
                La propia instancia del Modelo.

            Returns:
            Un Boolean que indica si el perfil está activo. 
        """

        return self.user.is_active

    def activate(self):
        """Activa el perfil del usuario, activando al usuario del perfil.

            Args:
            self:
                La propia instancia del Modelo.
        """
        self.user.is_active = True
        self.save()

    def deactivate(self):
        """Desactiva el perfil del usuario, desactivando al usuario del perfil.

            Args:
            self:
                La propia instancia del Modelo.
        """
        self.user.is_active = False
        self.save()    

    def __str__(self):
        return f"Perfil del Usuario {0}".format(self.user.get_full_name)

    class Meta:
        """Clase que usa Django para configurar el modelo.

        docs: https://docs.djangoproject.com/en/4.0/ref/models/options/

        Attributes:
            verbose_name = Un nombre legible por humanos para el objeto, en singular.
            verbose_name_plural = El nombre plural del objeto.
            ordering = El orden predeterminado para el objeto, para usar al obtener listas de objetos, puede ser por mas de un atributo, asd o desc
            permissions = Permisos adicionales para ingresar en la tabla de permisos al crear este objeto.
        """
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuarios"
        ordering = ["-id"]