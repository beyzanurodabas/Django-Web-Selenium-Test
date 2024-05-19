from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('index.html', views.index, name='index'),
    path('404.html', views.dortyuzdort, name='dortyuzdort'),
    path('about-us.html', views.aboutUs, name='aboutUs'),
    path('awards.html', views.awards, name='awards'),

    path('blog.html', views.blog, name='blog'),
    path('add-blog-post.html', views.add_blog_post, name='add_blog_post'),
    path('blog/<int:pk>/', views.blog_single_post, name='blog_single_post'),
    path('blog/<int:pk>/add_comment/', views.add_comment, name='add_comment'),  # Bu satırı ekleyin
    
    path('industries/<int:pk>/', views.industriesSingleIndustry, name='industriesSingleIndustry'),
    path('industries.html', views.industries, name='industries'),
    path('add-industries.html', views.add_industries, name='add_industries'),
    path('industries/<int:pk>/add_comment/', views.add_comment, name='add_comment'),  # Bu satırı ekleyin

    path('careers.html', views.careers, name='careers'),
    path('case-studies-classic.html', views.caseStudiesClassic, name='caseStudiesClassic'),
    path('case-studies-grid.html', views.caseStudiesGrid, name='caseStudiesGrid'),
    path('case-studies-modern.html', views.caseStudiesModern, name='caseStudiesModern'),
    path('case-studies-single.html', views.caseStudiesSingle, name='caseStudiesSingle'),
    path('coming-soon.html', views.comingSoon, name='comingSoon'),
    path('contact-us.html', views.contantUs, name='contantUs'),
    path('faqs.html', views.faqs, name='faqs'),
    path('home-classic.html', views.homeClassic, name='homeClassic'),
    path('home-modern.html', views.homeModern, name='homeModern'),
 
    path('it-solutions-single.html', views.itSolutionsSingle, name='itSolutionsSingle'),
    path('it-solutions.html', views.itSolutions, name='itSolutions'),
    path('leadership-team.html', views.leadershipTeam, name='leadershipTeam'),
    path('pricing.html', views.pricing, name='pricing'),
    path('request-quote.html', views.requestQuote, name='requestQuote'),
    path('search.html', views.search, name='search'),
    path('why-us.html', views.whyUs, name='whyUs'),
    path('Login.html', views.login,name="login"),
    path('Register.html', views.register,name="register")
]