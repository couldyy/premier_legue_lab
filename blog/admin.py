from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ( 'is_analyst', 'is_default_user')}),  # Include custom fields
    )
    list_display = ('email', 'username', 'is_active', 'is_admin', 'is_superuser', 'is_staff', 'is_analyst', 'is_default_user', 'first_name', 'last_name', 'password')
    #fields = ('email', 'username', 'date_joined', 'last_login', 'is_active', 'is_admin', 'is_superuser', 'is_staff', 'is_analyst', 'is_default_user', 'first_name', 'last_name', 'password')
    readonly_fields = ( 'date_joined', 'last_login')
    

class IssueStatusAdmin(admin.ModelAdmin):
    list_display = ('status_description',) 
    fields = ('status_description',) 


class IssueTicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'issue_description', 'status')
    #list_display = ('user', 'issue_description')
    list_display_links = ('user',)
    fields = ('get_user', 'issue_description', 'status')
#    fields = ('get_user', 'issue_description')
    readonly_fields = ('get_user',)

    def get_user(self, obj):
        user_obj = User.objects.raw("SELECT * FROM `blog_user` WHERE id=%s LIMIT 1", [obj.user]) 
        for u in user_obj:
            return u.username

    

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Data
        fields = '__all__'
        #fields = ( 'title', 'content', 'photo', 'posted_by')  

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    #prepopulated_fields = {"id": ("id",)}
    list_display = ('title', 'created_at', 'updated_at', 'get_posted_by_user', 'get_photo', 'views')
    list_display_links = ('title',)
    #list_filter = ('category', 'tag')
    fields = ('title', 'content', 'photo', 'get_photo', 'created_at', 'get_posted_by_user', 'views')
    readonly_fields = ('views', 'created_at', 'get_photo', 'get_posted_by_user')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe((f'<img src="{obj.photo.url}" width=75>'))

    def get_posted_by_user(self, obj):
        user_obj = User.objects.raw("SELECT * FROM `blog_user` WHERE id=%s LIMIT 1", [obj.posted_by]) 
        for u in user_obj:
            return u.username

    def save_model(self, request, obj, form, change):
        obj.posted_by = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.has_perm('blog.add_data')

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('blog.change_data')

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('blog.delete_data')

    def has_view_permission(self, request, obj=None):
        # You can allow or disallow view access here
        return True

    get_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"id": ("title",)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"id": ("title",)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class CommentAdmin(admin.ModelAdmin):
    #list_display = ('user_created_comment', 'comment_content', 'post_of_comment', 'comm_to_repl', 'like_count')
    #list_display_links = ('user_created_comment', 'comment_content', 'post_of_comment', 'comm_to_repl', 'like_count')
    #fields = ('user_created_comment', 'comment_content', 'post_of_comment', 'comm_to_repl', 'like_count', 'likes')
    list_display = ('user', 'post', 'created_at', 'comment_text')
    list_display_links = ('user', 'post', 'created_at', 'comment_text')
    fields = ('user', 'post', 'created_at', 'comment_text')



admin.site.register(Data, PostAdmin)
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Tags, TagsAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(IssueTicket, IssueTicketAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(IssueStatus, IssueStatusAdmin)
