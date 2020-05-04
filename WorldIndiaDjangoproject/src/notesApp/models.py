from django.db import models

# Create your models here.
class Notes(models.Model):
    title              = models.CharField(max_length=120)#max-field required
    content            = models.TextField(blank=True,null=False)
    createdDate        = models.DateTimeField('Created')
    modifiedDate       = models.DateTimeField('Modified')
    def __repr__ (self):
        return '<Note %s>' % self.id

    def __str__ (self):
        return self.title