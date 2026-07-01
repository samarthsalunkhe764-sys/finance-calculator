from calculators.sip import future_value

def test_sip():
    assert future_value(1000,12,1)>12000
