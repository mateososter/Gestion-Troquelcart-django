from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "cliente"
        verbose_name_plural= "clientes"


    id = models.AutoField(primary_key=True, unique=True, blank=False)
    name = models.CharField(max_length=100, verbose_name="nombre", unique=True)
    telephone = models.CharField(max_length=15, verbose_name="telefono/celular")
    mail = models.EmailField(max_length=254, verbose_name="correo electronico")
    street = models.CharField(max_length=100, verbose_name="calle")
    number = models.IntegerField(verbose_name="altura")
    floor = models.CharField(max_length=5, verbose_name="piso", blank=True)
    dept = models.CharField(max_length=5, verbose_name="departamento", blank=True)

    def get_absolute_url(self):
        return reverse("pegado:client-detail", kwargs={"pk":self.id})

class Material(models.Model):
    def __str__(self):
        return self.material

    class Meta:
        verbose_name= "material"
        verbose_name_plural= "materiales"
    
    id = models.AutoField(primary_key=True, unique=True, blank=False)
    material = models.CharField(max_length=100)

class Product(models.Model):
    def __str__(self):
        return self.model
    
    class Meta:
        verbose_name= "producto"
        verbose_name_plural= "productos"

    id = models.AutoField(primary_key=True, unique=True, blank=False)
    id_client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name = "productos", verbose_name= "cliente")
    id_material = models.ForeignKey(to=Material, on_delete=models.CASCADE, verbose_name= "material")
    model = models.CharField(max_length=100, unique=True, verbose_name="modelo")
    modality = models.CharField(max_length=50, verbose_name="modalidad de entrega")
    value_prefolding = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="valor de predoblado", help_text="Este es el valor que cobra Gaby por el trabajo por cada millar") 
    value_window = models.DecimalField(max_digits=20,decimal_places=2, verbose_name="valor de ventana", help_text="Este es el valor que cobra Gaby por el trabajo por cada millar") 
    value_lateral = models.DecimalField(max_digits=20,decimal_places=2, verbose_name="valor de lateral", help_text="Este es el valor que cobra Gaby por el trabajo por cada millar") 
    value_bottom  = models.DecimalField(max_digits=20,decimal_places=2, verbose_name="valor de fondeo", help_text="Este es el valor que cobra Gaby por el trabajo por cada millar")
    value_millar  = models.DecimalField(max_digits=20,decimal_places=2, verbose_name="valor del millar", help_text="Este es el valor que cobra Gaby por el trabajo por cada millar")
    comision_prefolding = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="comision de predoblado", help_text="Este es el valor que paga Gaby a cada pegadora por el trabajo por cada millar")
    comision_window = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="comision de ventana", help_text="Este es el valor que paga Gaby a cada pegadora por el trabajo por cada millar")
    comision_lateral = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="comision de lateral", help_text="Este es el valor que paga Gaby a cada pegadora por el trabajo por cada millar")
    comision_bottom = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="comision de fondeo", help_text="Este es el valor que paga Gaby a cada pegadora por el trabajo por cada millar")
    
    def get_absolute_url(self):
        return reverse("pegado:product-detail", kwargs={"pk":self.id})


class Worker(models.Model):
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= "pegadora"
        verbose_name_plural= "pegadoras"

    id=models.AutoField(primary_key=True, unique=True, blank=False)
    name = models.CharField(max_length=100, verbose_name="nombre", unique=True)
    telephone = models.CharField(max_length=15, verbose_name="telefono/celular")
    mail = models.EmailField(max_length=254, verbose_name="correo electronico")
    join_date = models.DateField(verbose_name="fecha de inicio de actividades")
    net_cash = models.DecimalField(max_digits=20,decimal_places=2, verbose_name="saldo",default=0)

    def get_absolute_url(self):
        return reverse("pegado:worker-detail", kwargs={"pk":self.id})

class Payment(models.Model):
    def __str__(self):
        return self.id

    class Meta:
        verbose_name= "pago"
        verbose_name_plural= "pagos"

    id = models.AutoField(primary_key=True, unique=True, blank=False)
    id_workername = models.ForeignKey(to=Worker, on_delete=models.CASCADE, related_name = "pagos", verbose_name= "pegadora")
    date = models.DateField(verbose_name="fecha de pago")
    amount = models.DecimalField(max_digits=20,decimal_places=2, verbose_name="monto")

    def get_absolute_url(self):
        return reverse("pegado:payment-list")
        
class Order(models.Model):
    def __str__(seld):
        return self.id 

    class Meta:
        verbose_name= "trabajo"
        verbose_name_plural= "trabajos"

    id= models.AutoField(primary_key=True, unique=True, blank=False)
    id_product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name = "trabajos", verbose_name= "modelo")
    id_workername = models.ForeignKey(to=Worker, on_delete=models.CASCADE, related_name = "trabajos", verbose_name= "pegadora")
    quantity = models.IntegerField(verbose_name= "cantidad")
    prefolding = models.BooleanField(verbose_name= "predoblado", help_text="Indica si se realizo predoblado")
    window = models.BooleanField(verbose_name= "ventana", help_text="Indica si se realizo ventana")
    lateral = models.BooleanField(verbose_name= "lateral", help_text="Indica si se realizo lateral")
    bottom = models.BooleanField(verbose_name= "fondeo", help_text="Indica si se realizo fondeo")
    is_complete = models.BooleanField(verbose_name= "completo", help_text="Indica si el pedido esta terminado completamente")
    amount = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="monto del trabajo")

    def get_absolute_url(self):
        return reverse("pegado:order-detail", kwargs={"pk":self.id})