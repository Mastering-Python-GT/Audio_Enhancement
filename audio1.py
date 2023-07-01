from pedalboard.io import AudioFile
from pedalboard import *
import noisereduce as nr

sr=44100
with AudioFile('audios/audio1.wav').resampled_to(sr) as f:
    audio = f.read(f.frames)

reduced_noise = nr.reduce_noise(y=audio, sr=sr, stationary=True, prop_decrease=0.75)

board = Pedalboard([
    NoiseGate(threshold_db=-30, ratio=1.5, release_ms=250),
    Compressor(threshold_db=-16, ratio=2.5),
    LowShelfFilter(cutoff_frequency_hz=400, gain_db=10, q=1),
    Gain(gain_db=10)
])

effected = board(reduced_noise, sr)


with AudioFile('audios/audio1_enhenced.wav', 'w', sr, effected.shape[0]) as f:
  f.write(effected)




















  """
print('original audio')
sd.play(audio[0],sr)
sd.wait()

print('enhanced audio')
sd.play(effected[0],sr)
sd.wait()

"""