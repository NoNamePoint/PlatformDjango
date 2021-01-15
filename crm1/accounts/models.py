from django.db import models



class Customer(models.Model):
    class Meta:	
	    verbose_name = 'Заказчик'
	    verbose_name_plural = 'Заказчики'


    name = models.CharField(max_length=200, verbose_name= 'Имя' ,null=True)
    phone = models.CharField(max_length=200, verbose_name= 'Телефон', null=True)
    email = models.EmailField(max_length=200, verbose_name='Почта', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):

	    return self.name

class Tag(models.Model):
    class Meta:
	    verbose_name = 'Тег'
	    verbose_name_plural = 'Теги'

    name = models.CharField(max_length=200, null=True, verbose_name = 'Категория')

    def __str__(self):
	    return self.name
    	

class Product(models.Model):
    	
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'


	CATEGORY = (('Для дома', 'Для дома'),
			('Для улицы', 'Для улицы')) 

	name = models.CharField(max_length=200, verbose_name='Наименование товара', null=True)
	price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', null=True)
	slug = models.SlugField(max_length = 50 ,unique=True, null=True)
	category = models.CharField(max_length=200, null=True, verbose_name='Категория', choices=CATEGORY)
	description = models.CharField(max_length=200, verbose_name='Описание', null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tag = models.ManyToManyField(Tag, verbose_name = 'Тег')
	
	def __str__(self):
    		return self.name

class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
	    

    STATUS = (('Ожидание', 'Ожидание'),
           ('На доставке', 'На доставке'),
			('Доставлено', 'Доставлено'))

    customer = models.ForeignKey(Customer, null=True, verbose_name='Заказчик', on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, verbose_name='Товар', on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, verbose_name='Статус', choices=STATUS)


