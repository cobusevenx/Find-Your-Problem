from django.shortcuts import render
from django .http import HttpResponse
from django.template import loader
import requests
from time import sleep
from bs4 import BeautifulSoup


def getlinks(li):
    finallist=[]
    for d in range(1,32):
        try:
            #sleep(3)
            s="http://codeforces.com/problemset/page/"
            s=s + str(d)

            r=requests.get(s)
            #print(r.content)
            soup=BeautifulSoup(r.content,"html.parser")
            data=soup.find_all("table",{"class":"problems"})
            for x in data:
                   y=x.find_all("td")
                   l=len(y)
                   #print(y)
                   for i in range(0,l,4):
                        #print(y[i+1])
                        flag=1
                        for tag in li:
                            if tag in y[i+1].text:
                                flag=1
                            else:
                                flag=0
                                break
                        if flag==1:
                            #print(y[i+1])
                            t=str(y[i+1])
                            #print(t[60:65].split("/")[0])
                            #print(str(t[n:n+24].split("/")[0]))
                            a=y[i+1].text.split("\r\n")
                            #print(a)
                            #print(a[1].split("\n\n")[0])
                            #l1.append(t[60:65].split("/")[0])
                           # context.update("")
                            #l2.append(t[60:65].split("/")[1])
                            #l3.append(a[1].split("\n\n")[0])
                            s=t[60:65].split("/")[0] + "/" + t[60:65].split("/")[1]
                            finallist.append([t[60:65].split("/")[0],t[60:65].split("/")[1],a[1].split("\n\n")[0],s])
                            #lis.append(t[60:65].split("/")[0]+"   "+t[60:65].split("/")[1]+"     "+a[1].split("\n\n")[0])
                            #print(lis)
        except requests.ConnectionError:
            sleep(5)
            continue
    return finallist
def getdata(s):
    n=s.find("tag")
    a=s[n+7:int(len(s))-3]
    x=s[n+7:int(len(s))].find("]")
    e=s[n+7:n+x+7]
    p=e.split("'")
    l=p[1:int(len(p))-1:2]

    return l
def gethackerlinks(val):
    s="https://www.hackerrank.com/domains/algorithms/" + str(val[0])
    return s
def index(request):
    #print(request.POST)
    if request.method=="POST":
        req=str(request.POST)
        print(req)
        val=getdata(req)
        print(val[0])
        final=getlinks(val)
        hackerlink=gethackerlinks(val)
        context={"hacker":hackerlink,"result":final,"value":val[0],} #"result":final
        return render(request,"home/results.html",context)

    #return render(request,"home/index.html",{})
def index2(request):
    return render(request,"home/index.html",{"1":2})
