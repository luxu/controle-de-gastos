# coding=utf-8

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model

User = get_user_model()

class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()
