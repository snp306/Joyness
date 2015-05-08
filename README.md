# Joyness
Scripts for flight sims
-------
Mjoy.py - FreePIE python script for flight sims. Provides mouse and keyboard support via vJoy device driver and some other features.
Tested with IL-2: Cliffs of Dover and Rise of Flight, but should work with other games as well. 

AxisWinToogle.ahk - AutoHotkey script for toogling axis window. Made for Joystick Curves. 
Game needs to run in the fullscreen window mode.

Features
--------

- Mjoy/keyb virtual joystick
- Rudder and Brakes keyb axes
- Toogleble FOV zoom
- Mousewheel throttle

Preparation
-----------

Get vJoy, Joystick Curves, FreePIE and AutoHotkey. Configure your sim keys/axes accordingly to the script (or vice versa).
Joystick Curves initializes vJoy when starting, so run the Mjoy script first.

Notes
-----

Mjoy defaults:

WASD				- Elevator, roll
QE				- Rudder
X				- Brakes
Alt				- Looking around
Space				- X/Y axis centering
MiddleMouseButton		- Custom zoom toogle for CoD
Mousewheel			- Custom throttle for CoD

CoD:

Camera Control in Ind Mode	:Alt
Snap Forward			:Alt
Throttle 			:Alt; 3,4

Use Snap Mode.

Make sure axes look like this:

Documents\1C SoftClub\il-2 sturmovik cliffs of dover - MOD\confUser.ini

[HotKey pilotMove]
- Joystick+AXE_Z=1brakes
- Joystick+AXE_RZ=1rudder
- Joystick+AXE_Y=1elevator
- Joystick+AXE_X=1aileron

RoF:

- Camera pitch			:Lalt + mouse y
- Camera yaw			:Lalt + mouse x
- Head vertical turn		:Lalt + mouse y
- Head horizontal turn		:Lalt + mouse x
- Head Snap Center		:middle mouse
- Engine Start			:I

Known Issues
------------
Mouse sensitivity is dependand on screen resolution, if set too low limits the onscreen virtual joystick range.

snp306 <snappyslicer gmail com> 05-May-2015
