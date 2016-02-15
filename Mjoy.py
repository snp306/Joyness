#Title         :Mjoy vJoy FreePIE python script
#Version       :0.3 (2016-02-15)
#Author        :snp
#Description   :FreePIE python script for flight sims. Provides mouse and keyboard support via vJoy device driver and some other features.

import time
from System import Int16
from ctypes import windll, Structure, c_ulong, byref

class POINT(Structure):
   _fields_ = [("x", c_ulong), ("y", c_ulong)]

if starting:
   vJoy0_stat = 1
   vJoy[0].x = 0
   vJoy[0].y = 0
   vJoy[0].z = 0
   vJoy[0].rz = 0
   x = 0
   y = 0
   z = 0
   rz = 0
   mouse_x = 0
   mouse_y = 0
   mouse_x_locked = 0
   mouse_y_locked = 0
   x_m = 0
   y_m = 0
   axis_max = 16448
   screen_x = windll.user32.GetSystemMetrics(0)
   screen_y = windll.user32.GetSystemMetrics(1)
   pt = POINT()   
   sequence = 0
   system.setThreadTiming(TimingTypes.HighresSystemTimer)
   system.threadExecutionInterval = 1

# Mouse looking around

if keyboard.getPressed(Key.LeftAlt):
   mouse_x_locked = pt.x
   mouse_y_locked = pt.y

if keyboard.getKeyDown(Key.LeftAlt):
   windll.user32.SetCursorPos((mouse_x_locked),(mouse_y_locked))

# Lock key

if keyboard.getPressed(Key.End):
   mouse_x_locked = pt.x
   mouse_y_locked = pt.y

if keyboard.getKeyDown(Key.End):
   windll.user32.SetCursorPos((mouse_x_locked),(mouse_y_locked))

# Il2 CoD - Mousewheel throttle

if mouse.wheelUp:
   keyboard.setPressed(Key.D4)
      
if mouse.wheelDown:
   keyboard.setPressed(Key.D3)

# Il2 CoD - Toogleable FOV zoom
# Doesn't work with middleButton directly

if mouse.middleButton:
   keyboard.setPressed(Key.PageUp)

if keyboard.getPressed(Key.PageUp):
   if sequence == 0:
      keyboard.setPressed(Key.D7)   
   elif sequence == 1:
      keyboard.setKeyDown(Key.LeftControl)
      time.sleep(1)
      keyboard.setKeyUp(Key.LeftControl)
      
   sequence = sequence + 1
   if sequence > 1:
      sequence = 0

# Rudder control

if rz > axis_max:
   rz = axis_max
   
if rz < - axis_max:
   rz = - axis_max

if keyboard.getKeyDown(Key.Q):
   rz = rz - 60

if keyboard.getKeyUp(Key.E):
   if keyboard.getKeyUp(Key.Q):
      if rz > 0:
         rz = rz - 60
      if rz < 0:
         rz = rz + 60
      
if keyboard.getKeyDown(Key.E):
   rz = rz + 60

vJoy[0].rz = rz

# Brakes control

if z > axis_max:
   z = axis_max
   
if z < - axis_max:
   z = - axis_max

if keyboard.getKeyDown(Key.X):
   z = z + 100
   vJoy[0].z = z

if keyboard.getKeyUp(Key.X):
   z = -axis_max
   vJoy[0].z = -axis_max
   
# X/Y axis centering

if keyboard.getKeyDown(Key.Space):
   windll.user32.SetCursorPos((screen_x / 2),(screen_y / 2))

# Mjoy vJoy

#Turn VJoy on/off

if keyboard.getPressed(Key.K):
   if sequence == 0:
      vJoy0_stat = 1   
   elif sequence == 1:
      vJoy0_stat = 0
      
   sequence = sequence + 1
   if sequence > 1:
      sequence = 0
   
if vJoy0_stat == 1:
   windll.user32.GetCursorPos(byref(pt))
   mouse_x = pt.x
   mouse_y = pt.y
   sensitivity = 32
   x_m = (mouse_x - (screen_x / 2)) * sensitivity
   y_m = (mouse_y - (screen_y / 2)) * sensitivity
   x_both = x_m + x
   y_both = y_m + y
   x_keyb_sensitivity = 65
   y_keyb_sensitivity = 20
   
   if x_m > axis_max:
      x_m = axis_max
   
   if x_m < - axis_max:
      x_m = - axis_max
      
   if y_m > axis_max:
      y_m = axis_max
   
   if y_m < - axis_max:
      y_m = - axis_max
   
   if x > axis_max:
      x = axis_max
   
   if x < - axis_max:
      x = - axis_max
      
   if y > axis_max:
      y = axis_max
   
   if y < - axis_max:
      y = - axis_max
      
   if x_both > axis_max:
      x_both = axis_max
   
   if x_both < - axis_max:
      x_both = - axis_max
      
   if y_both > axis_max:
      y_both = axis_max
   
   if y_both < - axis_max:
      y_both = - axis_max
      
   if keyboard.getKeyDown(Key.A):
      x = x - x_keyb_sensitivity
      keyboard.setPressed(Key.End)

   if keyboard.getKeyUp(Key.D):
      if keyboard.getKeyUp(Key.A):
         if x > 0:
            x = x - x_keyb_sensitivity
         if x < 0:
            x = x + x_keyb_sensitivity

   if keyboard.getKeyDown(Key.D):
      x = x + x_keyb_sensitivity
      keyboard.setPressed(Key.End)
      
   if keyboard.getKeyDown(Key.W):
      y = y - y_keyb_sensitivity
      keyboard.setPressed(Key.End)

   if keyboard.getKeyUp(Key.S):
      if keyboard.getKeyUp(Key.W):
         if y > 0:
            y = y - y_keyb_sensitivity
         if y < 0:
            y = y + y_keyb_sensitivity

   if keyboard.getKeyDown(Key.S):
      keyboard.setPressed(Key.End)
      y = y + y_keyb_sensitivity

   vJoy[0].x = x_both
   vJoy[0].y = y_both

# Diag

diagnostics.watch(screen_x)
diagnostics.watch(screen_y)
diagnostics.watch(mouse_x)
diagnostics.watch(mouse_y)
diagnostics.watch(mouse_x_locked)
diagnostics.watch(mouse_y_locked)
diagnostics.watch(vJoy[0].x)
diagnostics.watch(vJoy[0].y)
diagnostics.watch(vJoy[0].z)
diagnostics.watch(vJoy[0].rz)
