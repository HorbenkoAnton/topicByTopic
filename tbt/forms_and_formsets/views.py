from django.shortcuts import render,redirect
from .forms import ContactForm,NewMessageForm,UserProfileForm,RegistrationForm
from .models import UserProfile, Address
from .forms import AddressFormSet

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


def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page or do something else
            return redirect('success_page')
    else:
        form = UserProfileForm()

    return render(request, 'user_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #some additional checks here
            return redirect('success_page')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form' : form})



def manage_addresses(request, user_id):
    user = UserProfile.objects.get(pk=user_id)
    if request.method == 'POST':
        formset = AddressFormSet(request.POST, queryset=Address.objects.filter(user=user))
        if formset.is_valid():
            addresses = formset.save(commit=False)
            for address in addresses:
                address.user = user
                address.save()
            return redirect('success_page')  # Redirect to success page upon successful form submission
    else:
        formset = AddressFormSet(queryset=Address.objects.filter(user=user))
    
    return render(request, 'manage_addresses.html', {'formset': formset, 'user': user})
