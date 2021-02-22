from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyProduct)
admin.site.register(ProductFromProvider)
admin.site.register(ProductProviderTpl)
admin.site.register(Provider)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(MLDescriptionTpl)
admin.site.register(MLCategory)
