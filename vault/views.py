from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Vault, Info
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import VaultForm, UserRegistrationForm


class VaultView(LoginRequiredMixin, ListView):
    model = Info
    template_name= "vault/home.html"
    context_object_name = "vault"

    
    def get_queryset(self):
        data = Vault.objects.get(user_id=self.request.user)
        qs = Info.objects.all().filter(vault_id=data)
        if qs:
            return qs
        return redirect("add")


class AddAccountView(LoginRequiredMixin, CreateView):
    model = Info
    form_class = VaultForm
    context_object_name = "content" 
    template_name = "vault/create_acc.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.vault_id = Vault.objects.get(user_id=self.request.user)

        return super().form_valid(form)


class CreateAccount(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "vault/register.html"
    success_url = reverse_lazy("home")


class DeleteAccView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Info
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()

        if obj.vault_id.user_id == self.request.user:
            return True
        return False

class UpdateAccView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Info
    success_url = reverse_lazy("home")
    template_name = "vault/update_acc.html"
    form_class = VaultForm

    def test_func(self):
        obj = self.get_object()
        if obj.vault_id.user_id == self.request.user:
            return True
        print("False")
        return False

    def form_valid(self, form):
        form.instance.vault_id = Vault.objects.get(user_id=self.request.user)
        return super().form_valid(form)