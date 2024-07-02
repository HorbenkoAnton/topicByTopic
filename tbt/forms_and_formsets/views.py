from django.shortcuts import render,redirect
from .forms import ContactForm,NewMessageForm,UserProfileForm,RegistrationForm, AddressForm,ImageForm,DocumentForm
from .models import UserProfile, Address,Image
from django.forms import modelformset_factory


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


def manage_addresses(request):
    # Formsets are better be declared at forms.py but let's try this one
    AddressFormSet = modelformset_factory(Address, form=AddressForm, extra=1)

    if request.method == 'POST':
        formset = AddressFormSet(request.POST, queryset=Address.objects.filter(user=request.user))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
            return redirect('success_page')
    else:
        formset = AddressFormSet(queryset=Address.objects.filter(user=request.user))

    return render(request, 'manage_addresses.html', {'formset': formset})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)  # Pass request.FILES here for file handling
        if form.is_valid():
            form.save()
            return redirect('images_list')
    else:
        form = ImageForm()
    
    return render(request, 'upload_image.html', {'form': form})

def images_list(request):
    images = Image.objects.all()
    return render(request, 'images_list.html', {'images': images})

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request , 'upload_file.html', {'form':form})