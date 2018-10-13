from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from vault.models import User


class Author(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(null=True, blank=True, upload_to='authors/')

    def __str__(self):
        return self.name

class BookManager(models.Manager):
    def get_recommended(self):
        return self.all()[:3]


class Book(models.Model):
    title = models.CharField(max_length=80)
    authors = models.ManyToManyField(Author)
    date = models.DateField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True, upload_to='covers/')
    objects = BookManager()

    def __str__(self):
        return self.title

class ReviewWriter(models.Model):
    user = models.OneToOneField(User)
    read_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_writer(sender, instance, created, **kwargs):
    if created:
        ReviewWriter.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.reviewwriter.save()


class Review(models.Model):
    rating = models.IntegerField()
    opinion = models.CharField(max_length=1200, blank=True)
    writer = models.ForeignKey(ReviewWriter, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} ({self.rating})"
