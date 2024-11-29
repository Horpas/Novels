screen Inventory:
    modal True
    zorder 14
    
    fixed:
        add "images/sprites/inventory.png" align (.5,.5)

screen IBottle:
    imagebutton:
        xpos 656
        ypos 256       
        idle "images/items/Juice.png"
        hover "images/items/Juice_hover.png"
        hover_sound "sfx/bottle_hover.mp3"
        action Notify("Я пока пить не хочу.")
    zorder 14

label OpenInventory:
show screen Inventory
show screen Closee
if bottle == True:
    show screen IBottle
else:
    hide screen IBottle
if keys == True:
    show screen IKeys
else:
    hide screen IKeys
" "

label CloseInventory:
hide screen IBottle
hide screen IKeys
hide screen Closee
hide screen Inventory
" "
screen IKeys:
    imagebutton:
        xpos 877
        ypos 256       
        idle "images/items/keys.png"
        hover "images/items/keys_hover.png"
        hover_sound "sfx/spoons.mp3"
        action Notify("Осталось дойти до машины.")
    zorder 14