from django.shortcuts import render, redirect
from .models import Name, Rule
from .forms import NameForm, RuleForm
from django.http import JsonResponse


def home(request):
    names = Name.objects.all()
    rules = Rule.objects.all()
    return render(request, 'secret_santa/home.html', {'names': names, 'rules': rules})

def add_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_name = form.save()  # Save the new name
            return JsonResponse({'name': new_name.name})
    return JsonResponse({'name': None})  # Return a JSON response even if there's an issue

def add_rule(request):
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            new_rule = form.save()  # Save the new rule
            return JsonResponse({
                'name1': new_rule.name1.name,
                'name2': new_rule.name2.name,
            })
    return JsonResponse({'name1': None, 'name2': None})  # Return a JSON response even if there's an issue

def secret_santa(request):
    # Implement the secret_santa function to generate results
    # Pass results to the template
    return render(request, 'secret_santa/result.html')

def delete_name(request, name_id):
    try:
        name = Name.objects.get(id=name_id)
        name.delete()
        return JsonResponse({'message': 'Name deleted successfully'})
    except Name.DoesNotExist:
        return JsonResponse({'message': 'Name not found'}, status=404)

def delete_rule(request, rule_id):
    try:
        rule = Rule.objects.get(id=rule_id)
        rule.delete()
        return JsonResponse({'message': 'Rule deleted successfully'})
    except Rule.DoesNotExist:
        return JsonResponse({'message': 'Rule not found'}, status=404)
