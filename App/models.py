from django.db import models

# Create your models here.
class Appuser(models.Model):
    id=models.AutoField(primary_key=True)
    userId=models.CharField(max_length=32);
    image=models.ImageField(blank=True);
    message=models.CharField(max_length=300)
    busyType=models.CharField(max_length=32);
    def __str__(self):
        return str(self.id)+" "+self.userId+" "+self.message;
class Schedule(models.Model):
    user=models.OneToOneField(Appuser,blank=False);
    name1=models.CharField(max_length=32);
    name1StartTime=models.CharField(max_length=32);
    name1EndTime=models.CharField(max_length=32);

    name2 = models.TextField(max_length=32);
    name2StartTime = models.CharField(max_length=32);
    name2EndTime = models.CharField(max_length=32);

    name3 = models.CharField(max_length=32);
    name3StartTime = models.CharField(max_length=32);
    name3EndTime = models.CharField(max_length=32);
    def __str__(self):
        return self.user.userId;





