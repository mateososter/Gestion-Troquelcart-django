from django import forms

from .models import Worker, Product, Client, Payment

class WorkerModelForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields= [
            "name",
            "telephone",
            "mail",
            "join_date",
            "net_cash"
        ]

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= [
            "model",
            "id_client",
            "id_material",
            "modality",
            "value_prefolding",
            "value_window",
            "value_lateral" ,
            "value_bottom"  ,
            "value_millar" ,
            "comision_prefolding" ,
            "comision_window" ,
            "comision_lateral", 
            "comision_bottom"
        ]

class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields= [
            "name",
            "telephone",
            "mail",
            "street",
            "number",
            "floor",
            "dept"
        ]

class PaymentModelForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields= [
            "id_workername",
            "date",
            "amount"
        ]