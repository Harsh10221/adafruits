stp 1
start menu -> preferences -> resbe pi confi
12c enable

stp2
sudo apt-get update
sudo apt-get upgrade

stp3
cd ~
sudo apt-get install build-essential python-dev python-smbus git
sudo apt-get install i2c-tools

stp4
cd TYIT/3-oscilloscope/
Next, clone the Adafruit git folder for the library by running.
Git clone https://github.com/adafruit/Adafruit_Python_ADS1x15
Cd Adafruit_Python_ADS1x15
Sudo python setup.py install

stp5 chcek (scope rotate)
cd examples
python simpletest.py

stp6
sudo apt-get install python-matplotlib
sudo apt-get install python-pip
sudo pip install drawnow
sudo python scope.py




code

import time
import matplotlib.pyplot as plt
from drawnow import*
import Adafruit_ADS1x15
adc=Adafruit_ADS1x15.ADS1115()
GAIN=1
val=[]
cnt=0
plt.ion()
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 Channel 0')
def makeFig():
 plt.ylim(-5000,5000)
 plt.title('Oscilloscope')
 plt.grid(True)
 plt.ylabel('ADC Ost_resultutputs')
 plt.plot(val, 'ro-', label='Channel 0')
 plt.legend(loc='lower right')

while (True):
 value=adc.get_last_result()
 print('channel 0: {0}'.format(value))

 time.sleep(0.5)
 val.append(int(value))
 drawnow(makeFig)
 plt.pause(0.000001)
 cnt=cnt+1
 if(cnt>50):
 val.pop(0)

