from django.shortcuts import render


def home(request):
    context = {"visitor_name": "trail explorer"}
    return render(request, "home.html", context)
def report(request):
    if request.method == "POST":
        context = {
            "name": request.POST.get("name", ""),
            "trail": request.POST.get("trail", ""),
        }
        return render(request, "thank_you.html", context)
    return render(request, "report.html")
