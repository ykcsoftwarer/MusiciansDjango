from django.shortcuts import render, HttpResponse


def home_page(request):
    return render(request, "index.html")

"""<div style="color:white; height:1000px; background-color:black; ">
   <h1>Hello this is the user</h1>
  </div>"""