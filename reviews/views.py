from django.shortcuts import render

def review(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        print(name, "-" , username)
    
    return render(request, "reviews/review.html")

def feedback(request):
    return render(request, "reviews/feedback.html")
