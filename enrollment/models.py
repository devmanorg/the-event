from django.db import models


class Application(models.Model):
    contact_phone = models.CharField(max_length=20)

    ticket_type = models.CharField(max_length=20, db_index=True, choices=(
        ('standard-access', 'Standard Access'),
        ('pro-access', 'Pro Access'),
        ('premium-access', 'Premium Access'),
    ))

    confirmed = models.BooleanField(default=False, db_index=True)


class Participant(models.Model):

    application = models.ForeignKey(Application, related_name='participants', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
