; Toggles Always On Top & Titlebar
!^=::
Winset, Alwaysontop, Toggle, Joystick
WinSet, Style, ^0xC00000, Joystick
return

; Show/Hide Toogle Window
!^-::
IfWinExist, Joystick
 WinHide
Else
 WinShow, Joystick
return
