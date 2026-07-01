from calculators.emi import emi

def test_emi():
    assert emi(100000,10,1)>0
