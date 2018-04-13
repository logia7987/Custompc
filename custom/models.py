from django.db import models

# Create your models here.
class Hardware(models.Model):
    HARDWARE_KIND_CHOICE =(
        ('CPU','CPU'),
        ('BRD','Board'),
        ('RAM','RAM'),
        ('VGA','VGA'),
        ('POW','Power'),
        ('HDD','HDD'),
        ('SSD','SSD'),
        ('ODD','ODD'),
    )
    hardware_kind = models.CharField(
        max_length=3,
        choices=HARDWARE_KIND_CHOICE
    )
    name = models.CharField(max_length=100)
    option = models.TextField()

    def __str__(self):
        return self.name

class Compa(models.Model):
    comp_mode = models.CharField(max_length=100)
    hardware = models.ManyToManyField(Hardware)

    def __str__(self):
        return self.comp_mode

class Custom(models.Model):
    user = models.ForeignKey('auth.User')
    create_date = models.DateTimeField(auto_now_add=True)
    cpu = models.ForeignKey(Hardware,null=True,blank=True,related_name='cpu')
    board = models.ForeignKey(Hardware, null=True, blank=True,related_name='board')
    ram = models.ForeignKey(Hardware, null=True, blank=True,related_name='ram')
    vga = models.ForeignKey(Hardware, null=True, blank=True,related_name='vga')
    power = models.ForeignKey(Hardware, null=True, blank=True,related_name='power')
    hdd = models.ForeignKey(Hardware, null=True, blank=True,related_name='hdd')
    ssd = models.ForeignKey(Hardware, null=True, blank=True,related_name='ssd')
    odd = models.ForeignKey(Hardware, null=True, blank=True, related_name='odd')
    text = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.text[:30]