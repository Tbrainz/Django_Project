from django.db import models
from django.contrib.auth.models import User

# Create your models here.
gen = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)
marital_status = (
    ('SINGLE', 'SINGLE'),
    ('MARRIED', 'MARRIED')
)

state_of_origin = (
    ('Abia', 'Abia'),
    ('Adamawa', 'Adamawa'),
    ('Akwa Ibom', 'Akwa Ibom'),
    ('Rivers', 'Rivers')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=20)
    DoB = models.DateField()
    gender = models.CharField( max_length =7, choices=gen)
    marital_status = models.CharField(max_length=15, choices=marital_status)
    address = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=11)

    state_of_origin = models.CharField(max_length=10, choices=state_of_origin, default='')
    lga_of_origin = models.CharField(max_length=20, default='')
    year_of_application = models.CharField(max_length=4, default='')
    scheme_name = models.CharField(max_length=10, blank= True, null =True, default='')
    profile_image = models.ImageField(upload_to='profile_pics', default='')
    residential_address = models.CharField(max_length=20, default='')
    state_of_residence = models.CharField(max_length=100, default='')
    lga_of_residence = models.CharField(max_length=100, default='')
    highest_lev_of_edu = models.CharField(max_length=100, default='')
    year_of_graduation = models.CharField(max_length=100, default='')
    id_type = models.CharField(max_length=100, default='')
    id_number = models.CharField(max_length=100, default='')
    uploaded_id_card = models.CharField(max_length=100, default='')
    bvn = models.CharField(max_length=100, default='')
    account_num = models.CharField(max_length=100, default='')
    account_name = models.CharField(max_length=100, default='')
    bank_name = models.CharField(max_length=100, default='')



    def __str__(self):
        return f'{self.user}'