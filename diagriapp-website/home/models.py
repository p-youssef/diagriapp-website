from django.db import models
from django.utils.timezone import now  

class Plant(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم النبات")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نبات"
        verbose_name_plural = "نباتات"


class AboutCompany(models.Model):
    summary = models.TextField(verbose_name="ملخص")
    goals = models.TextField(verbose_name="الأهداف")
    mission = models.TextField(verbose_name="المهمة")
    vision = models.TextField(verbose_name="الرؤية")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف")
    link_to_app = models.URLField(verbose_name="رابط التطبيق")

    def save(self, *args, **kwargs):
        if AboutCompany.objects.exists() and not self.pk:
            raise ValueError("لا يُسمح إلا بمثال واحد فقط لمعلومات الشركة.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return "إعدادات معلومات الشركة"

    class Meta:
        verbose_name = "معلومات حول الشركة"
        verbose_name_plural = "معلومات حول الشركة"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المقال")
    body = models.TextField(verbose_name="المحتوى")
    author = models.CharField(max_length=100, verbose_name="المؤلف")
    release_date = models.DateField(verbose_name="تاريخ النشر")
    plants = models.ManyToManyField(Plant, verbose_name="النباتات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقال"
        verbose_name_plural = "مقالات"


class NewsItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الخبر")
    body = models.TextField(verbose_name="المحتوى")
    publish_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "أخبار"
