# Commerce with Django

- Lauch App
```
python manage.py makemigrations auctions
python manage.py migrate
```

- Run Server
```
python manage.py runserver
```
http://127.0.0.1:8000/

- Create Admin
```
python manage.py createsuperuser
```
<!-- super -->
<!-- password -->

- Create Model models.py
```
class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=240)
    category = models.CharField(max_length=64)
    url = models.CharField(max_length=240)
    bid = models.FloatField()

    def __str__(self):
        return f"{self.title}"
```

- Register Your Model admin.py
```
from .models import Listing
admin.site.register(Listing)
```

- Update views to consume table data
```
from .models import Listing

def index(request, ):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })
```

- Create new Listing / Update database from form
```
def new(request):
    if request.method == 'POST':
        title = request.POST['title']

        new_listing = Listing(title=title)
        new_listing.save()

    return render(request, "auctions/new.html")
```

