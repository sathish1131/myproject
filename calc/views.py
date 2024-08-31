from django.shortcuts import render
import numexpr as ne

# Create your views here.

def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            result = ne.evaluate(expression)
        except Exception as e:
            result = f"Error: {str(e)}"
        return render(request, 'calc.html', {'result': result})
    return render(request, 'calc.html')