import numpy as np
import soundfile as sf
class Sound:
    def __init__(self,db):
        self._target_spl = db
        self._reference_pressure = 20e-6

        self._frequency = 1000
        self._duration = 1.0
        self._sample_rate = 44100

    @property
    def db(self):
        return self._target_spl

    @db.setter
    def db(self,db):
        self._target_spl = db

    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self,duration):
        self._duration = duration

    def create_sound(self):

        #SPL(dB)=20×log(p/p0) p -> rms pressure | p0 -> reference pressure
        #standard reference pressure is 20 micropascals which is considered the threshold of human hearing


        pressure = self._reference_pressure * (10 ** (self._target_spl / 20))
        #calculate sound duration
        internal_sample_rate = np.linspace(0,int(self._duration),int(self._sample_rate * self._duration),endpoint=False)
        #use np.sin to create pure wave sounds
        #self._frequency is how many complete cycles the sine wave will make in one second
        #each value in internal_sample_rate corresponds to a specific moment in time
        #to acquire given db multiply with pressure
        wave_form = pressure * np.sin(2 * np.pi * self._frequency * internal_sample_rate)
        sf.write('startle.wav', wave_form, self._sample_rate)




