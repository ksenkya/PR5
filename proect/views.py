from django.shortcuts import render
import sqlite3

# Create your views here.

def first_page(request):
    return render(request, 'Page1.html')

def second_page(request):
    c = sqlite3.connect('basa.db')
    cur = c.cursor()
    cur.execute("SELECT Name,Opisanie,Price FROM Tovar")
    test = cur.fetchall()
    return render(request, 'Page2.html', {'test': test})
