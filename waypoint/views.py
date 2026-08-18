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

def search(request):
    query = request.GET.get("q", "")
    context = {"query": query}
    return render(request, "search.html", context)

def catalog(request):
    trails = [
        {"name": "Ridge Loop", "distance": 5.2, "elevation": 320, "difficulty": "moderate", "is_open": True},
        {"name": "Summit Trail", "distance": 8.7, "elevation": 950, "difficulty": "expert", "is_open": True},
        {"name": "Creekside Path", "distance": 2.1, "elevation": 40, "difficulty": "easy", "is_open": True},
        {"name": "Backcountry Run", "distance": 12.4, "elevation": 1100, "difficulty": "expert", "is_open": False},
        {"name": "Meadow Walk", "distance": 3.5, "elevation": 90, "difficulty": "easy", "is_open": True},
        {"name": "Rocky Pass", "distance": 6.8, "elevation": 610, "difficulty": "moderate", "is_open": False},
    ]
    return render(request, "catalog.html", {"trails": trails})