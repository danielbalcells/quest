from django.db import models


class Question(models.Model):

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'<Question(text="{self.text}")>'
