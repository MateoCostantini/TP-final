from main import notes
from harmonics import get_tone
import analyze_files

def test_get_tone():
    fs = 48000
    partiture_file = open('partiture_file.txt', 'r')
    # z = []
    instrument_file = open("instrument_file.txt", "r")
    track = notes(fs, partiture_file, instrument_file)
    harmonics_list, module_list = analyze_files.get_instrument(instrument_file)
    partiture = analyze_files.get_partiture(partiture_file)
    instrument_file.close()
    partiture_file.close()
    # x = 0
    # z = 0
    # g = get_tone(harmonics_list, partiture, module_list, fs)
    # for i in track:
    #     z +=i
    # for i in g:
    #     x+=i
    # assert x == z, "not pass"
    assert get_tone(harmonics_list, partiture, module_list, fs).all() == track.all(), "not pass"
    
test_get_tone()
