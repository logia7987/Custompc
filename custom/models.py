from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_member = models.BooleanField(default=True)

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
    hard_thumbnail = ProcessedImageField(
        upload_to='hardware',
        processors=[Thumbnail(55,55)],
        format='JPEG',
        options={'quality':60},
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def hit(self):
        hard_count = 0;
        if self.hardware_kind == "CPU":
            req = Custom.objects.filter(cpu=self).count();
        elif self.hardware_kind == "BRD":
            req = Custom.objects.filter(board=self).count();
        elif self.hardware_kind == "RAM":
            req = Custom.objects.filter(ram=self).count();
        elif self.hardware_kind == "VGA":
            req = Custom.objects.filter(vga=self).count();
        elif self.hardware_kind == "POW":
            req = Custom.objects.filter(power=self).count();
        elif self.hardware_kind == "HDD":
            req = Custom.objects.filter(hdd=self).count();
        elif self.hardware_kind == "SSD":
            req = Custom.objects.filter(ssd=self).count();
        elif self.hardware_kind == "ODD":
            req = Custom.objects.filter(odd=self).count();
        some_hard = Hardware.objects.filter(hardware_kind=self.hardware_kind)
        for i in some_hard:
            if self.hardware_kind == "CPU":
                hard_count = hard_count + Custom.objects.filter(cpu=i.id).count();
            elif self.hardware_kind == "BRD":
                hard_count = hard_count + Custom.objects.filter(board=i.id).count();
            elif self.hardware_kind == "RAM":
                hard_count = hard_count + Custom.objects.filter(ram=i.id).count();
            elif self.hardware_kind == "VGA":
                hard_count = hard_count + Custom.objects.filter(vga=i.id).count();
            elif self.hardware_kind == "POW":
                hard_count = hard_count + Custom.objects.filter(power=i.id).count();
            elif self.hardware_kind == "HDD":
                hard_count = hard_count + Custom.objects.filter(hdd=i.id).count();
            elif self.hardware_kind == "SSD":
                hard_count = hard_count + Custom.objects.filter(ssd=i.id).count();
            elif self.hardware_kind == "ODD":
                hard_count = hard_count + Custom.objects.filter(odd=i.id).count();
        top = hard_count/100*85
        if req >= top:
            return 'HIT'
        else:
            return ''

class Compa(models.Model):
    comp_mode = models.CharField(max_length=100)
    hardware = models.ManyToManyField(Hardware)

    def __str__(self):
        return self.comp_mode

    def cleaner(self):
        if self.hardware == None:
            self.delete()

class Custom(models.Model):
    user = models.ForeignKey(User)
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
        if self.text:
            return self.text[:10]
        else:
            return self.user.username

    class Meta:
        ordering = ['-create_date']

class Comment(models.Model):
    custom = models.ForeignKey('custom.Custom', related_name='custom_comments', null=True)
    board = models.ForeignKey('board.Board', related_name='board_comments', null=True)
    author = models.ForeignKey(User)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:10]

