# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define m = Character('???', color="#8fbc8f")
define m2 = Character('[m_name]', color="#8fbc8f")
define L = Character('Одиночество', color="#8b0000")
define K = Character('Кудесник', color="#191970")
define LL = Character('Ложь', color="#8b0000")
define M = Character('Мама', color="#00FF00")
define S = Character('София', color="#FF4500")
define A = Character(None, kind=nvl)
define B = Character('Анна', color="#C71585")
define AN = Character('Антон', color="#8B0000")
define slow_dissolve = Dissolve(1.0)
define fast_dissolve = Dissolve(0.2)
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define Notebook = False
define 1st_page = False

screen Notebook:
        imagebutton:
            xalign 0.98
            yalign 0.01
            idle "images/sprites/notebook.png"
            hover "images/sprites/notebook_hover.png"
            action Notify("Там пока ничего нет.")
screen Menu:
        imagebutton:
            xalign 0.01
            yalign 0.98
            idle "images/sprites/menu.png"
            hover "images/sprites/menu_hover.png"
            action MainMenu()

screen Phone:
        imagebutton:
            xalign 0.01
            yalign 0.01
            idle "images/sprites/phone.png"
            hover "images/sprites/phone_hover.png"
            action Notify("Он мне пока не нужен.")
    
screen chapter1:
    text "{b}ДЕНЬ 1.{/b} \n {size=30}Знакомство.":
        xalign 0.5 yalign 0.5
        size 50
 
screen School:
    text "{b}08:10{/b}":
        xalign 0.5 yalign 0.5
        size 50
  
    
    
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    
     scene black
     window hide
    
     A '''
Вот и начинается наша история...

Прежде, чем мы начнём, напомню, что эта новелла сделана на основе реальных каракуль, которые писал когда-то автор.

Сейчас у него всё нормально.{w} Наверное.

Во всяком случае, приятной игры!
     '''
     
     nvl hide
     
     show bg river_evening
     with slow_dissolve
     play music "audio/Music/Evening.mp3" fadeout 1.0
     play sound "audio/Sounds/Riverside.mp3"
     
     m "Что-ж."
     
     m "Возможно, сегодня, я наконец-то отдохну, как следует."
     "..."
     
     "Нет. Боюсь, что не отдохну."
     
     "Опять он..."
     
     L "Cкучал?"
     
     show Lone_N
     with dissolve
     
     "Передо мной возникла высокая тёмная фигура Демона. Глаза были идеально белые; руки тонкие, как палочки."
     
     "Жуть, простыми словами."
     
     hide Lone_N  
     show Lone_H
     
     L "Наслаждаешься солнышком?"
     
     m "Да, так что свали на время."
     
     hide Lone_H
     with dissolve
     play sound "audio/Sounds/Sit.mp3"
     queue sound "audio/Sounds/Riverside.mp3"
     "Он внезапно сел рядом..."
     
     "По сравнению с ним, я был просто гном."
     
     "Его улыбка тянулась всё сильнее, и сильнее, когда он смотрел вначале на закат, а затем на меня."
     
     "Это не первая моя встреча с подобным отродьем."
     
     "Жил с ними всегда, с самого детства."
     
     "Детский сад...{w} Школа..."
     
     "Время летит, и ничего не меняется."
     
     "Я всё так же живу с Демонами в своей голове."
     
     hide bg river_evening
     with flashbulb
     show bg deal_1
     with dissolve
     
     "С кем-то удавалось договариваться..."
     hide bg deal_1
     with flashbulb     
     show bg deal_2 
     with dissolve
     
     "Ну, а с кем-то...{w=1}Не всегда."
     
     hide bg deal_2 
     with slow_dissolve
     
     show bg river_evening
     with dissolve
     
     L "Ты что, уснул?"
     
     "Мне было на него плевать.{w=1} Сидеть одному. {w=1.5} На берегу. {w=1}Со своими тараканами в голове.{w=1} Что может быть ещё лучше?"
     
     m "Скажи..."
     m "Сон ли это всё? {w=1}Или же я просто окончательно свихнулся,{w=0.5} раз болтаю с самим собой?"
     L "..."
     "Да.{w=1} Он просто исчез. {w=1.5} Блядь, как всегда."

     pause 1.5
    
     menu:
     
        "Уйти":
            jump leave
        "Посидеть ещё":
            jump stay
     
return

label leave:
    m "..."
    m "Уже поздно. {w} Лучше пойти домой, пока родители не начали ругаться."
    hide bg river_evening
    with slow_dissolve
    play sound "audio/Sounds/open_door.mp3"
return    

