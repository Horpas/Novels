define radio = 0
define stlight = 0

label drivee:
$renpy.notify("Ну что, поехали...")
show screen BS
with slow_dissolve
stop music fadeout 1.0
hide bg street
hide screen street
hide screen gostop
hide screen car
hide screen win
hide screen rainn
jump ICar

label ICar:
show screen driving
show screen beep
show screen radio
show screen bardachok
show screen TCity
show screen BTHomeA
hide screen BS
with dissolve
" "

label radio:
play music("audio/ost/p2/gruppa_krovi.mp3") fadeout 1.0
$renpy.notify("Кайф...")
$radio += 1

if radio == 2:
    stop music fadeout 0.5
    $renpy.notify("Достаточно классики.")
    $radio = 0
jump ICar

label TCrossroad:
hide screen bardachok
hide screen radio
hide screen beep
show screen BS
with dissolve
hide screen TCity
hide screen BTHomeA
show screen crossroad
show screen sign
show stLight
show screen Red
hide screen BS 
with dissolve
" "
label r_strlight:
hide screen Green
screen strlightR():
    timer 10.0 action Jump(y_strlight)

label y_strlight:
hide screen Red
screen strlightR():
timer 3.0 action Jump(g_strlight)

lable g_strlight:
hide screen Yellow
screen strlightG():
timer 15.0 action Jump(y_strlight)
