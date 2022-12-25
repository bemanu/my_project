from django.db import models
from django.db.models import CASCADE


class WorkingHours(models.Model):
    start_time = models.TimeField('Start time')
    end_time = models.TimeField('End time')

    def __str__(self):
        return f'%s - %s' %(self.start_time,self.end_time)

class Barbershop(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=2000)
    address1 = models.CharField("Address line 1",max_length=1024, )
    address2 = models.CharField("Address line 2", max_length=1024,)
    post_code = models.CharField("Postal code", max_length=12,)
    city = models.CharField( "City",max_length=1024,)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    open_hours = models.ForeignKey(WorkingHours, on_delete=CASCADE)

    def __str__(self):
        return "%s \n %s \n %s \n %s \n %s \n %s  %s \n mobile: %s \n phone: %s " %(self.name,self.bio, self.address1, self.address2, self.post_code,self.city,self.mobile,self.phone,self.email)


class Barbers(models.Model):
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    barbershop = models.ForeignKey(Barbershop, on_delete=CASCADE)
    working_hours = WorkingHours()
