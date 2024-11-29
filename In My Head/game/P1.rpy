#Скрипты или Лейблы

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define slow_dissolve = Dissolve(1.0)
define keys = False
define bottle = False
define Gopstop_B = True

label start:
stop music fadeout 1.0
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
pause 5
play sound "audio/sfx/bed.mp3"
pause 3
show screen BS
with dissolve
jump room1

label room1:
show screen room1st
show screen Phone
show screen Backpack
show screen TKitchen
show screen Window
show screen sofa
if keys == False:
    show screen keys
else:
    hide screen keys
hide screen BS
with dissolve
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
"  "
label KeI:
$renpy.notify("Пригодится.")
$renpy.sound.play("audio/sfx/Backpack.mp3")
hide screen keys
with dissolve
$keys = True
jump room1

label TWindow:
show screen BS
with dissolve
hide screen Phone
hide screen Backpack
hide screen TKitchen
hide screen Window
hide screen sofa
hide screen keys 
hide screen room1st
show screen room_w
show screen Phone
show screen Backpack
show screen ToRoom
hide screen BS
with dissolve
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
$renpy.notify("Опять гроза в начале мая.")
"  "
label ToRoom:
show screen BS
with dissolve
hide screen TKitchen2
hide screen P
hide screen MW
hide screen drawer
hide screen TFridge
hide screen Fridge
hide screen TExit
hide screen RKitchen
jump room1

label BTRoom:
show screen BS
with dissolve
hide screen room_w
hide screen ToRoom
show screen room1st
show screen TKitchen
show screen Window
show screen sofa
if keys == False:
    show screen keys
else:
    hide screen keys
hide screen BS
with dissolve
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
"  "

label BotI:
$renpy.notify("Пригодится.")
$renpy.sound.play("audio/sfx/Backpack.mp3")
hide screen Bottle
with dissolve
$bottle = True
jump Fridge

label kitchen:
    show screen BS 
    with dissolve
    hide screen DBexit
    hide screen Boots
    hide screen EBoot
    hide screen DTKitchen
    hide screen Window
    hide screen sofa
    hide screen keys
    hide screen TKitchen
    hide screen Bexit
    hide screen room1st
    show screen RKitchen
    show screen TKitchen2
    show screen P
    show screen drawer
    show screen MW
    show screen Fridge
    show screen TExit
    hide screen BS
    with dissolve
    $renpy.sound.play("audio/sfx/rain.mp3", loop=True)
    " "
label errorK:
    hide screen error_message
    hide screen Bottle 
    hide screen error_bottle
    hide screen cola
    hide screen KBack
    hide screen Phone
    if bottle == False:
        show screen Crash2
    else:
        show screen Crash1
    hide screen Backpack
    show screen error_message
    play sound "audio/sfx/error.mp3"
    $renpy.notify("Когда-нибудь я выучу Python и уберу тебя отсюда.")
    ""

label error2:
    hide screen Idrawer
    hide screen spoon
    hide screen Phone
    hide screen Backpack
    hide screen TKitchen3
    hide screen glass
    hide screen glass2
    hide screen tubus
    hide screen error_plate
    hide screen servicee
    hide screen TKitchen2
    hide screen error_message2
    hide screen crash2
    show screen error_message2
    show screen crash2
    play sound "audio/sfx/error.mp3"
    $renpy.notify("Когда-нибудь я выучу Python и уберу тебя отсюда.")
    ""

label Bkitchen:
    hide screen TFridge
    hide screen error_message
    hide screen error_bottle
    hide screen Bottle
    hide screen cola
    hide screen KBack
    show screen RKitchen
    show screen Phone
    show screen Backpack
    show screen TKitchen2
    show screen P
    show screen Fridge
    show screen TExit
    show screen drawer
    show screen MW
    $renpy.sound.play("audio/sfx/rain.mp3", loop=True)
    " "

label Fridge:
    hide screen Crash1
    hide screen Crash2
    hide screen error_message
    hide screen TKitchen2
    hide screen drawer
    hide screen MW
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
    show screen cola
    if bottle == False:
        show screen Bottle
    else:
        hide screen Bottle
    show screen error_bottle
    show screen KBack
    $renpy.sound.play("audio/sfx/Fridge.mp3", loop=True)
    ""

