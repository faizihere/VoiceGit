from logging import lastResort
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()

from urllib import request
from datetime import *
from .forms import *

import datetime


def home(request):
    return render(request, 'interface/home.html')

def entityReg(request):    
    return render(request, 'authentication/entityOwnerReg.html')



# remember about serial key access
# faizi remember about is_paid
def registerAction(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        entityName = request.POST.get('entityName')
        branchName = request.POST.get('branchName')
        email = request.POST.get('email')
        verifyEmail = request.POST.get('verifyEmail')
        username = request.POST['email']
        password = request.POST['password']
        verifyPassword = request.POST['verifyPassword']
        designation = request.POST.get('designation')
        entityID = request.POST.get('entityID')
        branchID = request.POST.get('branchID')
        

        if(email == verifyEmail):
            if(password == verifyPassword):
                if User.objects.filter(username=username).exists():

                    # messages.info(request, 'Email already registered')
                    print("Email already registered")
                    return render(request, 'authentication/entityOwnerReg.html')

                else:
                    # time delta is set for 365 days but it should varry based on the user subscription duration.
                    if(designation == "is_entityOwner"):

                        user = User.objects.create_user(username=username, email=email, password=password, name=name, is_entityOwner=True, entityName=entityName, account_expiry=datetime.now()+ timedelta(days=(+365)))
                        user.save()


                        generatedEID = str(user.id)+entityName[0:6].upper()
                  
                        user.entityID = generatedEID
                        user.save()

                        EntityDiretorie.objects.create(user = user, entityName=entityName, entityID = generatedEID).save()

                    if(designation == "is_branchManager"):

                        entityDirectory = EntityDiretorie.objects.filter(entityID=entityID).first()
                        entityName = entityDirectory.entityName

                        user = User.objects.create_user(username=username, email=email, password=password, name=name, is_branchManager=True, entityName=entityName, entityID=entityID, branchName=branchName, account_expiry=datetime.now()+ timedelta(days=(+365)))
                        user.save()

                        generatedBID = str(user.id)+entityName[0:3].upper()+branchName[0:3].upper()

                        user.branchID = generatedBID
                        user.save()
                        
                        BranchDirectorie.objects.create(branchName = branchName, entity = entityDirectory, branchID = generatedBID)


                        """
                        request entity name from entity directory and store it...
                        generate branchID thereby counter manager can use it
                        """

                    if(designation == "is_counterManager"):

                        fetched = BranchDirectorie.objects.filter(branchID=branchID).first()
                    
                        entityName = fetched.entity
                        branchName = fetched.branchName

                        user = User.objects.create_user(username=username, email=email, password=password, name=name, is_counterManager=True, branchName=branchName, branchID=branchID, account_expiry=datetime.now()+ timedelta(days=(+365)))
                        user.save()

                        branch = BranchDirectorie.objects.filter(branchID = branchID).first()

                        CountersDirectorie.objects.create(branch = branch)

                      


                        """
                        We need branch names to be stored somewhere so that we can use it
                        """

                    print("user registered successfully!")

                    return render(request, 'successRedirect/entityOwnerSuccess.html')
                    # think about popping the serial number incase of ofline mode of registration.

            else:
                # messages.info(request, 'Password not matching')
                print("Password Not Matching")
                return render(request, 'authentication/entityOwnerReg.html')

        else:
            print("Email not matching")
            # messages.info(request, 'Email not matching')
            return render(request, 'authentication/entityOwnerReg.html')
"""    
    if request.method == "POST":
        
        name = request.POST.get('name')
        entityName = request.POST.get('entityName')
        branchName = request.POST.get('branchName')
        email = request.POST.get('email')
        verifyEmail = request.POST.get('verifyEmail')
        username = request.POST['email']
        password = request.POST['password']
        verifyPassword = request.POST['verifyPassword']
        designation = request.POST.get('designation')
        entityID = request.POST.get('entityID')
        branchID = request.POST.get('branchID')
        

        if(email == verifyEmail):
            if(password == verifyPassword):
                if User.objects.filter(username=username).exists():

                    # messages.info(request, 'Email already registered')
                    print("Email already registered")
                    return render(request, 'authentication/entityOwnerReg.html')

                else:
                    # time delta is set for 365 days but it should varry based on the user subscription duration.
                    if(designation == "is_entityOwner"):

                        user = User.objects.create_user(username=username, email=email, password=password, name=name, is_entityOwner=True, entityName=entityName, account_expiry=datetime.now()+ timedelta(days=(+365)))
                        user.save()


                        generatedEID = str(user.id)+entityName[0:6].upper()
                  
                        user.entityID = generatedEID
                        user.save()

                        EntityDiretorie.objects.create(entityName=entityName, entityID = generatedEID).save()

                    if(designation == "is_branchManager"):


                        entityDirectory = EntityDiretorie.objects.filter(entityID=entityID).first()



                        user = User.objects.create_user(username=username, email=email, password=password, name=name, is_branchManager=True, entityName=entityName, entityID=entityID, branchName=branchName, account_expiry=datetime.now()+ timedelta(days=(+365)))
                        user.save()

                        Branche.objects.create(branchName=branchName, entityID=entityID).save()

                        generatedBID = str(user.id)+entityName[0:3].upper()+branchName[0:3].upper()

            
                        user.branchID = generatedBID
                        user.save()
                        
                        fetcherUser = User.objects.filter(email = email).first()


                        entityDirectory.branchID = generatedBID
                        entityDirectory.user = fetcherUser.id
                        entityDirectory.save()

                    
                        # request entity name from entity directory and store it...
                        # generate branchID thereby counter manager can use it
                    

                    if(designation == "is_counterManager"):

                        fetched = EntityDiretorie.objects.filter(branchID=branchID).first()
                    
                        entityName = fetched.entityName
                        entityID = fetched.entityID
                        branchName = fetched.branchName
                        enityID = fetched.entityID

                        user = User.objects.create_user(username=username, email=email, password=password, name=name, is_counterManager=True, entityName=entityName, entityID=entityID, branchName=branchName, branchID=branchID, account_expiry=datetime.now()+ timedelta(days=(+365)))
                        user.save()
                        print(entityName, entityID, branchName, enityID)


                        
                        # We need branch names to be stored somewhere so that we can use it
                    

                    print("user registered successfully!")

                    return render(request, 'successRedirect/entityOwnerSuccess.html')
                    # think about popping the serial number incase of ofline mode of registration.

            else:
                # messages.info(request, 'Password not matching')
                print("Password Not Matching")
                return render(request, 'authentication/entityOwnerReg.html')

        else:
            print("Email not matching")
            # messages.info(request, 'Email not matching')
            return render(request, 'authentication/entityOwnerReg.html')
"""



def loginAction(request):
    
    if request.method == 'POST':

        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if(user):
            auth.login(request, user)
            if request.user.is_authenticated:
                if request.user.is_entityOwner:
                    return redirect(entityDirectorDash)

                if request.user.is_branchManager:
                    return redirect(branchManagerDash)

                if request.user.is_counterManager:
                    userBranch = BranchDirectorie.objects.filter(branchID = request.user.branchID).first()
              
                    print(userBranch.entity.entityID)
                    return redirect(cashierDash)

            return redirect('home')

        else:
            print("Wrong Username/Password")
            # messages.info(request, 'Wrong Username/Password')
            return redirect('home')

        #         dateExpiry = request.user.account_expiry
        #         dateToday =  date.today()

        #         if(dateExpiry < dateToday):
        #             changeUserStatus = User.objects.filter(id = request.user.id).first()
        #             changeUserStatus.is_paid = False
        #             changeUserStatus.save()
        #             return redirect('zvcxv')

        #         else:
        #             return redirect('xvyzx')
            

    else:
        return render(request, 'authentication/login.html')


def cashierDash(request):
    if request.user.is_counterManager:
        return render(request, 'interface/dashCM.html')

def branchManagerDash(request):
    if request.user.is_branchManager:
        return render(request, 'interface/dashBM.html')

def entityDirectorDash(request):
    if request.user.is_entityOwner:
        return render(request, 'interface/dashED.html')

def logoutAction(request):
    auth.logout(request)
    print("Logout Successful!")
    return redirect('home')

def branchManagerReg(request):
    return render(request, 'authentication/branchManagerReg.html')

def counterManagerReg(request):
    return render(request, 'authentication/counterManager.html')

def temp(request):
    return render(request, 'temp/ownerPage.html')

def supplierAction(request):
    return render(request,'interface/manager/supplierHome.html')

def addSupplier(request):

    if request.method == "POST":
        
        supplierName = request.POST.get('supplierName')
        supplierMobile = request.POST.get('supplierMobile')
        companyName = request.POST.get('companyName')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postalCode = request.POST.get('postalCode')
        designation = request.POST.get('designation')
        country = request.POST.get('country')
        address = request.POST.get('address')

        if(designation == "is_branchManager"):
            print("Supplier Added")
            supplier = Supplier.objects.create(supplierName=supplierName, mobileNumber=supplierMobile, companyName=companyName, city=city, state=state, country = country, postalCode=postalCode)
            supplier.save()

            regForm = CountryModelForm()
            context = {'regForm':regForm}
            return render(request,'interface/manager/addSupplier.html',context)

    else:
        regForm = CountryModelForm()

        context = {'regForm':regForm}

        return render(request,'interface/manager/addSupplier.html',context)

def productAction(request):
    return render(request,'interface/manager/productHome.html')

def managerDashboard(request):
    return render(request, 'interface/dashBM.html')

def addProduct(request):


    if request.method == "POST":
        
        productName = request.POST.get('productName')
        productCode = request.POST.get('productCode')
        supplier = request.POST.get('supplier')
        sellingCost = request.POST.get('sellingCost')
        vendorPrice = request.POST.get('vendorPrice')
        quantity = request.POST.get('quantity')
        tax = request.POST.get('tax')


        userBranch = BranchDirectorie.objects.filter(branchID = request.user.branchID).first()

        

        product = Product.objects.create(branch = userBranch, productName=productName, productCode=productCode, supplier=supplier, sellingCost=sellingCost, vendorPrice=vendorPrice, quantity = quantity, tax=tax)
        product.save()
        return render(request,'interface/manager/addProduct.html')

    else:
        return render(request,'interface/manager/addProduct.html')

# Array to store multiple products

productName = []
productCode = []
productPricing = []
productQuantity = []
productActualPrice = []

# formula
# (25*25000)/100
def billProduct(request):

    
    
    branchID = request.user.branchID
    itemCode = request.POST.get('itemCode')
    itemQuantity = request.POST.get('itemQuantity')
    
    fetchedBranch = BranchDirectorie.objects.filter(branchID = branchID).first()

    fetchedItem = Product.objects.filter(productCode = itemCode, branch = fetchedBranch).first()

    if(fetchedItem):
        sellingCost = float(fetchedItem.sellingCost)
        productActualPrice.append(sellingCost)
        description = fetchedItem.productName


        fetchedQuantity = int(itemQuantity)
        unitPrice = sellingCost
            
        productName.append(fetchedItem.productName)
        productCode.append(itemCode)
        productQuantity.append(fetchedQuantity)

        quantityBasedPrice = fetchedItem.sellingCost * fetchedQuantity

        productPricing.append(quantityBasedPrice)

        for i in range(len(productPricing)):
            totalBill = sum(productPricing)

        context = {'totalBill':totalBill, 'unitPrice':unitPrice, 'productQuantity':productQuantity, 'description':description, 'productPricing':productPricing, 'productName':productName, 'productActualPrice':productActualPrice}
        return render(request, 'interface/dashCM.html',context)
    

    return render(request, 'interface/dashCM.html')

def billClear(request):
    
    productName.clear()
    productPricing.clear()
    productQuantity.clear()
    productActualPrice.clear()

    context = {'productQuantity':productQuantity, 'productPricing':productPricing, 'productName':productName, 'productActualPrice':productActualPrice}
    return render(request, 'interface/dashCM.html',context)

    # kdsf398
def billConfirm(request):
    print("Bill Confirm!")
    print(request.user.id)
    print(request.user.branchID)
    fetchedData = BranchDirectorie.objects.filter(branchID = request.user.branchID).first()
    print(fetchedData.branchName)
    print(fetchedData.entity)
    userID = str(request.user.id)
    entityName = str(fetchedData.entity)

    invoiceID = entityName[0:3].upper()
    
    latestInvoice = InvoiceParent.objects.filter(branch = fetchedData).order_by('id').last()
    print(latestInvoice.invoiceNumber)

    if not latestInvoice:
        InvoiceParent.objects.create(invoiceNumber = invoiceID+str(1),branch = fetchedData)
    
    else:
        toCount = int(latestInvoice.invoiceNumber[3:])
        counted = str(toCount+1)
        currentInvoiceNumber = latestInvoice.invoiceNumber[0:3]+counted
        InvoiceParent.objects.create( branch = fetchedData, invoiceNumber = currentInvoiceNumber, billAmount=sum(productPricing), totalProducts = sum(productQuantity))
     
        print("Total Bill")
        print(sum(productPricing))
    for i in range(len(productName)):
        invoiceDirectory = InvoiceParent.objects.filter(invoiceNumber = currentInvoiceNumber).first()

        InvoiceChild.objects.create(invoiceNumber = invoiceDirectory, productCode = productCode[i])

    productName.clear()
    productPricing.clear()
    productQuantity.clear()
    productActualPrice.clear()

    return render(request, 'interface/dashCM.html')
