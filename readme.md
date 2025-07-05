## What this be?
An input viewer, presently primarily for playing Tetris, that also interacts with vibrators through [Intiface Central.](https://intiface.com/central/)

Only currently supports one toy at a time.  

Change your keybinds in globals.py

#### What's it do and how?
It starts a few threads:
* Main thread handles all controller inputs
* Second thread listens to all keyboard inputs
* Third thread listens to all mouse inputs

All inputs on any of these devices (which are read in the background) will increment the global "intensity" value by some amount.  
The way I've set it up, all buttons, dpad movement, keystrokes, and mouse clicks increment the value by 1.0.  
Mouse movement increments by 0.01 every frame.
Controller triggers and joysticks moving increments by 0.2 every frame

Every 3 seconds, the intensity value, by default, 

To do:  
* ~~Just make it increase intensity on ALL keyboard and controller inputs.~~  
* ~~Make it easy to rebind the relevant keys for the actual viewer part.~~  
* ~~Make it so controller inputs also map to the viewer buttons.~~  
* Make the initialization less jank.  
* Make several different input viewing scenes, for different use cases.
* Make the key binding part an automated, GUI-driven affair.
* Make per-usage profiles a thing.