label stay:
    m "..."
    m "Ну хоть этот Чертила ушёл. Можно наконец-то побыть одному."
    "Просидев на берегу ещё где-то час, я начал засыпать..."
    hide bg river_evening
    with slow_dissolve
    "В голове всё тот же сон..."
    "Сон,{w} от которого у меня муражки по коже."
    "Сон {w}, который снова возвращал меня в тот день..."
    "..."
    show bg chapter_1
    with slow_dissolve
    "В этом сне...{w}Я видел его..."
    "Какой-то дед звал меня к себе.{w} К вратам..."
    "Я снова послушно подошёл к нему..."
    show bg dream_sketchbook
    with dissolve
    K "Возьми."
    show screen Notebook
    with dissolve
    "И я снова держу в руках то{w}, что помогало мне на протяжении многих лет держаться на плаву."
    "Помогала рассказать то{w}, что открыто я никому бы вслух не произнёс."
    hide bg dream_sketchbook
    with slow_dissolve
    show bg river_evening
    with slow_dissolve
    play sound "audio/Sounds/Sit.mp3"
    queue sound "audio/Sounds/Riverside.mp3"
    "И как всегда, на этом мой сон обрывается."
    "..."
    "Ладно."
    "Пора собираться."
    hide bg river_evening
    with slow_dissolve
    hide screen notebook
    with slow_dissolve
    stop sound fadeout 1
    stop music fadeout 2 
    pause 1
    show screen chapter1
    with slow_dissolve
    pause 10
    hide screen chapter1
    with slow_dissolve
    play sound "audio/Sounds/Bell.mp3" fadeout 2
    pause 3
    show bg room1b
    with slow_dissolve
    pause 1
    hide bg room1
    with slow_dissolve
    pause 2
    show bg room1b
    with fast_dissolve
    pause 0.2
    hide bg room1
    with fast_dissolve
    pause 0.2
    show bg room1
    with fast_dissolve
    m "Блядь!"
    m "7:45!"
    m "Надо пулей лететь на уроки!"
    
    hide window
    pause 1
    play sound "audio/Sounds/bed.mp3"
    hide bg room1 with fast_dissolve
    show bg room2 with fast_dissolve
    pause 1.5
    m "Я же заводил будильник на 7:30!"
    m "..."
    m "Ладно, придётся разогнаться."
    hide bg room2 with dissolve
    show bg kitchen with dissolve
    play music "audio/Music/Morning.mp3"
    pause 1.5
    m "Так-с...{w=1}Начнём с кофе."
    play sound "audio/Sounds/Coffee.mp3"
    "Я как обычно готовлю себе кофе."
    "Дома как всегда идеальная тишина."
    show lie neutral with slow_dissolve
    "Быстро допив кофе, передо мной появляется ещё один кадр."
    LL "Как твой кофе?"
    m "Да как обычно. А ты решил мне с самого утра настроение испортить?"
    LL "Ну, не хочу тебя расстраивать..."
    show lie happy with fast_dissolve
    extend "Но тебе необязательно со мной разговаривать таким тоном."
    m "Кому опять Лапшу вешаешь?"
    hide lie happy with fast_dissolve
    M "Сынок, ты с кем там разговариваешь?"
    "Зараза..."
    
    menu:
        "Что мне сказать?"
        
        "Сказать правду":
            jump Truth
            
        "Соврать":
            jump Lie
            
            
    label Truth:
        m "Да снова со своими тараканами разговариваю."
        M "..."
        M "Ну ладно..."
        jump school
        
    label Lie:
        m "..."
        m "Да всё нормально, рецепт читаю."
        M "..."
        M "Ну ладно..."
        jump school
        
label school:
    "Голос мамы затихает. Кажется, пронесло."
    "Впредь придётся поменьше болтать с самим собой."
    hide screen Notebook with dissolve
    hide bg kitchen with slow_dissolve
    stop music fadeout 2
    show screen School with slow_dissolve
    pause 10
    show screen Notebook with slow_dissolve
    hide screen School with slow_dissolve
    show bg school_1 with slow_dissolve
    play music "audio/Music/class.mp3" fadeout 1.0
    "{i}Зевнул{/i}"
    "Вау!"
    "Это всё красиво, но, по-моему, я уже опаздываю."
    show sofia neutral with dissolve
    "По пути я встретил её."
    "Красавицу, {w=1} в которую я был по уши влюблён."
    show sofia happy with fast_dissolve
    play sound "audio/Sounds/Sofia_L.mp3"
    "Но она лишь засмеялась, заметив меня..."
    hide sofia happy with dissolve
    play sound "audio/Sounds/ran.mp3"
    "и как всегда, убежала..."
    m "Ну и беги..."
    LL "Ну вот. {w=1} Такую цыпочку упустил..."
    m "Заткнись."
    play sound "audio/Sounds/go.mp3"
    hide screen Notebook with slow_dissolve
    hide bg School_1 with slow_dissolve
    pause 6
    show bg library with slow_dissolve
    pause 2
    nvl clear
    A '''
    {size=30}
    Это было обычное апрельское утро четверга.{w=1}
    Наш паренёк был в самом расцвете сил, готовый покорять вершины...{w=2}
    Ну или хотя бы не упасть на той высоте, на которой он находится.{w=3}

    {size=30}Вы - Ученик выпускного класса, который получил горький опыт в прошлом и теперь пожинает его плоды.{w=1} 

    {size=30}В течение этой истории,{w=0.5} вы сможете познакомиться со всеми его Демонами поближе: 
    Кто в чём силён {w=0.5} и кто как мешает нашему пареньку нормально жить.{w=3}

    {size=30}Перед началом{w=1}, мы предлагаем ознакомиться с основами интерфейса (как взаимодействовать с окружением и т.д.).
    {w=2}
    Вы готовы?
    {/size}
        '''
    nvl hide
    menu:
        "Не желаете освоиться с интерфейсом?"
        
        "Да.":
            "Отлично."
            show image "images/Tutorial.png" with fadeout
            "Итак, первое - ваш блокнот."
            "Он расположен в правом верхнем углу."
            "В нём будут записываться истории, которые герой видел в своих снах."
            "Так же, там будут находиться подсказки для некоторых головоломок, которые вам придётся решать во время прохождения игры."
            "Далее - ваш смартфон."
            "Находится он в левом верхнем углу."
            "С помощью него вы сможете перейти на карту локации и использовать некоторые приложения для решения головоломок."
            "В левом нижнем углу расположен оторванный лист."
            "С помощью него, вы сможете без проблем войти в меню."
            hide screen Tutorial with slow_dissolve
            "Ну, наше обучение подошло к концу."
            "Желаем вам приятной игры!"
            jump Library
        
        "Нет, спасибо.":
            "Тогда желаем вам приятной игры!"
            jump Library
                
