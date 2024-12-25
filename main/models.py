from django.db import models
from faker import Faker

class IpAddress(models.Model):
    """
    Model to represent an IP address. Supports both IPv4 and IPv6 formats.

    Fields:
        ip_address (CharField): A string field to store the IP address (maximum length of 45 characters).
    """

    ip_address = models.CharField(max_length=45)

    @classmethod
    def generator_ipv4(cls, num):
        """
        Generate and bulk create a specified number of IPv4 addresses.

        Args:
            num (int): The number of IPv4 addresses to generate and save.

        Example:
            IpAddress.generator_ipv4(100)  # Creates 100 fake IPv4 entries in the database.
        """
        fake = Faker()
        ips = [cls(ip_address=fake.ipv4()) for _ in range(num)]
        cls.objects.bulk_create(ips)

    @classmethod
    def generator_ipv6(cls, num):
        """
        Generate and bulk create a specified number of IPv6 addresses.

        Args:
            num (int): The number of IPv6 addresses to generate and save.

        Example:
            IpAddress.generator_ipv6(50)  # Creates 50 fake IPv6 entries in the database.
        """
        fake = Faker()
        ips = [cls(ip_address=fake.ipv6()) for _ in range(num)]
        cls.objects.bulk_create(ips)
