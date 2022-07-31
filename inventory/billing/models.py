from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# entityid should be a foreign key


class User(AbstractUser):
    name = models.CharField(max_length=15,null=False,default='name')
    email = models.EmailField(max_length=30,unique=True,null=False)
    is_superAdmin = models.BooleanField('Is SuperAdmin',default=False)
    is_entityOwner = models.BooleanField('Is EntityOwner',default=False)
    is_branchManager = models.BooleanField('Is Branch Manager',default=False)
    is_counterManager = models.BooleanField('Is Counter Manager',default=False)
    account_expiry = models.DateField(blank=True, null=True)

    branchName = models.CharField(max_length=50, null= True)

    entityName = models.CharField(max_length=50, null= True)
    entityID = models.CharField(max_length=50, null= True)
    branchID = models.CharField(max_length=50, null=True)
    branchCount = models.IntegerField(default = 1, blank=True, null=True)

    def __str__(self):
        return self.name



class EntityDiretorie(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    
    entityName = models.CharField(max_length=50, null= True)
    entityID = models.CharField(max_length=50, null= True)
    branchCount = models.CharField(max_length=50, null= True)

    def __str__(self):
        return "%s" % self.entityName

class BranchDirectorie(models.Model):
    branchName = models.CharField(max_length=50, null= True)
    entity = models.ForeignKey(EntityDiretorie, on_delete=models.CASCADE)
    countersCount = models.IntegerField(default = 1, blank=True, null=True)
    branchID = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.branchName

    class Meta:
        ordering = ['branchName']

class CountersDirectorie(models.Model):
    branch = models.ForeignKey(BranchDirectorie, on_delete=models.CASCADE)
    counterName = models.CharField(max_length=50, null= True)
    # branchID = models.CharField(max_length=50, null=True)


    def __str__(self):
        return "%s" % self.branch


class LicenseKey(models.Model):
    unUsedKey = models.CharField(max_length=50, null= True)
    usedKey = models.CharField(max_length=50, null= True)


class Supplier(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    supplierName = models.CharField(max_length=50, null= True)
    companyName = models.CharField(max_length=50, null= True)
    mobileNumber = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, null= True)
    city = models.CharField(max_length=50, null= True)
    state = models.CharField(max_length=50, null= True)
    country = CountryField()
    postalCode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.supplierName

# class Product(models.Model):
#     branchID = models.CharField(max_length=50, null=True)
#     productName = models.CharField(max_length=50, null=True)
#     productCode = models.CharField(max_length=50, null=True)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
#     sellingCost = models.FloatField(blank=True, null=True)
#     vendorPrice = models.FloatField(blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)
#     tax = models.IntegerField(default=18, blank=True, null=True)

#     def __str__(self):
#         return self.productName

class Product(models.Model):
    branch = models.ForeignKey(BranchDirectorie, on_delete=models.CASCADE)

    productName = models.CharField(max_length=50, null=True)
    productCode = models.CharField(max_length=50, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    sellingCost = models.FloatField(blank=True, null=True)
    vendorPrice = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    tax = models.IntegerField(default=18, blank=True, null=True)

    def __str__(self):
        return self.productName

class InvoiceParent(models.Model):
    branch = models.ForeignKey(BranchDirectorie, on_delete=models.CASCADE,null=True)
    invoiceNumber = models.CharField(max_length=50, null=True)
    billAmount = models.FloatField(blank=True, null=True)
    totalProducts = models.IntegerField(blank=True, null=True)
    totalTax = models.IntegerField(default=18, blank=True, null=True)

class InvoiceChild(models.Model):
    invoiceNumber = models.ForeignKey(InvoiceParent,on_delete=models.CASCADE)
    productCode = models.CharField(max_length=50, null=True)
    