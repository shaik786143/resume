from django.db import models
STATE_CHOICE=(
    ('aP', 'ap'),
    ('andaman','andaman' ),
    ('assam', 'assam'),
    ('chandigar', 'chandigar'),
    ('bihar', 'bihar'),
    ('westbengal', 'westbengal'),
    ('delhi', 'delhi'),
    ('gova', 'gova'),
    ('gujarat', 'gujarat'),
    ('kerala', 'kerala'),
    ('up', 'up'),
   
)

# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=100)
    mobile=models.PositiveBigIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)

