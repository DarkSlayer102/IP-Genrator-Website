from django.db import models
from faker import Faker

class IpAddress(models.Model):
    ip_address = models.CharField(max_length=45)

    @classmethod
    def generator_ipv4(cls,num):
        fake = Faker()

        ips = [cls(ip_address=fake.ipv4()) for i in range(num)]
        cls.objects.bulk_create(ips)

    @classmethod
    def generator_ipv6(cls,num):
        fake = Faker()
        ips = [cls(ip_address=fake.ipv6()) for i in range(num)]
        cls.objects.bulk_create(ips)
