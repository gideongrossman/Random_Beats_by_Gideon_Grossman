from random import randint
import sheet_music_generator


def GenerateBeat(number_of_beats_in_measure):
    number_of_snare_hits = randint(1,int(number_of_beats_in_measure))
    number_of_bass_kicks = randint(1,int(number_of_beats_in_measure))
    beats_to_hit_the_snare = ChooseBeatsToHitDrum(number_of_snare_hits, int(number_of_beats_in_measure))
    beats_to_kick_the_bass = ChooseBeatsToHitDrum(number_of_bass_kicks, int(number_of_beats_in_measure))
    new_beat = Beat(beats_to_kick_the_bass, beats_to_hit_the_snare)
    #sheet_music_generator.GenerateSheetMusicImage()
    return new_beat, 4
    
def ChooseBeatsToHitDrum(number_of_beats, number_of_beats_in_measure):
    hits = []
    i = 0
    while (i < number_of_beats):
        count = (randint(1,number_of_beats_in_measure))
        if not(count in hits):
            hits.append(count)
            i+=1              
    return hits
    
class Beat:
    def __init__(self, bass_kicks, snare_hits):
        self.bass_kicks = bass_kicks
        self.snare_hits = snare_hits