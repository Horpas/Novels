#Скрипты или Лейблы

label start:
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
pause 5
play sound "audio/sfx/bed.mp3"
pause 3
jump room1

label room1:
show screen room1st
with dissolve
show screen Phone
with dissolve
show screen Backpack
with dissolve
show screen TKitchen
show screen Window
show screen sofa
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
"  "

label TWindow:
hide screen Phone
hide screen Backpack
hide screen TKitchen
hide screen Window
hide screen sofa 
hide screen room1st
with dissolve
show screen room_w
with dissolve
show screen Phone
show screen Backpack
show screen ToRoom
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
"  "
$renpy.notify("Опять гроза в начале мая.")

label ToRoom:
hide screen TKitchen2
hide screen P
hide screen TFridge
hide screen Fridge
hide screen TExit
hide screen Backpack
with dissolve
hide screen Phone
with dissolve
hide screen RKitchen
with dissolve
jump room1

label BTRoom:
hide screen room_w
with dissolve
hide screen Phone
hide screen Backpack
hide screen ToRoom
show screen room1st
with dissolve
show screen Phone
with dissolve
show screen Backpack
with dissolve
show screen TKitchen
show screen Window
show screen sofa
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
"  "

label kitchen:
    
    hide screen DBexit
    hide screen Boots
    hide screen EBoot
    hide screen DTKitchen
    hide screen Window
    hide screen sofa
    hide screen TKitchen
    hide screen Backpack
    with dissolve
    hide screen Phone
    with dissolve
    hide screen Bexit
    with dissolve
    hide screen room1st
    with dissolve
    show screen RKitchen
    with dissolve
    show screen Phone
    with dissolve
    show screen Backpack
    with dissolve
    show screen TKitchen2
    show screen P
    show screen Fridge
    show screen TExit
    $renpy.sound.play("audio/sfx/rain.mp3", loop=True)
    " "
label error:
    hide screen error_message
    hide screen error_bottle
    hide screen cola
    hide screen KBack
    hide screen Phone
    hide screen Backpack
    show screen crash
    show screen error_message
    play sound "audio/sfx/error.mp3"
    $renpy.notify("Когда-нибудь я выучу Python и уберу тебя отсюда.")
    ""

label Bkitchen:
    hide screen TFridge
    hide screen error_message
    hide screen error_bottle
    hide screen cola
    hide screen KBack
    show screen RKitchen
    with dissolve
    show screen Phone
    with dissolve
    show screen Backpack
    with dissolve
    show screen TKitchen2
    show screen P
    show screen Fridge
    show screen TExit
    $renpy.sound.play("audio/sfx/rain.mp3", loop=True)
    " "

label Fridge:
    hide screen crash
    hide screen error_message
    hide screen TKitchen2
    hide screen P
    hide screen RKitchen
    hide screen Fridge
    hide screen crash
    hide screen TExit
    hide screen Phone
    hide screen Backpack
    show screen Backpack
    show screen Phone
    show screen TFridge
    with dissolve
    show screen cola
    show screen error_bottle
    show screen KBack
    $renpy.sound.play("audio/sfx/Fridge.mp3", loop=True)
    ""

label Exit:
hide screen TKitchen2
hide screen P
hide screen TFridge
hide screen Fridge
hide screen TExit
hide screen Phone
with dissolve
hide screen Backpack
with dissolve
hide screen RKitchen
with dissolve
show screen Bexit
with dissolve
show screen Phone
with dissolve
show screen Backpack
with dissolve
show screen DBexit
show screen Boots
show screen EBoot
show screen DTKitchen
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
" "