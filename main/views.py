from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Dark Side of the Moon',
        'price' : '650000',
        'description' : 'The Dark Side of the Moon is the eighth studio album by the English rock band Pink Floyd',
        'date_of_distribution' : '1 March 1973',
        'stock_available' : 10,
        'genre' : 'rock'
    }

    return render(request, "main.html", context)