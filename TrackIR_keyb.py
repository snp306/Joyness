#Title           :Keyb trackIR FreePIE python script
#Version         :0.1 (2015-05-15)
#Author          :snp
#Description     :FreePIE python script for flight sims. Provides keyboard support via trackIR.

from System import Int16

if starting:
   trackIR.x = 0
   trackIR.y = 0
   x = 0
   y = 0
   position = 0
   sequence = 0
   
if x > 30:
   x = 30

if x < -30:
   x = -30 
 
if y > 5:
   y = 5

if y < -30:
   y = -30

if keyboard.getPressed(Key.X):
   if sequence == 0:
      position = 10 #For Bf 109 :) 
   elif sequence == 1:
      position = 0

   sequence = sequence + 1
   if sequence > 1:
      sequence = 0

if keyboard.getKeyDown(Key.Z):
   x = x - 0.2
   trackIR.x = x
   
if keyboard.getKeyUp(Key.C):
   if keyboard.getKeyUp(Key.Z):
      trackIR.x = position
      x = position

if keyboard.getKeyDown(Key.C):
   x = x + 0.2
   trackIR.x = x
      
if keyboard.getKeyDown(Key.D1):
   y = y - 0.01
   trackIR.y = y
   
if keyboard.getKeyDown(Key.D2):
   y = y + 0.01
   trackIR.y = y

if keyboard.getKeyDown(Key.LeftAlt): # Sometimes view resets to default position for "no reason" and this fixes it.
   x = x + 0.2
   trackIR.x = x

trackIR.y = y
   
diagnostics.watch(trackIR.x)
diagnostics.watch(trackIR.y)
