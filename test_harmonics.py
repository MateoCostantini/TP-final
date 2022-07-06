from harmonics import get_tone

def test_get_tone():
    harmonics_list = [(1, 1.0), (2, 0.2), (3, 0.3), (4, 0.1)]
    partiture= [(0.0, 1760.0, 0.5), (0.5, 698.456, 0.5), (1.0, 4186.01, 0.5), (1.2, 2217.46, 0.7), (1.9, 34.6479, 0.5)] #A6 F5 C8 Db7 Db1
    module_list = [('LINEAR', 0.02), ('CONSTANT',), ('INVEXP', 0.06)]
    fs = 12000
    
    assert len(get_tone(harmonics_list, partiture, module_list, fs)) == 29521, "not passed"
   
test_get_tone()
