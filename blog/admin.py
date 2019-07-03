from django.contrib import admin
from .models import Post

# ми імпортуємо (включаємо) модель посту Post визначену у попередньому
# розділі(models.py). Щоб зробити нашу модель видимою на сторінці адміністратора, потрібно зареєструвати
# модель за допомогою admin.site.register(Post)

# щоб зайти в панель адміністратора потрібно спершу створити супер користувача за допомогою команди:
# python manage.py createsuperuser

admin.site.register(Post)