label TExit:
show screen BS
with dissolve
hide screen Bottle
hide screen TKitchen2
hide screen drawer
hide screen MW
hide screen P
hide screen TFridge
hide screen Fridge
hide screen TExit
hide screen RKitchen

label Exit:
show screen Bexit
show screen DBexit
show screen Boots
show screen EBoot
show screen DTKitchen
hide screen BS
with dissolve
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
" "

label BTK:
hide screen TKitchen3
hide screen crash2
hide screen glass
hide screen glass2
hide screen tubus
hide screen servicee
hide screen spoon
hide screen error_plate
hide screen Idrawer
jump Bkitchen

label TDrawer:
hide screen Idrawer
hide screen spoon
hide screen TKitchen3
hide screen glass
hide screen glass2
hide screen tubus
hide screen error_plate
hide screen servicee
hide screen TKitchen2
hide screen error_message2
hide screen crash2
hide screen MW
hide screen P
hide screen TFridge
hide screen Fridge
hide screen drawer
hide screen TExit
hide screen RKitchen
show screen Idrawer
show screen spoon
show screen TKitchen3
show screen glass
show screen glass2
show screen tubus
show screen error_plate
show screen servicee
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
" "

label podyezd:
show screen BS
with dissolve
hide screen WWhite
hide screen DBexit
hide screen Boots
hide screen EBoot
hide screen DTKitchen
hide screen Bexit
show screen Podyezd
jump podezd

label podezd:
show screen Tyard
show screen winda
show screen Thome
show screen rozetka
show screen heater
hide screen BS 
with dissolve
$renpy.sound.play("audio/sfx/rain.mp3", loop=True)
" "

label ban:
$renpy.notify("Ай! Да кто делает розетки в подъезде?!")
play sound("audio/sfx/rozetka.mp3")
show screen WWhite
with flashbulb
hide screen WWhite
with dissolve
jump podezd

label TExit2:
show screen BS 
with dissolve
hide screen Tyard
hide screen WWhite
hide screen winda
hide screen Thome
hide screen rozetka
hide screen heater
hide screen Podyezd
jump Exit

label street:
show screen BS 
with dissolve
hide screen Tyard
hide screen WWhite
hide screen winda
hide screen Thome
hide screen rozetka
hide screen heater
hide screen Podyezd
jump Strt2

label Strt2:
show screen street
show screen gostop
show screen car
show screen win
show screen rainn
hide screen BS 
with dissolve
play music "audio/ost/p1/na_zare.mp3" fadeout 1.0
""

label gopstop:
if Gopstop_B == True:
    hide screen BS
    hide screen gostop
    with dissolve
    hide screen rainn
    hide screen car
    hide screen win
    hide screen street
    show bg street
    play sound "sfx/gopstop_talking.mp3"
    show v with dissolve
    jump G_battle
    label G_battle:  
    menu:
        V "Опять ты?"

        "Чего тебе?":
            play sound "sfx/gopstop_talking.mp3"
            V "Не строй из себя дебила."
            V "Чё по мелочи сегодня?"

        "Отвали.":
            play sound "sfx/gopstop_talking.mp3"
            V "В бубен захотел, умник?"
            V "Чё по мелочи сегодня?"

        "Твоя машина у выезда?":
            play sound "sfx/gopstop_talking.mp3"
            V "Ха!{w} Делать мне нечего!"
            V "Чё по мелочи сегодня?"
else:
    $renpy.notify("Лучше не трогать его.")

label G_battle2:
menu:
    V "Алё? Я тебя спрашиваю!"

    "Сегодня пусто":
        $renpy.notify("А потом прыгать...")
        jump G_battle2

    "Выпить хочешь?":
        if bottle == False:
            $renpy.notify("А что ему предложить?")
            jump G_battle2
        else:
            $bottle = False
            $renpy.sound.play("audio/sfx/cola.mp3")
            V "Уговорил...кыш отсюда."
            hide v with dissolve
            $Gopstop_B = False 
            jump Strt2

    "Слушай, угомонись.":
        play sound "sfx/gopstop_talking.mp3"
        V "Ты как разговариваешь с грозой улиц?"
        V "Харе уплывать от вопроса."
        jump G_battle2
