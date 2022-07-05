# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:26:03 2022

@author: 54911
"""

# from xylophone.client import XyloClient
# from xylophone.xylo import XyloNote

posible_notes = ("C7", "C#7", "Cb7",
                 "B6", "Bb6",
                 "A6", "A#6", "Ab6",
                 "G6", "G#6", "Gb6",
                 "F6", "F#6",
                 "E6", "Eb6",
                 "D6", "D#6", "Db6",
                 "C6", "C#6",
                 "B5", "Bb5",
                 "A5", "A#5", "Ab5",
                 "G5",
                 "F5",
                 "E5", "Eb5",
                 "D5", "D#5", "Db5",
                 "C5", "C#5",
                 "B4", "Bb4",
                 "A4", "A#4", "Ab4",
                 "G4", "G#4")

class XyloNote:
    def __init__(self, note, tstart, bps):
        self.note = note
        self.tstart = tstart
        self.bps = bps
         

if __name__ == "__main__": 
    notes =[]
    with open("partiture.txt", "r") as f:
        for line in f:
            note_param = (line.rstrip()).split(" ")
            if note_param[1] in posible_notes:
                note_param[0] = float(note_param[0])
                note = XyloNote(note_param[1], note_param[0], 120)
                notes.append(note)
    print(notes)    


# client = XyloClient(host='localhost', port=8080)
# client.load(notes)
# client.play()