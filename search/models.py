from django.db import models
from django.utils.datetime_safe import datetime


class Country(models.Model):
    name = models.TextField('Название страны', null=False)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    name = models.TextField('Название города', null=False)

    def __str__(self):
        return self.name


class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    code = models.TextField('IATA код', max_length=3, null=False, unique=True)

    def __str__(self):
        return self.code


class HotelStars(models.IntegerChoices):
    ZERO_STARS = 0, 'Без звёзд'
    ONE_STAR = 1, 'Одна звезда'
    TWO_STARS = 2, 'Две звезды'
    THREE_STARS = 3, 'Три звезды'
    FOUR_STARS = 4, 'Четыре звезды'
    FIVE_STARS = 5, 'Пять звезд'


class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.TextField('Название отеля', null=False)
    stars = models.IntegerField(default=HotelStars.ZERO_STARS, choices=HotelStars.choices)

    def __str__(self):
        return self.name


class Discount(models.Model):
    reduction = models.IntegerField('Размер скидки')


class Tour(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True)
    images = models.ImageField(null=True, upload_to="hotels/", blank=False)
    images_2 = models.ImageField(null=True, upload_to="hotels/", blank=False)
    images_3 = models.ImageField(null=True, upload_to="hotels/", blank=False)
    images_4 = models.ImageField(null=True, upload_to="hotels/", blank=False)
    description = models.TextField('Описание тура', max_length=280, blank=True)
    site_url = models.URLField('Сайт', blank=True)
    contact_phone = models.TextField('Телефон', blank=True)
    count_travelers = models.SmallIntegerField('Количество человек', default=2, null=False)
    promoted = models.BooleanField('Продвижение в блоке с рекламой', default=False)
    price = models.SmallIntegerField('Цена тура', default=0)
    departure_date = models.DateTimeField('Дата оправления', null=True)
    arrival_date = models.DateTimeField('Дата прибытия', null=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)

    def count_nights(self):
        return (self.arrival_date - self.departure_date).days

    def __str__(self):
        return 'Тур в город {} в отель {}'.format(self.hotel.city, self.hotel.name)


class Request(models.Model):
    tour = models.ForeignKey(Tour, blank=False, on_delete=models.CASCADE)
    phone = models.TextField('Телефон', blank=False)
    email = models.EmailField()
