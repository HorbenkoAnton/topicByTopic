from django.shortcuts import render,redirect
from .forms import ContactForm,NewMessageForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def new_message_view(request):
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_success')
    else:
        form = NewMessageForm()
    return render(request, 'new_message.html', {'form': form})
