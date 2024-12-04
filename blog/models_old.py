from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import AbstractUser, User
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=100, unique=True, verbose_name='Url slug')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    posted_by = models.CharField(max_length=100, verbose_name='Кем добавлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    tag = models.ManyToManyField('Tags', verbose_name='Тэг', blank=True)
    comment = models.ForeignKey('Comment', verbose_name='Комментарий', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_news', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=100, unique=True, verbose_name='category_url_slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']

class Tags(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=100, unique=True, verbose_name='tag_url_slug')

    def get_absolute_url(self):
        return reverse('news_by_tag', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Comment(models.Model):
    user_created_comment = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    post_of_comment = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    comment_content = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(auto_now_add=True)
    comm_to_repl = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    like_count = models.IntegerField(verbose_name='Количество лайков', default=0)
    likes = models.ManyToManyField(User, blank=True, null=True, verbose_name='лайки')



    #def get_absolute_url(self):
    #    return reverse('single_news', kwargs={'slug': self.post_of_comment.slug})

    class Meta:
        ordering = ['-created']

#class Like(models.Model):
#    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
#    post = models.ForeignKey(Post, related_name='post_of_like', on_delete=models.CASCADE)
#    comment = models.ForeignKey(Comment, related_name='comment_to_like', on_delete=models.CASCADE, default=None)

