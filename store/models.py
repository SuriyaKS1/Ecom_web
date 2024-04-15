from django.db import models

class Promotions(models.Model):
    description=models.CharField(max_length=250)
    discount=models.FloatField()

class Collections(models.Model):
    title=models.CharField(max_length=250)

class Products(models.Model):
    title= models.CharField(max_length=225)
    slug=models.SlugField()
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collections, on_delete=models.PROTECT)
    pormotion=models.ManyToManyField(Promotions)

class Customers(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE ,'BRONZE'),
        (MEMBERSHIP_SILVER , 'SILVER'),
        (MEMBERSHIP_GOLD , 'GOLD'),
    ]
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    email_id=models.EmailField(unique=True)
    phone=models.CharField(max_length=225)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    #used choice model to select membership
    


class Orders(models.Model):
    PAYMENT_COMPLETE='C'
    PAYMENT_PENDING='P'
    PAYMENT_FAILED='F'
    PAYMENT_CHOICE=[
        (PAYMENT_COMPLETE,'COMPLETE'),
        (PAYMENT_PENDING,'PENDING'),
        (PAYMENT_FAILED,'FAILED'),
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment=models.CharField(max_length=1,choices=PAYMENT_CHOICE,default=PAYMENT_PENDING)
    #used choice model to select about the payment process
    customer=models.ForeignKey(Customers,on_delete=models.PROTECT)

class Ordered_items(models.Model):
    order=models.ForeignKey(Orders, on_delete=models.PROTECT)
    product=models.ForeignKey(Products, on_delete=models.PROTECT)
    quality=models.PositiveIntegerField()
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)

class Carts(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

class Cart_items(models.Model):
    cart=models.ForeignKey(Carts,on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    
class Address(models.Model):
    street=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    customer=models.ForeignKey(Customers, on_delete=models.CASCADE)
    '''primary key allow only one address and wont allow duplicates
    used one-to-one field to inherete the parent class(Customers) to the child(Addess) class
    the on_delete model it has four models(CASCADE,SET_NULL,SET_DEFAULT,PROTECT)
    CASCADE= if customer profile deleted the address also deleted
    SET_NULL = if customer deleted the address not deleted and it stays in the database and sets to nullable and the func doesn't allow nullable value
    SET_DEFAULT=if customer deleted  the address set to its default value
    PROTECT=if customer deleted the address not deleted and its get protected
    '''




