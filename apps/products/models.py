from apps.user.models import UniUser as User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create(cls, value):
        category_ins = cls.objects.filter(name=value).exists()
        if not category_ins:
            category = Category()
            category.name = value
            category.save()


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create(cls, value):
        category_ins = cls.objects.filter(name=value).exists()
        if not category_ins:
            category = SubCategory()
            category.name = value
            category.save()


class SupCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create(cls, value):
        category_ins = cls.objects.filter(name=value).exists()
        if not category_ins:
            category = SupCategory()
            category.name = value
            category.save()


class AddCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create(cls, value):
        category_ins = cls.objects.filter(name=value).exists()
        if not category_ins:
            category = AddCategory()
            category.name = value
            category.save()


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    sku = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    finishes = models.CharField(max_length=200,
                                help_text='<strong style="color:teal">Please seperate the finishes by Bar symbol( | ). Like ex: chrome|brushed-nickel</strong>',
                                null=True, blank=True)
    sup_category = models.ForeignKey(SupCategory, on_delete=models.CASCADE, blank=True, null=True)
    add_category = models.ForeignKey(AddCategory, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_in_stock = models.BooleanField(verbose_name='Is in stock?', default=True)
    is_featured = models.BooleanField(verbose_name='Is Featured?', default=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class HomeSlider(models.Model):
    HOME_SLIDER_CHOICES = (
        ('/category/kitchen', '/category/kitchen'),
        ('/category/bathroom', '/category/bathroom'),
        ('/category/commercial', '/category/commercial'),
    )

    image = models.ImageField(upload_to='home_slider', null=True, blank=True)
    category_url = models.CharField(max_length=200, choices=HOME_SLIDER_CHOICES, default=HOME_SLIDER_CHOICES[0],
                                    null=True, blank=True)

    def __str__(self):
        return self.image.url


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    # order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return float(format(total, ".2f"))

    @property
    def get_tax(self):
        return 0.15


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(verbose_name='Is order completed?', default=False)
    complete_date = models.DateTimeField(null=True, blank=True)
    is_delivered = models.BooleanField(verbose_name='Is order delivered?', default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    order_type = models.CharField(max_length=100, null=True, blank=True, )
    sales_rep = models.CharField(max_length=200, null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    shipping_address = models.ForeignKey('ShippingAddress', related_name='shipping_address', on_delete=models.SET_NULL,
                                         blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.customer)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return float(format(total, ".2f"))

    @property
    def get_tax(self):
        return 0.15

    @property
    def get_tax_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems]) * 0.15
        return total

    @property
    def get_cart_total_with_tax(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        total_tax = sum([item.get_total for item in orderitems]) * 0.15
        return total + total_tax

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        # total = len([item.quantity for item in orderitems])
        return total

    @property
    def is_order_delivered(self):
        if self.is_delivered:
            return True
        return False


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True, )
    email = models.EmailField(null=True, blank=True, )
    phone = models.CharField(max_length=200, null=True, blank=True, )
    address = models.TextField(null=True, blank=True, )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
