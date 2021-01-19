from django.db import models


class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_content = models.CharField(max_length=500)

    def __str__(self):
        return self.news_title+", "+self.news_content


class NewsComments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    comments = models.CharField(max_length=250)

    def __str__(self):
        return str(self.news)+", "+self.email+", "+self.comments