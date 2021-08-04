import rooms
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ Roomtype Object Definition """

    class Meta:
        # admin penal에서 클래스의 이름이 어떻게 표기될 것인지 설정 해주는 변수
        verbose_name_plural = "Room Type"
        ordering = ['name']


# 결국 이 클래스는 손자 클래스가 된다.


class Amenity(AbstractItem):

    """ Amenity Object Definition """

    class Meta:
        # admin penal에서 클래스의 이름이 어떻게 표기될 것인지 설정 해주는 변수
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Object Definition """

    class Meta:
        # admin penal에서 클래스의 이름이 어떻게 표기될 것인지 설정 해주는 변수
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Object Definition """

    class Meta:
        # admin penal에서 클래스의 이름이 어떻게 표기될 것인지 설정 해주는 변수
        verbose_name_plural = "House Rule"


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    bed = models.IntegerField()
    bedrooms = models.IntegerField()
    guests = models.IntegerField(help_text="How many people will be staying?")
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # 이때 host는 user이다. 모델과 모델을 연결해야 한다. 이것이 foreign key.
    # user와 room은 일대 다 관계이다. user는 여러개의 room을 가질 수 있다.
    # 하지만 room은 1명의 user만을 가질 수 있다.
    # on_delete: user가 삭제되었다면 어떻게 대응 할 것인가?
    # 이 옵션은 foreign key에만 적용된다.
    # related_name = 관계된 객체가 "자신"을 어떻게 가리키는가임!
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE)
    # Many to many관계는 foreign key를 사용하지 않는다.
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True)
    # 여러개의 amenity 타입을 하나의 방이 가질 수 있음.
    Amenities = models.ManyToManyField(
        Amenity, related_name="rooms", blank=True)
    Facilities = models.ManyToManyField(
        Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(
        HouseRule, related_name="rooms", blank=True)

    #### 여기 함수들은 각 room 객체에 대해 적용하는 함수 ####

    # 클래스를 문자열로 보여주는 함수. 이를 커스텀 할 수 있음. 모든 클래스가 가짐
    def __str__(self):
        return self.name

    # 아래의 함수는 어디민에서 모델으 건드릴 때 뿐만이 아니라 어딘가에서 모델을 건드릴 때 항상 일어난다.
    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return all_ratings / len(all_reviews)
        return 0

    def first_photo(self):
        photo, = self.photos.all()[:1]
        return photo.file.url

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5] # 한 객체에 등록된 사진들을 다 가져온다.
        print(photos)
        return photos

class Photo (core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    rooms = models.ForeignKey(
        Room, related_name="photos", on_delete=models.CASCADE)

    # 객체를 출력했을 때 표시되는 방법
    def __str__(self):
        return self.caption
