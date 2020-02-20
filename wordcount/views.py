from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"home.html")

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    most = dict()
    for word in wordlist:
        most[word] = 0
    for word in wordlist:
        most[word] +=1
    d = sorted(most.values(), reverse=True)
    mostp = ""
    for x in most:
        if most[x] == d[0]:
            mostp = x + "," +mostp
    a = sorted(most.items(),key=lambda most: most[1],reverse=True)

    
    return render(request,'count.html',{"text":fulltext , "count":len(wordlist),"mostapp":mostp,"most":a})

def about(request):
    return render(request,"about.html")