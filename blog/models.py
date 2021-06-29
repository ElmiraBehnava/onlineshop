from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _





class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class PostCategory(models.Model):
    name = models.CharField(_('name'), max_length=200, db_index=True)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name =  _('PostCategory')
        verbose_name_plural = _('PostCategories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:post_list_by_category", args=[self.slug])


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    postcategory = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='blogs', verbose_name=_('category'), blank=True, null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    short_description = RichTextUploadingField(_('short_description'),blank=True, null=True)
    long_description = RichTextUploadingField(_('long_description'),blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])




class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'



    



