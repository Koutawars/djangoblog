from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    publishedDate = models.DateField(auto_now_add=True) 
    def __str__(self):
        return "[" + str(self.id) +  "] " + self.title
class Comment(models.Model):
    username = models.CharField(max_length=50)
    content = models.TextField()
    publishedDatetime = models.DateTimeField(auto_now_add=True) 
    entryId = models.ForeignKey(Entry, on_delete=models.CASCADE) 
    class Meta:
        ordering = ['-publishedDatetime']
    def __str__(self):
        return "[" + self.username +  "] " + self.content[:70]