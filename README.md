abletonian
==========

Abletonian is a free and open source alternative to Ableton Live's looping software.
Still in early development, Abletonian aims to offer all the key features of Live, and then expand into new concepts like algorithmic composition and networked collaboration.

Abletonian depends on [pyo](https://code.google.com/p/pyo/) for DSP, and [Kivy](http://kivy.org/) for graphics.
Make sure these are installed and working before attempting to use Abletonian.

To start Abletonian:

>>> python main.py

You should be presented with an interface containing scene buttons, clip buttons, and more.
To load a clip, click on a clip button and select the file to load.
To launch a scene, click on its scene button.
To switch to another scene, click on the new scene's button. The new scene will not start playing until the old scene completes.
