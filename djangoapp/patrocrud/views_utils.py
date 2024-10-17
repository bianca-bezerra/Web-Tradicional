from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


def create(request, form_type, template, redirect_url, title):
    if request.method == "POST":
        form = form_type(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_type()
        context = {"form": form, "subtitle": title, "redirect_url": redirect_url}

    return render(request, template, context)


def delete(request, pk, model, redirect_url):
    objeto = get_object_or_404(model, pk=pk)
    objeto.delete()
    return HttpResponseRedirect(reverse(redirect_url))


def update(request, obj_type, form_type, pk, template, redirect_url, title):
    object = get_object_or_404(obj_type, pk=pk)

    if request.method == "POST":
        form = form_type(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(redirect_url, pk=object.pk)
    else:
        form = form_type(instance=object)

    context = {
        "form": form,
        "subtitle": title,
        "redirect_url": redirect_url,
        "pk": object.pk,
    }
    return render(request, template, context)
