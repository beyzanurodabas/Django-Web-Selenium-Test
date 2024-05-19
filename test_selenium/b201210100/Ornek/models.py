from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='b201210100/static/assets/blog_images') 
    categories = models.CharField(max_length=200) 
    date = models.DateField()
    description = models.TextField()
    read_more_link = models.URLField()

    def __str__(self):
        return self.title
    
class Industry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='b201210100/static/assets/industries_images')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog_post.title}"
    
class CommentIndustry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    industry_post = models.ForeignKey(Industry, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.industry_post.title}"
