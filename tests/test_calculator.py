import pytest
from calculator import summarize_network, split_network
import ipaddress

def test_summarize_small_network():
    summary = summarize_network("192.168.0.0", 30)
    result = summary['result']
    assert result['Number of Hosts'] == 2
    assert result['First Usable IP'] == "192.168.0.1"
    assert result['Last Usable IP'] == "192.168.0.2"
    assert "Compatible" in summary['cloud_warnings'][0]

def test_split_network():
    network = ipaddress.ip_network("10.0.0.0/24")
    subnets = split_network(network, 26)
    assert len(subnets) == 4
    assert str(subnets[0]) == "10.0.0.0/26"
