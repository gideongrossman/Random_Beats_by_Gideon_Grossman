from random import randint
import sheet_music_generator
import json
from .models import Choice, Question, Beat

def GenerateBeat(number_of_beats_in_measure):
    number_of_snare_hits = randint(1,int(number_of_beats_in_measure))
    number_of_bass_kicks = randint(1,int(number_of_beats_in_measure))
    beats_to_hit_the_snare = json.dumps(ChooseBeatsToHitDrum(number_of_snare_hits, int(number_of_beats_in_measure)))
    beats_to_kick_the_bass = json.dumps(ChooseBeatsToHitDrum(number_of_bass_kicks, int(number_of_beats_in_measure)))
    new_beat = Beat.objects.create(beat_name = "not named", snare_hits = beats_to_hit_the_snare, bass_kicks = beats_to_kick_the_bass)
    #sheet_music_generator.GenerateSheetMusicImage()
    return new_beat
    
def ChooseBeatsToHitDrum(number_of_beats, number_of_beats_in_measure):
    hits = []
    i = 0
    while (i < number_of_beats):
        count = (randint(1,number_of_beats_in_measure))
        if not(count in hits):
            hits.append(count)
            i+=1              
    return hits