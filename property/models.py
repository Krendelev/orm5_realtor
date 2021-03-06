from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        "Когда создано объявление", default=timezone.now, db_index=True
    )
    description = models.TextField("Текст объявления", blank=True)
    price = models.IntegerField("Цена квартиры", db_index=True)

    town = models.CharField(
        "Город, где находится квартира", max_length=50, db_index=True
    )
    town_district = models.CharField(
        "Район города, где находится квартира",
        max_length=50,
        blank=True,
        help_text="Чертаново Южное",
    )
    address = models.TextField(
        "Адрес квартиры", help_text="ул. Подольских курсантов д.5 кв.4"
    )
    new_building = models.BooleanField(
        null=True, blank=True, db_index=True, verbose_name="Новостройка"
    )
    floor = models.CharField(
        "Этаж", max_length=3, help_text="Первый этаж, последний этаж, пятый этаж"
    )
    rooms_number = models.IntegerField("Количество комнат в квартире", db_index=True)
    living_area = models.IntegerField(
        "количество жилых кв.метров", null=True, blank=True, db_index=True
    )
    has_balcony = models.NullBooleanField("Наличие балкона", db_index=True)
    active = models.BooleanField("Объявление активно", db_index=True)
    construction_year = models.IntegerField(
        "Год постройки здания", null=True, blank=True, db_index=True
    )
    liked_by = models.ManyToManyField(
        User, related_name="liked_flats", blank=True, verbose_name="Кому понравилась"
    )

    def __str__(self):
        return f"{self.town}, {self.address} ({self.price}р.)"


class Complaint(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="complaints",
        verbose_name="Кто жаловался",
    )
    complaint_about = models.ForeignKey(
        Flat,
        related_name="compaints",
        on_delete=models.CASCADE,
        verbose_name="Квартира, на которую пожаловались",
    )
    complaint_text = models.TextField(verbose_name="Текст жалобы")


class Owner(models.Model):
    name = models.CharField("ФИО владельца", max_length=200)
    phonenumber = models.CharField("Номер владельца", max_length=20)
    phone_pure = PhoneNumberField(
        null=True, blank=True, verbose_name="Нормализованный номер владельца"
    )
    flats_owned = models.ManyToManyField(
        Flat,
        related_name="flat_owners",
        blank=True,
        verbose_name="Квартиры в собственности",
    )

    def __str__(self):
        return self.name
