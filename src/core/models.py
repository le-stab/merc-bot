from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.utils.translation import gettext_lazy as _


class Provider(models.Model):
    class ContentType(models.TextChoices):
        AUDIO = 'a', _('Audio')
        VIDEO = 'v', _('Video')
        BOOK = 'b', _('Book')
    name = models.CharField(max_length=80, null=True, blank=True)
    content_type = models.CharField(max_length=1, choices=ContentType.choices, null=True, blank=True)
    photo_logo = models.ImageField(upload_to="images", null=True, blank=True, verbose_name='Logo')
    photo_product = models.ImageField(upload_to="images", null=True, blank=True, verbose_name='Product Box')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductProviderTpl(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    title_css = models.CharField(max_length=100, null=True, blank=True)
    description_css = models.CharField(max_length=100, null=True, blank=True)
    toc_css = models.CharField(max_length=100, null=True, blank=True)
    duration_css = models.CharField(max_length=100, null=True, blank=True)
    author_css = models.CharField(max_length=100, null=True, blank=True)
    photo_css = models.CharField(max_length=100, null=True, blank=True)
    language_css = models.CharField(max_length=100, null=True, blank=True)
    category_css = models.CharField(max_length=100, null=True, blank=True)
    tags_css = models.CharField(max_length=100, null=True, blank=True)
    student_count_css = models.CharField(max_length=100, null=True, blank=True)
    reviews_count_css = models.CharField(max_length=100, null=True, blank=True)
    reviews_top_5_css = models.CharField(max_length=100, null=True, blank=True)
    year_css = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductFromProvider(models.Model):
    class Languages(models.TextChoices):
        ES = 'es', _('Espanol')
        EN = 'en', _('Ingles')
    provider = models.ForeignKey(Provider, on_delete=SET_NULL, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=SET_NULL, null=True, blank=True)
    language = models.CharField(max_length=2, choices=Languages.choices, null=True, blank=True, default='es')
    duration = models.CharField(max_length=200, null=True, blank=True)
    toc = models.TextField(max_length=200, null=True, blank=True, verbose_name='Table of Contents')
    photo_product = models.ImageField(upload_to="images", null=True,  blank=True, verbose_name='Product photo')
    video_yt = models.URLField(max_length=200, null=True, blank=True, verbose_name='YT Video')
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    student_count = models.IntegerField(null=True, blank=True)
    review_count = models.IntegerField(null=True, blank=True)
    review_top5 = models.TextField(max_length=200, null=True, blank=True, verbose_name='Reviews (Top 5)')
    year = models.DateField(null=True, blank=True, default='2020')
    url = models.URLField(max_length=350, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MLCategory(models.Model):
    name = models.CharField(max_length=160, null=True, blank=True)
    ml_id = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name


class MLDescriptionTpl(models.Model):
    name = models.CharField(max_length=160, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class MyProduct(models.Model):

    class MLListingType(models.TextChoices):
        GOLD_PRO = 'gold_pro', _('Premium')
        GOLD_PREMIUM = 'gold_premium', _('Oro Premium')
        CLASICA = 'gold_special', _('Clasica')
        GOLD = 'gold', _('Oro')
        SILVER = 'silver', _('Plata')
        BRONZE = 'bronze', _('Bronce')
        FREE = 'free', _('Gratuita')

    class MLStatus(models.TextChoices):
        ACTIVE = 'active', _('Active')
        PAUSED = 'paused', _('Paused')

    product = models.ForeignKey(ProductFromProvider, on_delete=models.CASCADE, null=True, blank=True)
    ml_decription_tpl = models.ForeignKey(MLDescriptionTpl, on_delete=SET_NULL, null=True, blank=True, verbose_name='Description Tpl')
    ml_listing_type = models.CharField(max_length=15, choices=MLListingType.choices, null=True, blank=True, default='gold_special', verbose_name='Listing Type')
    ml_view_count = models.IntegerField(null=True, blank=True, verbose_name='# Views')
    ml_sold_count = models.IntegerField(null=True, blank=True, verbose_name='# Sold')
    ml_messages = models.IntegerField(null=True, blank=True, verbose_name='# Messages')
    ml_questions = models.IntegerField(null=True, blank=True, verbose_name='# Questions')
    my_status = models.CharField(max_length=15, choices=MLStatus.choices, null=True, blank=True, default='active', verbose_name='Status')
    ml_status = models.CharField(max_length=15, choices=MLStatus.choices, null=True, blank=True, default='active', verbose_name='ML Status')
    ml_id = models.CharField(max_length=100, null=True, blank=True, verbose_name='ML Id')
    ml_category = models.ForeignKey(MLCategory, on_delete=SET_NULL, null=True, blank=True, verbose_name='ML Category')
    ml_lowest_price = models.IntegerField(null=True, blank=True, verbose_name='ML Lowest Price')
    available_quantity = models.IntegerField(null=True, blank=True, default=999)
    remote_url_file = models.URLField(max_length=350, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product


# TO DO:
# Orders CLASS
# - Will be triggered bu webhook
# - enables: order_id, order_status, order_messages
# class MLDeliveryStatus(models.TextChoices):
#     PENDING = 'pending', _('Pending')
#     DELIVERED = 'delivered', _('Delivered')
#     RETURNED = 'returned', _('Returned')
