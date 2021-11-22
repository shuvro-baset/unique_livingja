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
