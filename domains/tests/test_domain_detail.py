import unittest
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from domains.models import Domain, DomainFlag
from django.utils import timezone


def domain_url_detail(domain_id):
    return reverse('domain-detail', args=[domain_id])


def sample_domain(
    FQDN='www.test3.com',
    date_created=timezone.now(),
    date_expires=timezone.now(),
    date_deletion=timezone.now()
):
    """Sample domain for tests"""
    return Domain.objects.create(
        FQDN=FQDN,
        date_created=date_created,
        date_expires=date_expires,
        date_deletion=date_deletion
        )


def sample_flag(
    type='OUTZONE',
    flag_valid_from=timezone.now(),
    flag_valid_to=timezone.now()
):
    """Sample domain for tests"""
    return DomainFlag.objects.create(
        type=type,
        flag_valid_from=flag_valid_from,
        flag_valid_to=flag_valid_to,
        )


class DomainDetailDisplay(TestCase):
    """Testing correct display"""

    def setUp(self):
        client = Client()

    def test_detail_page_correct_display(self):
        """Testing domain displays correctly"""
        domain = sample_domain()
        flag = sample_flag()
        domain.flag.add(flag)

        url = domain_url_detail(domain.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['FQDN'], domain.FQDN)
        self.assertEqual(res.context['date_created'], domain.date_created)
        self.assertEqual(len(res.context['flags']), 1)

    def test_detail_page_more_flags(self):
        """Testing domain flags display correctly"""
        domain = sample_domain()
        flag = sample_flag()
        flag2 = sample_flag(type='EXPIRED')
        domain.flag.add(flag)
        domain.flag.add(flag2)

        url = domain_url_detail(domain.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['FQDN'], domain.FQDN)
        self.assertEqual(len(res.context['flags']), 2)
