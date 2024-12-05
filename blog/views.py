from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.http import HttpResponse
from django.db.models import F
from django.core.mail import send_mail
from .forms import *
from django.db import connection

# Create your views here.

class HomePage(ListView):
    model = Data
    template_name = 'blog/index.html'
    context_object_name = 'post'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        request = self.request
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        if not request.user.is_anonymous:
            if request.user.is_admin:
#            context['issues_count'] = IssueTicket.objects.filter(status=0).count
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM `issue_ticket`")
                    # get a single line from the result
                    row = cursor.fetchone()
                    # get the value in the first column of the result (the only column)
                    all_issues_count = row[0]
                context['all_issues_count'] = all_issues_count

            context['user_sent_issues'] = IssueTicket.objects.raw("SELECT * FROM `issue_ticket` WHERE  user_id=%s", [request.user.id])
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM `issue_ticket` WHERE   user_id=%s", [request.user.id])
                row = cursor.fetchone()
                user_issues_count = row[0]
            context['user_issues_count'] = user_issues_count
        return context

#class GetCategory(ListView):
#    # extra_context = {'categories': Category.objects.all()}
#    model = Data
#    template_name = 'blog/category.html'
#    context_object_name = 'post'
#    paginate_by = 4
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
#        return context
#
#    def get_queryset(self):
#        return Data.objects.filter(category__slug=self.kwargs['slug'])

#(status_id=1 OR status_id=2)

class ShowUserIssuesList(ListView):
    model = IssueTicket
    template_name = 'blog/issues_list.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        request = self.request
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        if not request.user.is_anonymous:
            if request.user.is_admin:
#            context['issues_count'] = IssueTicket.objects.filter(status=0).count
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM `issue_ticket`")
                    # get a single line from the result
                    row = cursor.fetchone()
                    # get the value in the first column of the result (the only column)
                    all_issues_count = row[0]
                context['all_issues_count'] = all_issues_count

            context['user_sent_issues'] = IssueTicket.objects.raw("SELECT * FROM `issue_ticket` WHERE   user_id=%s", [request.user.id])
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM `issue_ticket` WHERE   user_id=%s", [request.user.id])
                row = cursor.fetchone()
                user_issues_count = row[0]
            context['user_issues_count'] = user_issues_count
        return context

#    context = {"title": "My issues reports",
#               "issues_count": admin_issues_count,
#               "user_sent_issues": user_sent_issues,
#               "user_issues_count": user_issues_count,
#               }



class ShowSingleNews(DetailView):
    model = Data
    template_name = 'blog/single_news.html'
    context_object_name = 'post'

    form = CommentForm

    #def post(self, request, *args, **kwargs):
    #    form = CommentForm(request.POST)
    #    if form.is_valid():
    #        post = self.get_object()
    #        form.instance.user_created_comment = request.user
    #        form.instance.post_of_comment = post
    #        form.instance.
    #        commrepl = request.POST.get("commentID")
    #        form.instance.comm_to_repl_id = commrepl
    #        form.save()
    #    else:
    #        print("some error with form happened")
    #        print(form.errors.as_data())

    #    return redirect(reverse("single_news", kwargs={
    #        "pk": self.get_object().id,
    #    }))


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Data.objects.get(id=self.kwargs['pk'])
        context['form'] = self.form
        context['comments'] = Comments.objects.filter(post=self.get_object(), comm_to_repl=None)
        request = self.request
        if not request.user.is_anonymous:
            if request.user.is_admin:
#            context['issues_count'] = IssueTicket.objects.filter(status=0).count
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM `issue_ticket`")
                    # get a single line from the result
                    row = cursor.fetchone()
                    # get the value in the first column of the result (the only column)
                    all_issues_count = row[0]
                context['all_issues_count'] = all_issues_count

            context['user_sent_issues'] = IssueTicket.objects.raw("SELECT * FROM `issue_ticket` WHERE   user_id=%s", [request.user.id])
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM `issue_ticket` WHERE   user_id=%s", [request.user.id])
                row = cursor.fetchone()
                user_issues_count = row[0]
            context['user_issues_count'] = user_issues_count
        

        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()

        return context



#class GetNewsByTag(ListView):
#    template_name = 'blog/index.html'
#    context_object_name = 'post'
#    paginate_by = 4
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['title'] = 'Новости по тегу: ' + str(Tags.objects.get(slug=self.kwargs['slug']))
#        return context
#
#    def get_queryset(self):
#        return Data.objects.filter(tag__slug=self.kwargs['slug'])


class Search(ListView):
    template_name = 'blog/search_posts.html'
    context_object_name = 'post'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        request = self.request
        if not request.user.is_anonymous:
            if request.user.is_admin:
#            context['issues_count'] = IssueTicket.objects.filter(status=0).count
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM `issue_ticket`")
                    # get a single line from the result
                    row = cursor.fetchone()
                    # get the value in the first column of the result (the only column)
                    all_issues_count = row[0]
                context['all_issues_count'] = all_issues_count

            context['user_sent_issues'] = IssueTicket.objects.raw("SELECT * FROM `issue_ticket` WHERE user_id=%s", [request.user.id])
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM `issue_ticket` WHERE user_id=%s", [request.user.id])
                row = cursor.fetchone()
                user_issues_count = row[0]
            context['user_issues_count'] = user_issues_count
        return context

    def get_queryset(self):
        return Data.objects.filter(title__icontains=self.request.GET.get('s'))

def registration(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('home')
    else:
        form = CreateUser()
    return render(request, 'blog/registration.html', {"form": form, "title": 'Sign in'})


def loginn(request):
    if request.method == 'POST':
        form = LoginUser(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            account = authenticate(username=username, password=password)
            if account:
                login(request, account)
                return redirect('home')
    else:
        form = LoginUser()
    return render(request, 'blog/login.html', {"form": form, "title": 'Login'})

def logoutt(request):
    logout(request)
    return redirect('home')



def like(request, post_id, comment_id):
    result = ''
    post = Data.objects.get(id=post_id)
    comment = Comments.objects.get(id=comment_id)
    user = request.user
    if user in comment.likes.all():
        comment.likes.remove(user)
        comment.like_count -= 1
        result = Comments.like_count
        comment.save()
        comment.refresh_from_db()
    else:
        comment.likes.add(user)
        comment.like_count += 1
        comment.save()
        comment.refresh_from_db()
    return redirect(reverse("single_news", kwargs={
        "pk": post.id,
    }))

def submit_comment(request, pk):
    post_comment = Data.objects.get(pk=pk)
    user = request.user
    content = request.POST.get('comment_content')
    commrepl_id = request.POST.get("commentID")
    if commrepl_id == None:
        commrepl = None
    else :
        commrepl = Comments.objects.get(pk=commrepl_id)
    comment = Comments.objects.create(user=user, post=post_comment, comment_text=content, comm_to_repl=commrepl)

    comment.save()
    comment.refresh_from_db()
    page = request.META.get('HTTP_REFERER')
    return redirect(page)


def submit_issue(request, pk):
    post_issue = Data.objects.get(pk=pk)
    user = request.user
    content = request.POST.get('issue_description')
    status = IssueStatus.objects.get(pk=1)
#    commrepl_id = request.POST.get("commentID")
    issue = IssueTicket.objects.create(user=user, data_id=post_issue, issue_description=content, status=status) 

    issue.save()
    issue.refresh_from_db()
    page = request.META.get('HTTP_REFERER')
    return redirect(page)
