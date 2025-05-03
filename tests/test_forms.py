import pytest
from forms import SubnetForm

def test_valid_form():
    form = SubnetForm(data={"ip_address": "192.168.1.0", "cidr_mask": 24, "split_mask": "", "cloud_provider": "aws"})
    assert form.validate() == True

def test_invalid_ip():
    form = SubnetForm(data={"ip_address": "999.999.999.999", "cidr_mask": 24})
    assert "Invalid IP address." in form.errors.get("ip_address", [])

def test_mask_out_of_range():
    form = SubnetForm(data={"ip_address": "192.168.1.0", "cidr_mask": 999})
    assert "Enter a mask between 0 and 128." in form.errors.get("cidr_mask", [])
