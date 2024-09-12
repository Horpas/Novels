#Экраны, спрайты

screen sofa:
    imagebutton:
        xpos 0
        ypos 688
        idle "images/sprites/p1/Room1/Sofa.png"
        hover "images/sprites/p1/Room1/Sofa_hover.png"
        hover_sound "sfx/room.mp3"
        activate_sound "sfx/room.mp3"
        action MainMenu()

    zorder 2

screen TKitchen:
    imagebutton:
        xpos 1598
        ypos 92
        idle "images/sprites/p1/Room1/K_door.png"
        hover "images/sprites/p1/Room1/K_door_hover.png"
        hover_sound "sfx/K_hover.mp3"
        activate_sound "sfx/move.mp3"
        action Jump("kitchen")

    zorder 2

screen DTKitchen:
    imagebutton:
        xpos 450
        ypos 0
        idle "images/sprites/p1/Exit/DTKitchen.png"
        hover "images/sprites/p1/Exit/DTKitchen_hover.png"
        hover_sound "sfx/K_hover.mp3"
        activate_sound "sfx/move.mp3"
        action Jump("kitchen")

    zorder 2

screen DBexit:
    imagebutton:
        xpos 1317
        ypos 81
        idle "images/sprites/p1/Exit/Bexit.png"
        hover "images/sprites/p1/Exit/Bexit_hover.png"
        hover_sound "sfx/Exit.mp3"
        action Notify("Оставлять квартиру открытой - так себе идея.")

    zorder 2

screen Boots:
    imagebutton:
        xpos 898
        ypos 832
        idle "images/sprites/p1/Exit/Boots.png"
        hover "images/sprites/p1/Exit/Boots_hover.png"
        hover_sound "sfx/boots.mp3"
        activate_sound "sfx/Eboot.mp3"
        action Notify("Чьи это кроссовки?")

    zorder 2

screen EBoot:
    imagebutton:
        xpos 1240
        ypos 844
        idle "images/sprites/p1/Exit/EBoot.png"
        hover "images/sprites/p1/Exit/EBoot_hover.png"
        hover_sound "sfx/Eboot.mp3"
        activate_sound "sfx/Eboot.mp3"
        action Notify("О, нашёлся!")

    zorder 2

screen TKitchen2:
    imagebutton:
        xpos 98
        ypos 174
        idle "images/sprites/p1/Kitchen/door.png"
        hover "images/sprites/p1/Kitchen/door_hover.png"
        hover_sound "sfx/room.mp3"
        activate_sound "sfx/move.mp3"
        action Jump("ToRoom")

    zorder 2

screen P:
    imagebutton:
        xpos 520
        ypos 362
        idle "images/sprites/p1/Kitchen/p.png"
        hover "images/sprites/p1/Kitchen/p_hover.png"
        hover_sound "sfx/P.mp3"
        activate_sound "sfx/P_move.mp3"
        action Notify("Просто портрет моей мамы.")

    zorder 2

screen Fridge:
    imagebutton:
        xpos 1698
        ypos 365
        idle "images/sprites/p1/Kitchen/F.png"
        hover "images/sprites/p1/Kitchen/F_hover.png"
        hover_sound "sfx/Fridge_opened.mp3"
        activate_sound "sfx/Fridge_hover.mp3"
        action Jump("Fridge")

    zorder 2

screen error_message:
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "images/sprites/p1/Fridge/error_message.png"
        activate_sound "sfx/click.mp3"
        action Jump("Fridge")

    zorder 2

screen error_bottle:
    imagebutton:
        xpos 1177
        ypos 99
        idle "images/sprites/p1/Fridge/Orange_juice.png"
        hover "images/sprites/p1/Fridge/Orange_juice_hover.png"
        hover_sound "sfx/error_hover.mp3"
        activate_sound "sfx/error_hover.mp3"
        action Jump("error")

    zorder 2

screen Window:
    imagebutton:
        xpos 458
        ypos 187        
        idle "images/sprites/p1/Room1/Window.png"
        hover "images/sprites/p1/Room1/Window_hover.png"
        hover_sound "sfx/window.mp3"
        activate_sound "sfx/move.mp3"
        action Jump("TWindow")
    zorder 2

screen cola:
    imagebutton:
        xpos 205
        ypos 388        
        idle "images/sprites/p1/Fridge/Cola.png"
        hover "images/sprites/p1/Fridge/Cola_hover.png"
        hover_sound "sfx/cola_hover.mp3"
        activate_sound "sfx/cola.mp3"
        action Notify("Кайф...")
    zorder 2

screen drawer:
    imagebutton:
        xpos 1382
        ypos 660        
        idle "images/sprites/p1/Kitchen/drawer_door.png"
        hover "images/sprites/p1/Kitchen/drawer_door_hover.png"
        hover_sound "sfx/drawer_hover.mp3"
        activate_sound "sfx/drawer.mp3"
        action Jump("TDrawer")
    zorder 2

screen glass:
    imagebutton:
        xpos 1357
        ypos 452        
        idle "images/sprites/p1/Drawer/glass.png"
        hover "images/sprites/p1/Drawer/glass_hover.png"
        hover_sound "sfx/cape_hover.mp3"
        activate_sound "sfx/cape_click.mp3"
        action Notify("Это крышка от термоса, который я благополучно потерял.")
    zorder 2

screen glass2:
    imagebutton:
        xpos 1063
        ypos 33       
        idle "images/sprites/p1/Drawer/glass2.png"
        hover "images/sprites/p1/Drawer/glass2_hover.png"
        hover_sound "sfx/glass_hover.mp3"
        activate_sound "sfx/glass.mp3"
        action Notify("Горшочек больше не варит...")
    zorder 2   

