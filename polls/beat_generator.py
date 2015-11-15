from random import randint


def GenerateBeat():
    number_of_snare_hits = randint(0,8)
    number_of_bass_kicks = randint(0,8)
    beats_to_hit_the_snare = ChooseBeatsToHitDrum(number_of_snare_hits)
    beats_to_kick_the_bass = ChooseBeatsToHitDrum(number_of_bass_kicks)
    new_beat = Beat(beats_to_kick_the_bass, beats_to_hit_the_snare)
    return new_beat
    
def ChooseBeatsToHitDrum(number_of_beats):
    hits = []
    for i in range(number_of_beats):
        hits.append(randint(0,8))
    return hits
    
class Beat:
    def __init__(self, bass_kicks, snare_hits):
        self.bass_kicks = bass_kicks
        self.snare_hits = snare_hits
    
print GenerateBeat()
