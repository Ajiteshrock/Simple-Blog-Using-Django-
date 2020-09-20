from django.db import models
from django.utils import timezone
from django.urls import reverse

# Creating post and comment models
class Post(models.Model):

    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    text = models.TextField()
    create_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
          self.published_date = timezone.now()
          self.save()
          

    def approve_comments(self):
            return self.comments.filter(approved_comment =True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})


class Comments(models.Model):
    post = models.ForeignKey('blogapp.Post',related_name='comments',on_delete=models.CASCADE)
    #this is important that we made post model as a superusser model
    #author is primary key for the post database and foriegn key for comments database
    author = models.CharField(max_length = 200)
    text  = models.TextField()
    create_date= models.DateTimeField(default=timezone.now)
    approved_comment =models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_list')
