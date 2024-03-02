from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 120, blank = False, null = False)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete = models.SET_NULL,
                                 blank = True, null = True)
    description = models.TextField()
    image = models.ImageField(null = False, blank = False)

    def __str__(self):
        return self.description