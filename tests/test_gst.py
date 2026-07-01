from calculators.gst import add_gst

def test_gst():
    assert add_gst(100,18)==118
