from django.db import models


class Question(models.Model):

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    linked_questions = models.ManyToManyField(
        'self',
        through='QuestionLink',
        through_fields=('source', 'target'),
        symmetrical=False)

    class Meta:
        db_table = 'question'

    def __repr__(self):
        return f'<Question(id={self.id}, text="{self.text}")>'

    def __str__(self):
        return self.text


class QuestionLink(models.Model):

    source = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='source')
    target = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='target')

    class Meta:
        db_table = 'question_link'

    def __repr__(self):
        return (
            f'<QuestionLink('
            f'id={self.id}, '
            f'source="{self.source}", '
            f'target="{self.target}")>'
        )
