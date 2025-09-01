from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    domicilio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.dni} {self.nombre} {self.apellido}"



    # id_pac INT AUTO_INCREMENT,
    # nom_pac VARCHAR(50) NOT NULL,
    # ape_pac VARCHAR(50) NOT NULL,
    # dni_pac VARCHAR(12) NOT NULL,
    # fec_nac_pac DATE,
    # dom_pac VARCHAR(50),
    # tel_pac VARCHAR(40) NOT NULL,
    # email_pac VARCHAR(50),
    # CONSTRAINT pk_pac PRIMARY KEY(id_pac)