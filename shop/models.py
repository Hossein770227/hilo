from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(_("name"), max_length=100)
    slug = models.SlugField(max_length=150, unique=True,allow_unicode=True, blank=True)
    is_active= models.BooleanField(_("is active"))
    description = models.TextField(_("description"), null= True, blank=True)
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
            return self.name
    


class Product(models.Model):
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(_("slug"), unique=True)
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(_("image"), upload_to='images/')
    price_main = models.PositiveIntegerField(_("price"))
    price_with_discount = models.PositiveIntegerField(_("price with discount"), blank=True, null=True)
    amount = models.IntegerField(_("amount"), validators=[MinValueValidator(1)])
    date_time_added = models.DateTimeField(_("date time added"), auto_now_add=True)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])
    

    def clean(self):
       super().clean()
       if self.price_with_discount and self.price_with_discount >= self.price_main:
            raise ValidationError(_("discount price must be less than original price"))

    def __str__(self):
        return self.title