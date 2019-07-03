from django.db import models
from django.utils import timezone

# Коли змінюємо модель потрібно повідомити Джанго що змінилась наша модель за допомогою команди  +
# python manage.py makemigrations blog
# Django підготував для нас файл перенесення, який ми повинні тепер застосувати до нашої бази даних
# Набери python manage.py migrate blog

class Post(models.Model):   # означає, що Post є Django моделлю,
                            # отже Django знає, що вона повинна бути збережена у базі даних.

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # зв'язок із іншою моделлю.
    title = models.CharField(max_length=200)  # для текстових полів з обмеженням кількісті символів
    text = models.TextField()                 # великі блоки тексту без обмежень.
    created_date = models.DateTimeField(      # дата та час.
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
