
from django.db import models
from django.db.models import CASCADE
from shop.models import Shop

OCCUPATION = [
    (1, "Barber"),
    (2, "Perosnal trainer"),
    (3, "Life coach"),


]
TITLE = [
    (1, "Mr"),
    (2, "Mrs"),
    (3, "Ms"),
    (4, "Dr"),


]
WEEKDAYS = [
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
]


class WorkingHours(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField(default='9:00')
    to_hour = models.TimeField(default='17:30')
    Shop = models.ForeignKey(Shop,on_delete=CASCADE)

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)

    def get_weekday_display(self):
        return self.weekday[0:3]
