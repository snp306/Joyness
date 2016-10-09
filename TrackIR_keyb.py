#Title           :Keyb trackIR FreePIE python script
#Version         :0.2 (2016-10-08)
#Author          :snp
#Description     :FreePIE python script for flight sims. Provides keyboard support via trackIR.

from System import Int16

if starting:
   trackIR.x = 0
   trackIR.y = 0
   trackIR.z = 0
   x = 0
   y = 0
   z = 0
   position = 0
   sequence = 0

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

x = clamp(x, -15, 15)
y = clamp(y, 0, 9)
z = clamp(z, -40, 30)

if keyboard.getKeyDown(Key.N):
   z = z - 0.2
   trackIR.z = z

if keyboard.getKeyDown(Key.J):
   z = z + 0.2
   trackIR.z = z

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

trackIR.x = x
trackIR.y = y
trackIR.z = z
   
diagnostics.watch(trackIR.x)
diagnostics.watch(trackIR.y)
diagnostics.watch(trackIR.z)
