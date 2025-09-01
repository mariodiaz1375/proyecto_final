from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nombre = models.CharField(max_length=255, db_column='nom_pac')
    apellido = models.CharField(max_length=255, db_column='ape_pac')
    dni = models.CharField(max_length=255, db_column='dni_pac')
    fecha_nacimiento = models.DateField(db_column='dni_pac')
    domicilio = models.CharField(max_length=255, db_column='dom_pac')
    telefono = models.CharField(max_length=255, db_column='tel_pac')
    email = models.EmailField(max_length=255, db_column='dni_pac')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



    # id_pac INT AUTO_INCREMENT,
    # nom_pac VARCHAR(50) NOT NULL,
    # ape_pac VARCHAR(50) NOT NULL,
    # dni_pac VARCHAR(12) NOT NULL,
    # fec_nac_pac DATE,
    # dom_pac VARCHAR(50),
    # tel_pac VARCHAR(40) NOT NULL,
    # email_pac VARCHAR(50),
    # CONSTRAINT pk_pac PRIMARY KEY(id_pac)