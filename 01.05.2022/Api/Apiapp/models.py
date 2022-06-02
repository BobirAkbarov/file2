from django.db import models

class Mailing_list(models.Model):
    date_create = models.DateField(auto_now_add=True)
    text_message = models.TextField()
    custom = models.ManyToManyField('Custom', related_name='Customs')
    date_end = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date_create} -> {self.text_message} -> {self.custom} -> {self.date_end}'

class Custom(models.Model):
    number = models.CharField(max_length=13)
    code = models.CharField(max_length=20)
    tag = models.CharField(max_length=50)
    hour = models.CharField(max_length=30)

    def __str__(self):
        return f'Text: {self.number} -> {self.code} -> {self.tag} -> {self.hour}'

class Message(models.Model):
    date_create = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
    user = models.ForeignKey("Custom", related_name="Custom", on_delete=models.CASCADE)
    mailing_list = models.ForeignKey('Mailing_list', related_name='Mailing_lists', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date_create} -> {self.status} -> {self.user} -> {self.mailing_list}'

