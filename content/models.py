from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.shortcuts import reverse

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(unique=True, editable=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title', )
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.lower().replace('ı', 'i'))
        try:
            self.validate_unique()
        except:
            self.slug += f'-{self.pk}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.title} (yazar: {self.author.username})'
    
    def get_absolute_url(self):
        return reverse('content:entry_detail', kwargs={'slug': self.slug})

