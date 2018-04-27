from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Board(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('custom.User')
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.title

class BoardComment(models.Model):
    board = models.ForeignKey('board.Board', related_name='board_comments')
    author = models.ForeignKey('custom.User')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:10]