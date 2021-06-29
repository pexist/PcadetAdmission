from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


# security login activity log.
class Login_log(models.Model):
    id = models.AutoField(primary_key=True, null=False)  # applicant for admission process, ID autogen
    id_13 = models.CharField(max_length=13, null=True, help_text="หมายเลขบัตรประจำตัวประชาชน")  # Thai id number
    login_Date = models.DateTimeField(auto_now=True)  # Keep access datetime
    ip_address = models.GenericIPAddressField()
    # todo : keep all record that logged in.

    def __str__(self):
        return self.ID13

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Applicant(models.Model):
    AID = models.ForeignKey(Login_log, on_delete=models.CASCADE)
    TID = models.CharField(max_length=10, null=True)
    EXID = models.CharField(max_length=5, null=True)
    ID13 = models.CharField(max_length=13, null=True)
    BDD = models.DateField()
    FirstName = models.CharField(max_length=13, null=True)
    LastName = models.CharField(max_length=13, null=True)
    Nation = models.CharField(max_length=1, null=True)
    Religion = models.CharField(max_length=11, null=True)
    LProvice = models.CharField(max_length=2, null=True)
    Asec = models.CharField(max_length=1, null=True)
    Area = models.CharField(max_length=2, null=True)
    QUA = models.CharField(max_length=1, null=True)
    EducationStatus = (
        ('m4', 'ม4'),
        ('m5', 'ม5'),
        ('m6', 'ม6'),
        ('mx', 'อื่นๆ'),
    )
    education = models.CharField(max_length=2, choices=EducationStatus, default='mx')

    SchPro = models.CharField(max_length=2, null=True)
    SchName = models.CharField(max_length=100, null=True)
    GPA = models.CharField(max_length=4, null=True)
    S_tel = models.CharField(max_length=10, null=True)
    F_FName = models.CharField(max_length=50, null=True)
    F_LName = models.CharField(max_length=50, null=True)
    F_ID13 = models.CharField(max_length=13, null=True)
    F_Stat = models.CharField(max_length=1, null=True)
    F_Pro = models.CharField(max_length=2, null=True)
    F_Minis = models.CharField(max_length=2, null=True)
    F_Tel = models.CharField(max_length=10, null=True)
    M_FName = models.CharField(max_length=50, null=True)
    M_LName = models.CharField(max_length=50, null=True)
    M_ID13 = models.CharField(max_length=13, null=True)
    M_Stat = models.CharField(max_length=1, null=True)
    M_Pro = models.CharField(max_length=2, null=True)
    M_Minis = models.CharField(max_length=2, null=True)
    M_Tel = models.CharField(max_length=10, null=True)
    AD1 = models.CharField(max_length=1, null=True)
    AD2 = models.CharField(max_length=1, null=True)
    AD3 = models.CharField(max_length=1, null=True)
    AD4 = models.CharField(max_length=1, null=True)
    AD5 = models.CharField(max_length=1, null=True)
    STAT = models.CharField(max_length=2, null=True)
    DateREC = models.DateTimeField(null=True)
    DatePrintForm = models.DateTimeField(null=True)
    DatePAY = models.DateTimeField(null=True)

    # school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