label Library:
    show screen Phone
    show screen Menu
    show screen Notebook
    pause 2
    menu:
        
        "Посидеть в библиотеке":
            m "Думаю, посижу ещё немного здесь."
            "Библиотекарь:" "Эй, молодой человек! Вы, случаем, не опаздываете на литературу?"
            show anna neutral with dissolve
            "Передо мной стояла милая женщина преклонного возраста."
            "Она всегда выручала меня, когда требовалась помощь."
            "Именно ей я благодарен за многие списанные контрольные, если бы не она..."
            "Кто знает, чем бы это закончилось."
            "Библиотекарь" "Вы меня вообще слышите?"
            m "А? Да, уже иду, извините."
            show anna happy
            "Библиотекарь" "Опять заглядывались?"
            m "Вы чего? Нет, конечно."
            "Да кого я обманываю..."
            hide anna happy with dissolve
            show lie happy with fast_dissolve
            LL "Посмотрите на него! бедный 11-классник заглядывается на библиотекаршу!"
            m "Заткнись."
            hide lie happy with fast_dissolve
            show anna neutral with fast_dissolve
            "Библиотекарь" "Это вы мне?!"
            "Зараза.{w} Забыл, что для того, чтобы заткнуть своих бесов, необязательно говорить вслух..."
            m "Нет нет нет! Я тут...сам с собой опять."
            show anna happy
            "Библиотекарь" "Вы неисправимы, молодой человек! Идите на урок уже, а то опоздаете!"
            m "уже бегу..."
            "Как её зовут? Блин..."
            menu:
                 "Анна":
                     B "Я рада, что вы помните, как меня зовут. Это было очень приятно."
                     m "Да как я мог вас забыть, после всего, что вы для меня сделали."
                     B "Бегите уже!"
                     jump corridor
                     
                 "Раиса":
                     jump fail
                 "Людмила":
                     jump fail
                 "Дарья":
                     jump fail
        "Пойти в класс":
            m "Думаю, стоит прийти пораньше, иначе училка опять орать начнёт."
            LL "Наш послушный мальчик боится получить от учительницы очередную двойку?"
            m "Заткнись."
            jump corridor
        "Погулять по коридорам до звонка":
            m "..."
            m "Пойду прогуляюсь до звонка..."
            jump corridor
label fail:
    show anna neutral
    "Библиотекарь" "Кто, простите?"
    "Блин. Облажался."
    show anna happy
    "Библиотекарь" "Бегите уже!"
    hide library with dissolve
    jump corridor
    
label corridor:
    show bg school_2 with dissolve
    "Блин. До урока осталось меньше 5 минут..."
    play sound "audio/Sounds/bully.mp3"
    AN "Эй!"
    show anton neutral with dissolve
    "Какие люди."
    "Знакомьтесь, {color=#8B0000}Антон{/color}. Главный мудак, вечно издевающийся надо мной."
    show anton talking
    AN "Я тебе говорю, дебил!"
    show anton neutral
    m "Чего тебе?"
    show anton talking
    AN "Сегодня ты разговорчивее обычного, чё с тобой? Смелости набрался?"
    show anton neutral
    m "Слушай, отвали-ка, а? Не до тебя сейчас."
    show anton talking
    AN "Иди давай к своей классухе поплачь, депрессант ходячий..."
    hide anton talking with dissolve
    "..."
    "Дебил..."
    hide bg school_2 with slow_dissolve
    
return    