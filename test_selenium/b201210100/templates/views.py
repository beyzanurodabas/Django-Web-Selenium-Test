from django.shortcuts import render,redirect, get_object_or_404
from Ornek.models import BlogPost,Industry
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Ornek.forms import BlogPostForm,IndustryForm,CommentForm,Comment,CommentIndustry,CommentIndustryForm

def index(request):
    return render(request,'index.html')

def dortyuzdort(request):
    return render(request,'404.html')

def aboutUs(request):
    return render(request,'about-us.html')

def awards(request):
    return render(request,'awards.html')

#-------------------------LOGİN REGİSTER---------------------
def register(request):	
    if request.method =='POST':
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect("Login.html")
    else:
        return render(request,'Register.html')

def login(request):
    if request.method =='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("index.html")
        else:
            return render(request,'Login.html',{'Error':True})
    else:
        return render(request,'Login.html')

#------------------------BLOG------------------------------
def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def blog_single_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(blog_post=blog_post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog_post = blog_post
            comment.save()
            return redirect('blog_single_post', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog-single-post.html', {'blog_post': blog_post, 'comments': comments, 'form': form})

# def add_comment(request, pk):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.blog_post_id = pk  # Assign the blog_post_id to link the comment to the blog post
#             comment.save()
#             return redirect('blog_single_post', pk=pk)  # Redirect to the blog post detail page
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment.html', {'form': form})
from django.contrib import messages
def add_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog_post_id = pk  # Assign the blog_post_id to link the comment to the blog post
            comment.save()
            messages.success(request, 'Yorumunuz başarıyla gönderildi.')  # Başarı mesajı
            return redirect('blog_single_post', pk=pk)  # Gönderildikten sonra blog gönderisinin detay sayfasına yönlendir
        else:
            messages.error(request, 'Lütfen geçerli bir yorum girin.')  # Hata mesajı
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog.html')
    else:
        form = BlogPostForm()
    return render(request, 'add-blog-post.html', {'form': form})


# ----------------------------Industry -----------------------
def industriesSingleIndustry(request, pk):
    industries_post = get_object_or_404(Industry, pk=pk)
    comments = CommentIndustry.objects.filter(industry_post=industries_post)
    if request.method == 'POST':
        form = CommentIndustryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.industry_post = industries_post
            comment.save()
            return redirect('industriesSingleIndustry', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'industries-single-industry.html', {'industries_post': industries_post, 'comments': comments, 'form': form})

def industries(request):
    industries = Industry.objects.all()
    return render(request, 'industries.html', {'industries': industries})

def add_industries(request):
    if request.method == 'POST':
        form = IndustryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('industries.html')
    else:
        form = IndustryForm()
    return render(request, 'add-industries.html', {'form': form})

def careers(request):
    return render(request,'careers.html')

def caseStudiesClassic(request):
    return render(request,'case-studies-classic.html')

def caseStudiesGrid(request):
    return render(request,'case-studies-grid.html')

def caseStudiesModern(request):
    return render(request,'case-studies-modern.html')

def caseStudiesSingle(request):
    return render(request,'case-studies-single.html')

def comingSoon(request):
    return render(request,'coming-soon.html')

def contantUs(request):
    return render(request,'contact-us.html')

def faqs(request):
    return render(request,'faqs.html')

def homeClassic(request):
    return render(request,'home-classic.html')

def homeModern(request):
    return render(request,'home-modern.html')

def itSolutionsSingle(request):
    return render(request,'it-solutions-single.html')

def itSolutions(request):
    return render(request,'it-solutions.html')

def leadershipTeam(request):
    return render(request,'leadership-team.html')

def pricing(request):
    return render(request,'pricing.html')

def requestQuote(request):
    return render(request,'request-quote.html')

def search(request):
    return render(request,'search.html')

def whyUs(request):
    return render(request,'why-us.html')