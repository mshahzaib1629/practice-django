from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # adding __str__ function to display customer's name instead of object (1)
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    #   CATEGORY is not the property of this model. But a tuple containing drop down values for the category property
    CATEGORY = (
            ('Indoor', 'Indoor'),
            ('Out Door', 'Out Door'),
            ) 

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
      return self.name

class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
            )

    # on_delete=models.SET_NULL: when the customer is deleted, the customer field in order will be null
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)