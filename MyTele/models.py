from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(default='Text komments')

    def __str__(self):
        return u' name:{0} address:{1} '.format(self.name, self.address)

class AddressBookEntry(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, default='example@mail.ru')
    komment = models.TextField(default='Komment')

    def __str__(self):
        return u' name:{0} surname:{1} tel:{2}) email:{3} komment:{4}'.format(self.name,
                                                                              self.surname,
                                                                              self.telephone,
                                                                              self.email,
                                                                              self.komment[0:50])
