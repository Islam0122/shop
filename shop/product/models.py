import uuid

from django.db import models
from django.utils.text import slugify

class Status(models.TextChoices):
    draft = "draft", "Draft"
    active = "active", "Active"
    out_of_stock = "out_of_stock", "Out Of Stock"
    archived = "archived", "Archived"

class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    title = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.draft)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    tags = models.ManyToManyField(Tag, related_name='products',blank=True)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
