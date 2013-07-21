import pyo
import time

s = pyo.Server()
s.boot()
s.start()

loopdir = '/home/chrono/music/samples/drum loops/'
hitdir = '/home/chrono/music/samples/drum hits/'

sf1 = pyo.SfPlayer(loopdir+'120bpm_4b_obese_aflat_punctual.wav', speed=[1,1])
sf2 = pyo.SfPlayer(hitdir+'dundunba/dundunba.wav', speed=[1,1])

callbacks = []
callbacks.append(pyo.TrigFunc(sf1['trig'], sf1.out))
callbacks.append(pyo.TrigFunc(sf1['trig'], sf2.out))

#callback1 = pyo.TrigFunc(sf1['trig'], sf1.out)
#callback2 = pyo.TrigFunc(sf1['trig'], sf2.out)

"""
while True:
    time.sleep(1)
"""
