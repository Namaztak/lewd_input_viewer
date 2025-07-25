## What this be?
[TLDR quick visual demo here.](https://www.youtube.com/watch?v=iBZ0fyBmsrA)

An input viewer that vibrates your sex toys. Initially, primarily for playing Tetris (but the toy integration is 100% universal, and does NOT care at all what you're actually doing while this is running in the background), interacts with toys/machines through [Intiface Central.](https://intiface.com/central/)

Only currently supports one toy at a time.  

Change settings to control intensity, and keybindings for the actual viewer in globals.py.
The default keybinds will probably NOT match yours, but the toy vibration functionality will work no matter what your buttons are bound to.

### Requirements
* Python 3 installed. ([If you don't already have it, get it here.](https://www.python.org/downloads/))  
* Intiface Central installed and running.  
* A toy or machine that Intiface Central can control.  
* requirements.txt contains the following:  
 * [buttplug-py](https://github.com/Siege-Wizard/buttplug-py/tree/main) for interfacing with the toys  
 * [pygame](https://www.pygame.org/docs/ref/pygame.html) for the visuals and handling controller inputs  
 * [pynput](https://pypi.org/project/pynput/) for listening to the mouse and keyboard in the background  
* Trust in the fact that this all runs 100% locally and collects/saves absolutely nothing.  

### What the fuck is a python, where's the goddamn exe?
Go grab it from the releases in the sidebar. Also stop yelling at me.  
The exe is often not going to be the most up-to-date thing, cause I'm not gonna run this thing through auto-py-to-exe every time I make a small change. Downloading and running the source code is gonna be the best way to get the most recent changes.

#### What's it do and how?
First, it connects to a locally-running Intiface Central server, and gets the connected device(s).  
If there's no server running, or no toys are connected to it, it'll leave the toy empty, and from then on it's solely an input viewer.  
I'll make it so you can manually connect and/or switch toys later, but for now, it's gotta connect to a toy at its startup, or not at all.  
If you've done things out of order, just close the input viewer window, and restart the script when you have your Intiface Central server running, and at least one toy connected.

If there's more than one compatible device connected, it'll print them to the console and have you select which one it'll be sending vibrations to.
Just enter the number corresponding to the one you want it to control.  
* Note: If you've connected more than one device to Intiface Central, it doesn't necessarily list the toys in order when it asks. It just lists all connected toys, with their corresponding number. Type ONLY the number when it asks you. I'm pretty sure if you do more than that, it'll crash, because I didn't bother to sanitize user inputs for that yet.

It starts a few threads in the mean time:
* Main thread handles all controller inputs, and deals with the actual input viewer.
* Second thread listens to all keyboard inputs.
* Third thread listens to all mouse inputs.

All inputs on any of these devices (which are read in the background at all times while this is running) will increment the global "intensity" value by some amount.  
These amounts are explained, and can be seen and adjusted in globals.py.

By default:  
* Mouse movement increments by 0.02 every frame.
* Scrolling increments by 0.3
* Moving controller triggers and joysticks increment by 0.05 every frame they're moving.
* Normal buttons, dpad, keyboard keystrokes, and mouse clicks each increment the intensity by 1 per press.  
* Every 3 seconds (granularity variable), the intensity value gets reduced by 10.

#### Donate?

If this thing does good stuff for you, [toss me a buck or few](https://ko-fi.com/nam_137), would ya?

To do:  
* ~~Just make it increase intensity on ALL keyboard and controller inputs.~~  
* ~~Make it easy to rebind the relevant keys for the actual viewer part.~~  
* ~~Make it so controller inputs also map to the viewer buttons.~~  
* Make the initialization less jank.  
* Make several different input viewing scenes, for different use cases.
* Make the key binding for the visuals part a semi-automated, GUI-driven affair.
* Make per-usage profiles/scenes a thing.
    * Cleaned up icon naming/handling so people can just make their own sets of icons.
* Make it so it doesn't freak the fuck out while dragging the viewer window around.
    * ^ Apparently this one is impossible on Windows. Well, at least it's not my fault. Just try not to drag the window around. It doesn't really like it.
    * Your PC is gonna freak out a bit while you drag the window, then it'll chill again. What's happening is it's pausing all the threads while you're moving the window, and since one of those threads is directly tied to your mouse input, it gets upset. After you set the window back down wherever you want it, it'll work fine again. But since this program doesn't need to be in the foreground, neither for the input listening, nor capturing its visuals in OBS or whatever, you can realistically just cover it up with whatever other programs you're running and forget it exists. If you don't care about having it handle your mouse inputs, and you'd prefer to fix this issue completely, go into main.py and comment out the mouse thread lines.

### Make your own icons?

Make the icons 50x50 pngs and name them the same things as you see in the included icons folder(s).  
Whatever set of icons you wanna use, just have them in a folder called "icons" in the root directory.  
If you wanna hide a button you're not using, just put empty pngs in the folder and make sure they have the names of where they should go in the viewer, or the viewer will get upset and not run.
