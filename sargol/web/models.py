from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=300,unique=True,verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True,verbose_name="آیا نمایش داده شود")
    position = models.IntegerField(verbose_name="پوزیشن")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["position"]
    def __str__(self):
        return self.title
class products(models.Model):
    STATUS_CHOICEC =(('d','پیش ساز'),('p','منتشر شده'),)

    title = models.CharField(max_length=100,verbose_name="عنوان محصول")
    slug = models.SlugField(max_length=300,unique=True,verbose_name="آدرس محصول",default='', blank=True)
    category = models.ManyToManyField(Category,verbose_name="دسته بندی")
    price = models.CharField(max_length=200,verbose_name="قیمت")
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="media",verbose_name="عکس")
    publish = models.DateTimeField(default=timezone.now,null=True,blank=True,verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    upload = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICEC,verbose_name="وضعیت")
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["-publish"]
    def __str__(self):
        return self.title
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

class Articles(models.Model):
    STATUS_CHOICEC =(('d','پیش ساز'),('p','منتشر شده'),)

    title = models.CharField(verbose_name="عنوان مقاله",max_length=300)
    description = models.TextField(verbose_name="متن مقاله")
    category = models.ManyToManyField(Category,verbose_name="دسته بندی")
    status = models.CharField(max_length=1,choices=STATUS_CHOICEC,verbose_name="وضعیت")
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
    def __str__(self):
        return self.title

class Banners(models.Model):
    title = models.CharField(verbose_name="عنوان تغییر", max_length=50)
    category = models.ManyToManyField(Category,verbose_name="دسته بندی",blank=True)
    banner1=models.FileField(verbose_name="بنر یک", upload_to="products/banners/",
        max_length=100,null=True,blank=True)
    banner2=models.FileField(verbose_name="بنر دو", upload_to="products/banners/",
        max_length=100,null=True,blank=True)
    banner3=models.FileField(verbose_name="بنر سه", upload_to="products/banners/",
        max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنر ها"
    def __str__(self):
        return self.title
