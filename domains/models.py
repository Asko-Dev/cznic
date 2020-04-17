from django.db import models
from django.core.validators import RegexValidator


# Flag model, Flags will be assigned to Domains
class DomainFlag(models.Model):
    """Domain Flad for Domain"""

    TYPE_CHOICE = [
        ('EXPIRED', 'Expired'),
        ('OUTZONE', 'Outzone'),
        ('DELETE_CANDIDATE', 'Delete Candidate')
    ]
    type = models.CharField(
        choices=TYPE_CHOICE,
        max_length=20,
        default='EXPIRED'
    )
    flag_valid_from = models.DateTimeField(blank=True, null=True)
    flag_valid_to = models.DateTimeField(blank=True, null=True)

    REQUIRED_FIELDS = ('type',)

    def __str__(self):
        return self.type


# main domain model to which flags will get assigned
class Domain(models.Model):
    """Main Domain model"""
    FQDN = models.CharField(
        max_length=255,
        help_text='Fully Qualified Domain Name: www.yourdomain.com',
        unique=True,
        validators=[RegexValidator(
            '^www+\.[a-z0-9]+\.[a-z0-9]{1,4}$',
            'www.yourdomain.com only',
            'Invalid Entry')
        ]
    )
    date_created = models.DateTimeField()
    date_expires = models.DateTimeField()
    date_deletion = models.DateTimeField()
    flag = models.ManyToManyField('DomainFlag')

    REQUIRED_FIELDS = ('FQDN', 'date_created', 'date_expires', 'date_deletion')

    def __str__(self):
        return self.FQDN
