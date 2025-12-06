from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import EncodeForm, DecodeForm
from .utils import encode_message, decode_message
from io import BytesIO

def home(request):
    return render(request, 'home.html')

def encode(request):
    if request.method == 'POST':
        form = EncodeForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            message = form.cleaned_data['message']
            password = form.cleaned_data['password']
            
            try:
                encoded_image = encode_message(image_file, message, password)
                
                response = HttpResponse(content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename="encoded_image.png"'
                # Optimize PNG: level 9 compression, no interlacing
                encoded_image.save(response, 'PNG', optimize=True, compress_level=9)
                return response
            except Exception as e:
                messages.error(request, f"Error encoding message: {str(e)}")
    else:
        form = EncodeForm()
    return render(request, 'encode.html', {'form': form})

def decode(request):
    result = None
    if request.method == 'POST':
        form = DecodeForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            password = form.cleaned_data['password']
            try:
                result = decode_message(image_file, password)
                if result.startswith("Error"):
                     messages.error(request, result)
                     result = None
                else:
                    messages.success(request, "Message decoded successfully!")
            except Exception as e:
                messages.error(request, f"Error decoding message: {str(e)}")
    else:
        form = DecodeForm()
    return render(request, 'decode.html', {'form': form, 'result': result})