screen tubus:
    imagebutton:
        xpos 1424
        ypos 65      
        idle "images/sprites/p1/Drawer/tubus.png"
        hover "images/sprites/p1/Drawer/tubus_hover.png"
        hover_sound "sfx/tubus_hover.mp3"
        action Notify("Тубусы. Незаменимы в краже кофе у соседа.")
    zorder 2

screen MW:
    imagebutton:
        xpos 1616
        ypos 357      
        idle "images/sprites/p1/Kitchen/MW.png"
        hover "images/sprites/p1/Kitchen/MW_hover.png"
        hover_sound "sfx/MW.mp3"
        activate_sound "sfx/egg.mp3"
        action Notify("Опять забыл яйца вытащить...")
    zorder 2

screen servicee:
    imagebutton:
        xpos 240
        ypos 530      
        idle "images/sprites/p1/Drawer/service.png"
        hover "images/sprites/p1/Drawer/service_hover.png"
        hover_sound "sfx/spoons.mp3"
        activate_sound "sfx/spoons.mp3"
        action Notify("Зачем холостяку столько сервиса?")
    zorder 2

screen error_message2:
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "images/sprites/p1/Drawer/error_message.png"
        activate_sound "sfx/click.mp3"
        action Jump("TDrawer")

    zorder 2

screen spoon:
    imagebutton:
        xpos 746
        ypos 750
        idle "images/sprites/p1/Drawer/spoon.png"
        hover "images/sprites/p1/Drawer/spoon_hover.png"
        hover_sound "sfx/spoons.mp3"
        activate_sound "sfx/spoons.mp3"
        action Notify("Сейчас она мне ни к чему.")

    zorder 2

screen error_plate:
    imagebutton:
        xpos 226
        ypos 413
        idle "images/sprites/p1/Drawer/plate.png"
        hover "images/sprites/p1/Drawer/plate_hover.png"
        hover_sound "sfx/error_hover.mp3"
        activate_sound "sfx/error_hover.mp3"
        action Jump("error2")

    zorder 3

# Интерфейс

screen KBack:
    imagebutton:
        ypos 1000
        xpos 760       
        idle "images/sprites/Back.png"
        hover "images/sprites/Back_hover.png"
        hover_sound "sfx/hover.mp3"
        activate_sound "sfx/Fridge_closed.mp3"
        action Jump("Bkitchen")
    zorder 15

screen TExit:
    imagebutton:
        ypos 1000
        xpos 760       
        idle "images/sprites/Back.png"
        hover "images/sprites/Back_hover.png"
        hover_sound "sfx/hover.mp3"
        activate_sound "sfx/move.mp3"
        action Jump("Exit")
    zorder 15

screen Phone:
    imagebutton:
        ypos 726
        xpos 58      
        idle "images/sprites/Phone.png"
        hover "images/sprites/Phone_hover.png"
        hover_sound "sfx/phone.mp3"
        activate_sound "sfx/phone_hover.mp3"
        action MainMenu()

    zorder 15

screen Backpack:
    imagebutton:
        ypos 40
        xpos 40     
        idle "images/sprites/Backpack.png"
        hover "images/sprites/Backpack_hover.png"
        hover_sound "sfx/Backpack_hover.mp3"
        activate_sound "sfx/Backpack.mp3"
        action Notify("Пусто...")

    zorder 15

screen ToRoom:
    imagebutton:
        ypos 1000
        xpos 760       
        idle "images/sprites/Back.png"
        hover "images/sprites/Back_hover.png"
        hover_sound "sfx/hover.mp3"
        activate_sound "sfx/click.mp3"
        action Jump("BTRoom")
    zorder 15

screen TKitchen3:
    imagebutton:
        ypos 1000
        xpos 760       
        idle "images/sprites/Back.png"
        hover "images/sprites/Back_hover.png"
        hover_sound "sfx/hover.mp3"
        activate_sound "sfx/drawer_close.mp3"
        action Jump("BTK")
    zorder 15

# Фоны

screen room1st:
    modal True
    zorder 1
    
    fixed:
        xsize 1920 ysize 1080
        add "images/bg/p1/bg room1.png" align (.5,.5)

screen room_w:
    modal True
    zorder 1

    fixed:
        xsize 1920 ysize 1080
        add "images/bg/p1/bg window.png" align (.5,.5)

screen RKitchen:
    modal True
    zorder 1
    
    fixed:
        xsize 1920 ysize 1080
        add "images/bg/p1/bg kitchen.png" align (.5,.5)

screen TFridge:
    modal True
    zorder 1
    
    fixed:
        xsize 1920 ysize 1080
        add "images/bg/p1/bg fridge.png" align (.5,.5)

screen crash:
    modal True
    zorder 1
    
    fixed:
        xsize 1920 ysize 1080
        add "images/sprites/p1/Fridge/Crash.png" align (.5,.5)

screen crash2:
    modal True
    zorder 1
    
    fixed:
        xsize 1920 ysize 1080
        add "images/sprites/p1/Drawer/crash2.png" align (.5,.5)


screen Bexit:
    modal True
    zorder 1
    
    fixed:
        xsize 1920 ysize 1080
        add "images/bg/p1/bg exit.png" align (.5,.5)

screen Idrawer:
    modal True
    zorder 1
    
    fixed:
        xsize 1920 ysize 1080
        add "images/bg/p1/bg drawer.png" align (.5,.5)