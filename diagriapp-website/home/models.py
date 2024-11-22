from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AboutCompany(models.Model):
    summary = models.TextField()
    goals = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    link_to_app = models.URLField()

    def save(self, *args, **kwargs):
        if AboutCompany.objects.exists() and not self.pk:
            raise ValueError("Only one instance of AboutCompany is allowed.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return "About Company Configuration"


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    release_date = models.DateField()
    plants = models.ManyToManyField(Plant)

    def __str__(self):
        return self.title


class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
