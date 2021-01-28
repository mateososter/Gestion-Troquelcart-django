from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
    )
from .forms import WorkerModelForm, ProductModelForm, ClientModelForm, PaymentModelForm
from .models import Worker, Product, Client, Material, Payment

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request,"base.html", {})

class WorkerListView(ListView):
    template_name = "pegado/worker_list.html"
    queryset = Worker.objects.all()

class WorkerDetailView(DetailView):
    template_name = "pegado/worker_detail.html"
    queryset = Worker.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Worker,id=id_)

class WorkerCreateView(CreateView):
    template_name = "pegado/worker_create.html"
    form_class = WorkerModelForm
    queryset = Worker.objects.all()

class WorkerUpdateView(UpdateView):
    template_name = "pegado/worker_update.html"
    form_class = WorkerModelForm
    queryset = Worker.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Worker,id=id_)

class WorkerDeleteView(DeleteView):
    template_name = "pegado/worker_delete.html"
    queryset = Worker.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Worker,id=id_)

    def get_success_url(self):
        return reverse("pegado:worker-list")

class ProductListView(ListView):
    template_name = "pegado/product_list.html"
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    template_name = "pegado/product_detail.html"
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product,id=id_)

class ProductCreateView(CreateView):
    template_name = "pegado/product_create.html"
    form_class = ProductModelForm
    queryset = Product.objects.all()

class ProductUpdateView(UpdateView):
    template_name = "pegado/product_update.html"
    form_class = WorkerModelForm
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product,id=id_)

class ProductDeleteView(DeleteView):
    template_name = "pegado/product_delete.html"
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product,id=id_)

    def get_success_url(self):
        return reverse("pegado:worker-list")

class ClientListView(ListView):
    template_name = "pegado/client_list.html"
    queryset = Client.objects.all()

class ClientDetailView(DetailView):
    template_name = "pegado/client_detail.html"
    queryset = Client.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Client,id=id_)

class ClientCreateView(CreateView):
    template_name = "pegado/client_create.html"
    form_class = ClientModelForm
    queryset = Client.objects.all()

class ClientUpdateView(UpdateView):
    template_name = "pegado/client_update.html"
    form_class = ClientModelForm
    queryset = Client.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Client,id=id_)

class ClientDeleteView(DeleteView):
    template_name = "pegado/client_delete.html"
    queryset = Client.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Client,id=id_)

    def get_success_url(self):
        return reverse("pegado:client-list")

def material_create_view(request):
    
    if request.method == "POST":
        new_material=request.POST.get('material')
        #Acá podría haber una validación
        Material.objects.create(material=new_material)

    return render(request,"pegado/material_create.html", {})

class PaymentCreateView(CreateView):
    template_name = "pegado/payment_create.html"
    form_class = PaymentModelForm
    queryset = Payment.objects.all()

class PaymentListView(ListView):
    template_name = "pegado/payment_list.html"
    queryset = Payment.objects.all()
