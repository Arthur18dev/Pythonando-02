from django.db import models

class Convidados(models.Model):
    nome_convidado = models.CharField(max_length=100)
    token = models.CharField(max_length=100, unique=True)  # Token único para cada convidado
    status = models.CharField(
        max_length=2, 
        choices=[('AC', 'A Confirmar'), ('C', 'Confirmado'), ('R', 'Recusado')], 
        default='AC'
    )

    def __str__(self):
        return self.nome_convidado


class Acompanhante(models.Model):
    convidado = models.ForeignKey(Convidados, on_delete=models.CASCADE, related_name="acompanhantes")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Presentes(models.Model):
    nome_presente = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='presentes/', blank=True, null=True)  # Foto do presente
    importancia = models.IntegerField(choices=[(1, 'Pouco importante'), (2, 'Importante'), (3, 'Muito importante')])
    reservado = models.BooleanField(default=False)  # Indica se o presente foi reservado
    reservado_por = models.ForeignKey(Convidados, on_delete=models.SET_NULL, null=True, blank=True)  # O convidado que reservou o presente

    def __str__(self):
        return self.nome_presente
