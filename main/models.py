from django.db import models

# Create your models here.
class Member(models.Model):
    TEAMS = (
            ('Leads', 'Leads'),
            ('Software', 'Software'),
            ('Hardware', 'Hardware'),
            ('Research', 'Research'),
            ('Outreach', 'Outreach'),
    )

    YEARS = (
            ('Freshman', 'Freshman'),
            ('Sophomore', 'Sophomore'),
            ('Junior', 'Junior'),
            ('Senior', 'Senior'),
    )

    name = models.CharField(max_length=200, null = True)
    profile_pic = models.ImageField(upload_to='static/images', null = True, blank = True)
    lead = models.BooleanField(default=False)
    team = models.CharField(max_length = 200, null = True, choices=TEAMS)
    major = models.CharField(max_length=200, null = True)
    minor = models.CharField(max_length=200, null = True, blank = True)
    year = models.CharField(max_length = 200, null = True, choices=YEARS)
    linkedin = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return str(self.name)
