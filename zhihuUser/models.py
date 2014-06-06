from django.db import models

# Create your models here.
class ZhihuUser(models.Model):
    username = models.CharField(max_length=256, db_index=True)
    name = models.CharField(max_length=256)
    answers = models.IntegerField(default=0)
    questions = models.IntegerField(default=0)
    edits = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    essays = models.IntegerField(default=0)
    bookmarks = models.IntegerField(default=0)
    location = models.CharField(max_length=256)

class Question(models.Model):
    token = models.IntegerField(default=0, db_index=True)
    title = models.CharField(max_length=256)
    asker = models.ForeignKey(ZhihuUser)
    url = models.URLField(max_length=500)
    watchers = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)

class Answer(models.Model):
    token = models.IntegerField(default=0, db_index=True)
    question = models.ForeignKey(Question)
    url = models.URLField(max_length=500)
    answerer = models.ForeignKey(ZhihuUser)
    upvotes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
