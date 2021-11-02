from django.shortcuts import render

def Home(reguest):
    return render(reguest,'Home.html')

def test(reguest):
    return render(reguest,'table.html')