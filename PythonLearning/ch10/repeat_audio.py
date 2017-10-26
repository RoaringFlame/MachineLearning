from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import sys

WAV_FILE = "smashingbaby.wav"

data = wavfile.read(WAV_FILE)
print "Data type", data.dtype, "Shape", data.shape

plt.subplot(2, 1, 1)
plt.title("Original")
plt.plot(data)
plt.subplot(2, 1, 2)
repeated = np.tile(data, int(sys.argv[1]))
plt.title("Repeated")
plt.plot(repeated)
plt.show()
