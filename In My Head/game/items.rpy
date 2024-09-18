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
" "

label CloseInventory:
hide screen IBottle
hide screen Closee
hide screen Inventory
" "