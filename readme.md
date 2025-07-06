## What this be?
An input viewer that vibrates your sex toys. Initially, primarily for playing Tetris (but the vibrator integration is 100% universal, and does NOT care at all what you're actually doing while this is running in the background), interacts with vibrators through [Intiface Central.](https://intiface.com/central/)

Only currently supports one toy at a time.  

Change settings to control intensity, and keybindings for the actual viewer in globals.py.
The default keybinds will probably NOT match yours, but the toy vibration functionality will work no matter what your buttons are bound to.

#### What's it do and how?
First, it connects to a locally-running Intiface Central server, and gets the connected device(s).

If there's more than one compatible device connected, it'll print them to the console and have you select which one it'll be sending vibrations to.
Just enter the number corresponding to the one you want it to control.

It starts a few threads in the mean time:
* Main thread handles all controller inputs, and deals with the actual input viewer.
* Second thread listens to all keyboard inputs.
* Third thread listens to all mouse inputs.

All inputs on any of these devices (which are read in the background) will increment the global "intensity" value by some amount.  
These amounts are explained, and can be seen and adjusted in globals.py.

By default:  
* Mouse movement increments by 0.01 every frame.
* Moving controller triggers and joysticks increment by 0.05 every frame they're moving.
* Normal buttons and the dpad increment the intensity by 1 per press.
* Every 3 seconds (granularity variable), the intensity value gets reduced by 10.

To do:  
* ~~Just make it increase intensity on ALL keyboard and controller inputs.~~  
* ~~Make it easy to rebind the relevant keys for the actual viewer part.~~  
* ~~Make it so controller inputs also map to the viewer buttons.~~  
* Make the initialization less jank.  
* Make several different input viewing scenes, for different use cases.
* Make the key binding for the visuals part a semi-automated, GUI-driven affair.
* Make per-usage profiles/scenes a thing.
* Make it so it doesn't freak the fuck out while dragging the viewer window around.
* ^ Apparently this one is impossible on Windows. Well, at least it's not my fault. Just try not to drag the window around. It doesn't really like it.