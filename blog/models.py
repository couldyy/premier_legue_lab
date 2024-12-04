# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.urls import reverse, reverse_lazy


class CommentLike(models.Model):
    user = models.ForeignKey('blog.User', on_delete=models.SET_NULL, null=True)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments_likes'

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('blog.User', on_delete=models.SET_NULL, related_name='user', null=True)
    post = models.ForeignKey('blog.Data', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment_text = models.CharField(max_length=255)
    comm_to_repl = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    like_count = models.IntegerField(default=0)
    likes = models.ManyToManyField('blog.User', through='CommentLike', blank=True)

    class Meta:
        #managed = False
        db_table = 'Comments'


class Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    posted_by = models.ForeignKey('blog.User', on_delete=models.SET_NULL, null=True, blank=False) 
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    views = models.IntegerField(default=0)
    #category = models.ForeignKey('blog.Category', on_delete=models.PROTECT, verbose_name='Категория')
    #tag = models.ManyToManyField('blog.Tags', verbose_name='Тэг', blank=True)
    comment = models.ForeignKey('blog.Comments', verbose_name='Комментарий', on_delete=models.SET_NULL, null=True, blank=True)
    


    class Meta:
        #managed = False
        ordering = ['-created_at']
        db_table = 'Data'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_news', kwargs={'pk': self.pk})


class IssueTicket(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    user = models.ForeignKey('blog.User', on_delete=models.SET_NULL, null=True)
    data_id = models.ForeignKey('blog.Data', on_delete=models.CASCADE)
    issue_description = models.CharField(max_length=255)
    status = models.ForeignKey('blog.IssueStatus', on_delete=models.SET_NULL, null=True)
 
    class Meta:
        #managed = False
        db_table = 'issue_ticket'

class IssueStatus(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    status_description = models.CharField(max_length=50)

    def __str__(self):
        return self.status_description


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required")
        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_analyst = False
        user.is_admin = False
        user.is_default_user = True
        user.is_superuser = False
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
        )
        user.is_analyst = False
        user.is_admin = True
        user.is_default_user = False
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user



class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=200, verbose_name='email', unique=True)
    username = models.CharField(max_length=200, verbose_name='username', unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
    last_login = models.DateTimeField(auto_now=True, verbose_name='last login')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_analyst = models.BooleanField(default=False)
    is_default_user = models.BooleanField(default=True)
    first_name = models.CharField(max_length=150, verbose_name='First Name')
    last_name = models.CharField(max_length=150, verbose_name='Last Name', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name']

    objects = MyAccountManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_active and (perm in self.get_all_permissions())

    def has_module_perms(self, app_label):
        return True


