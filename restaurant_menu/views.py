from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


# Class based views tend to have less code and are cleaner.
# CBVs allow you to create custom base classes or mixins that encapsulate common functionality across multiple views.
# Django provides many built-in CBVs (e.g., ListView, DetailView, CreateView, UpdateView, DeleteView),
# that handle common use cases out of the box, reducing boilerplate code.

# ListView is good for showing lots of data in a list
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("date_created")  # if you wanted to reverse the order then use '-date_created'
    template_name = "index.html"  # all templates must be created in a folder called templates within the root folder

    # to allow html to access data we use the context
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


# DetailView is good for showing detailed views of particular objects, e.g., meal item or blog post
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
