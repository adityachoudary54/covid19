from django.db import models

class homePageData(models.Model):
    title              = models.CharField(max_length=120)#max-field required
    content            = models.TextField(blank=True,null=False)
    contentType        = models.CharField(max_length=120)
    createdDate        = models.DateTimeField('Created',auto_now_add=True)
    modifiedDate       = models.DateTimeField('Modified',auto_now=True)
    def __str__ (self):
        return self.title