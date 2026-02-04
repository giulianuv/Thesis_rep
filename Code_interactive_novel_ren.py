
#characters
define g = Character("Giulio", color="#66B3BA")
define b = Character("Billy", color="#da6e0f")
define m = Character("Marie Antoinette", color="#F6C1B4")
define u = Character("Guide", color="#F4D06F")
define q = Character("Queen Victoria", color="#7d1515")
define a = Character("Amelia", color="#7FB685")
define l = Character("Alice", color="#A1C6EA")
define c = Character("Coco Chanel", color="#E4A5A5")



#Load data from 'game/catalogue_renpy.json'
init python:
    import json
    
    def load_corsets(filename):
        with renpy.loader.load(filename) as f:
            return json.load(f)

    #Path
    corsets = load_corsets("catalogue_renpy.json")

    
    def get_corset_by_id(target_id):
        for corset in corsets:
            if corset["ID"] == target_id:
                return corset
        return None




# The game starts here.

label start:

    play music "Sonata13Bb.mp3"
        

    scene bgintro
    with Dissolve(5) 

    scene bg entrance momu2
    with Dissolve(3)

    show giulio happy
    with Dissolve(1)

    $ points = 10
    default bag = []

    g "Hey there!"
    g "I am Giulio, and I am here in Antwerp with my family.{p}We are visiting the Fashion Museum (MoMu) today."
    g "But enough about me, let's hear about you."

        #the player can write the name
    $ name_player = renpy.input("What is your name?", length=16, default="")


    $ name_player = name_player.strip()

    #if the player does not write the name, the name will be mysterious player
    if name_player == "":
        g "No pressure if you'd rather keep your name to yourself... I totally respect your privacy."
        $ name_player = "mysterious player"

    
    g "Nice to meet you, [name_player]!"

    label ask_age:
        $ age_player = renpy.input("How old are you?", length=2, default="").strip()
        if not age_player.isdigit():
            g "This is not a number! Please, enter your age."
            jump ask_age

        $ age_player = int(age_player)
        if age_player < 14:
            hide giulio happy
            show giuliosad
            g "I see you are under 14..."
            g "This interactive experience includes historical and social content that might be more suitable at a later age."
            g "So for now, we won’t continue further."
            g "But I hope you’ll come back someday...{p}When you are ready to explore these themes more deeply."

            hide giuliosad
            show giulio happy
            g "Thank you for your curiosity!"
            return

            
        g "Nice!{p}[age_player] years old...such a good age."
            
            
        g "Throughout this adventure, you'll have to make some important choices.{p}Like this one."
            
        menu:
                g "When was the MoMu inaugurated?"
                "In 1987":
                    jump choice1_incorrect
                "In 2002":
                    jump choice1_correct
    
        label choice1_incorrect:
                hide giulio happy
                show giuliosad
                play sound "wrong.mp3" volume 0.2
                g "Mh...not exactly."
                g "No worries though, there will be other chances."

                jump choice1_done

        label choice1_correct:
                play sound "correct.wav" volume 0.2
                $ points += 10
                g "You answered correctly and just earned 10 points."

                jump choice1_done
    
        label choice1_done:
    
    hide giuliosad
    show giulio happy at left
    with Dissolve (.5)
    
    g "Every decision you make will impact the story and change how things unfold. {p}So be careful and choose wisely."
    $ _rollback = False  #deactivate the "back" function
    
    
    show billyrenpy at right
    with Dissolve(.5)
    
    play sound "billy sound.wav" volume 0.2
    g "This is my dog Billy. He comes with us every time we go on holidays."
    g "But now let's go inside."

    hide giulio happy
    show giuliosad at left
    g "No, Billy...you have to wait here outside. You cannot enter the museum."

    hide billy
    with Dissolve(.5)


    scene bg momu inside2
    with Dissolve(.5)
    show giulio happy
    with Dissolve(1)

    g "Remember: each time you have to make a decision, you could earn points."
    g "You can use them in the shop to purchase items that may be useful throughout the game."
    g "Go ahead and check it out while I'm in line."

hide giulio happy
with Dissolve(.5)

stop music fadeout 1




scene bgshopfinal1
with Dissolve(2)


play music "shop.mp3"

"Welcome!"
"Your current score: [points]."
"You can buy just one item, so think carefully."
"Choosing one item over another might open (or close) different possibilities in the game."

label shop1:
    menu:
        "What would you like to buy?"
        "Envelope (20 points)":
            jump choice2_envelope
        "Scissors (40 points)":
            jump choice2_scissors
        "Golden key (10 points)":
            jump choice2_goldenkey
        

    label choice2_envelope:
        if points >= 20:
            play sound "buy.wav" volume 0.2
            $ points -= 20 
            "You bought an envelope!"
            stop music fadeout 1
            $ bag.append("envelope")
            "Thank you for your purchase. See you soon!"
        else:
            "You don't have enough points!"
            jump shop1
        jump choice2_done

    label choice2_scissors:
        if points >= 40:
            play sound "buy.wav" volume 0.2
            $ points -= 40
            "You bought scissors!"
            stop music fadeout 1
            $ bag.append("scissors")
            "Thank you for your purchase. See you soon!"
        else:
            "You don't have enough points!"
            jump shop1
        jump choice2_done

    label choice2_goldenkey:
        if points >= 10:
            play sound "buy.wav" volume 0.2
            $ points -= 10
            "You bought a golden key!"
            stop music fadeout 1
            $ bag.append("golden key")
            "Thank you for your purchase. See you soon!"
        else:
            "You don't have enough points!"
            jump shop1
        jump choice2_done

label choice2_done:







    

label chapter1:

    #18th century
    

play music "pianosonata12.mp3"
    
scene bg momu tour2
with Dissolve(1.5)

show guide at right
with Dissolve(1)


show giulio happy at left
with Dissolve(1)




u "Welcome to the MoMu!"
u "I hope you enjoy the tour.{p}I am Jessica, your guide."
u "Let's begin. {p}Follow me to the next room."

hide guide
with Dissolve(.5)


g "Interesting object here!{p}I wonder what it feels like to wear a corset..."
g "Well, no one is watching, so I guess trying it on can't do much harm."



hide giulio happy
with Dissolve(.5)

play music "Beethoven_number_5.wav"

scene bg black
with Dissolve(.5)

g "{cps=25}Oh! I can't get it off!{/cps}"
g "{cps=25}What am I going to do now? My family and museum staff are going to lose it...{/cps}"
g "{cps=25}I need to find a restroom and try to take it off...{p}Maybe I can put my T-shirt on it, so the corset is well hidden...{/cps}"
g "{cps=40}Oh my god, it is so tight, I think I might pass out...{/cps}"

stop music fadeout 1




scene bgchapone
with Dissolve (3) 

scene sfondocap1real
with Dissolve(3)

show maria antonietta
with Dissolve(.5)

play music "pitmansonata.mp3"


"Hello there."
"Giulio is in big trouble...{p}He really shouldn't have tried that corset."
"To get back to the present, he will have to travel through three centuries: the 18th, the 19th, and the 20th."
"He is going to face challenges along the way, and throughout this journey..."
"He will learn about the history of the corsets in the MoMu collection."
"Your task is to help and support Giulio, giving him the best suggestions.{p}And obviously, you will learn about corsets as well."
"Throughout the game, you might see red underlined words: these are links.{p}If you want to learn more about a topic, just click on them."
"By the way, I haven't introduced myself yet, but I figured you'd be fine without that..."


m "I am Marie Antoinette, queen of France."
m "I was born in Vienna in 1755 and I married the future Louis XVI in 1770."
m "At court...{p}Well, my lifestyle quickly turned both the aristocracy and the people against me."
m "During the French Revolution, I encouraged the king to reject compromises."

m "But we are not here for me."
m "I will guide you through the story of 18th-century corsets."

m "Before we start..."
menu:
    m "Was the corset merely a fashion item or a reflection of society and historical change?"
    "A fashion item":
        jump choice3_incorrect
    "Reflection of society and historical change":
        jump choice3_correct 

label choice3_incorrect:
    play sound "wrong.mp3" volume 0.2
    m "Unfortunately, that's not quite right. {p}The corset was not just a simple piece of clothing, but an element influenced by various historical, cultural, and economic factors."
    jump choice3_done

label choice3_correct:
    play sound "correct.wav" volume 0.2
    $ points += 10
    m "Well done! You are right."

    jump choice3_done
label choice3_done:
m "Still, the situation is much more complex than this. {p}The corset was a garment that evolved over time, following the natural course of history."

m "Did you know that even the {a=https://www.britannica.com/event/French-Revolution}French Revolution{/a} contributed to the changes in corsets of that period?"

show maria antonietta at right
with Dissolve (.5)

show paintingfr at left
with Dissolve (.5)

m "This is {i}Liberty Leading the People{/i} by Eugène Delacroix.{p}Probably one of the most famous paintings of this period."
m "It was created in 1830, so not exactly in the 18th century..."
m "But Marianne, who represents victorious France, symbolizes the revolutionary ideals of the French Revolution itself."

m "These very ideals would lead to the loosening of corsets."

hide paintingfr 
with Dissolve (.5)


m "Now, I'm curious to hear your opinion on something..."

menu:
    m "Were women victims of corsets?"
    "Yes":
        jump choice4_yes
    "No":
        jump choice4_no
label choice4_yes:
    m "Hmm, interesting answer..."
    jump choice4_done
label choice4_no:
    m "Hmm, I could almost agree with you."
    jump choice4_done
label choice4_done:


m "At this time, women are forced to wear corsets.{p}But they manage to turn this garment, imposed by society, into something that can help them live a better life."

show maria antonietta at right
with Dissolve(.5)

show giuliosad at left
with Dissolve(.5)

g "It's not very clear to me..."
m "Don't worry.{p}I'm sure that as you go on, the social context will make more sense and everything will become clearer."
m "Do you know that women even become involved in the production of corsets?"
m "But now, let me show you what one of these actually looked like."


hide giuliosad
with Dissolve (.5)

show maria antonietta at right
with Dissolve(.5)



show corsetone at Transform(xpos=1, ypos=1, zoom=1.5) #indicates the exact point in which the image should be displayed
with Dissolve(.5)


m "This is a corset from the MoMu collection." #T12/123/o11 
m "This is a whalebone stay (that’s what they used to call them back then)."


$ corset = get_corset_by_id("t12/123/o11")

m "This corset dates back to around [corset['Year 1']] and [corset['Year 2']]. {p}It’s right around this decade that women start wearing corsets without boning (though that’s not the case here)."
m "For formal occasions, French women still wear boned stays."
m "Decorations of this piece are [corset['Decorations']]."
m "The French Revolution ideals will contribute to the decline of these rigid stays."
g "Wait...what do all those terms mean?"
m "Do you mean {a=https://www.wikidata.org/wiki/Q901382}damask{/a}?"
g "Now this is clear.{p}But...whose is this corset?"


m "We don’t know who this particular corset belong to...{p}But here is a game for you. Want to guess?"

hide maria antonietta
with Dissolve(.5)

show giulio happy at right
with Dissolve(.5)

g "The damask pattern is symmetrical..."
g "And the structure is pretty rigid, even though in these years women are starting to wear boneless stays..."

g "Maybe I’ve cracked it! But I need your confirmation before I jump to conclusions. {p}I'd rather not get stuck in the 18th century forever..."


menu:
    g "Who could it have belonged to?"
    "Working woman":
        jump choice5_incorrect
    "Noblewoman":
        jump choice5_correct 

label choice5_incorrect:
    hide giulio happy
    with Dissolve (.5)

    show maria antonietta at right
    with Dissolve (.5)

    play sound "wrong.mp3" volume 0.2
    m "We can’t say sure...{w}But it doesn’t seem like something a humble woman would wear."
    m "The pattern looks too defined (and expensive) for someone from a modest background."
    m "Also, the rigid structure suggests it is probably worn for formal events."


    jump choice5_done

label choice5_correct:
    

    $ points += 10

    hide giulio happy
    with Dissolve (.5)

    show maria antonietta at right
    with Dissolve (.5)
    play sound "correct.wav" volume 0.2
    m "You are right.{p}The care in the pattern and the traditional structure could suggest the corset belongs to a noblewoman."
    m "Most likely, she wears it for a special occasion."

    jump choice5_done
label choice5_done:


    hide corsetone
    with Dissolve (.5)


    show maria antonietta
    with Dissolve (.5)

    m ""
    m "That brings us to the end of this part."
    m "Now you must excuse me for a moment.{p}After all, I am a queen. I've got important royal duties to attend to."

    hide maria antonietta
    with Dissolve(.5)

    show giulio happy
    with Dissolve(.5)

    g "Guess we can move on, wait...{p}What's that floating over there?"
    g "A chest?"
    g "I really want to open it..."
    play sound "lockeddoor.mp3" volume 0.2
    g ""
    g "It is locked.{p}The lock is gold...to open it, I would need a golden key."



    if 'golden key' in bag:

        show giulio happy at left
        with Dissolve(.5)


        show billyrenpy at right
        with Dissolve(.5)

        b "You do have a golden key in your bag!"
        b "Maybe it fits..."
    
        play sound "unlockdoor.mp3" volume 0.2
        g "It works!{p}What in the world...?"
        g "Another corset from the collection."
        g "Let's take a closer look {a=https://www.europeana.eu/en/item/2048208/europeana_fashion_OBJ34266}here{/a}..."


        #data of a specific corset are retrieved using the ID in the json file
        $ corset = get_corset_by_id('t12/1052/o10')


        g "This corset dates back to [corset['Year 1']]."
        g "The materials are [corset['Material']]."
        g "And the neckline is [corset['Neckline']]."
        b "It's a really beautiful corset! But please, don't wear it this time.{p}I like my life in the 21st century, thanks."
        
        
    elif 'envelope' in bag:
        show giulio happy at left
        with Dissolve(.5)


        show billyrenpy at right
        with Dissolve(.5)

        b "Your bag doesn't have any keys...but there's an envelope in there.{p}Maybe you should open it instead?"

        g "Let's open it."
        play sound "openenvelope.mp3" volume 0.2
        g ""
        g "There is a..."


        hide billyrenpy
        with Dissolve(.5)

        
        show giulio happy at left
        with Dissolve(.5)

        show drawingcorset at Transform(xpos=1, ypos=1, zoom=1.7)
        with Dissolve(.5)


        $ corset = get_corset_by_id('t10240')
        g "A [corset['Type']]."
        g "More precisely, it is a [corset['Description'] [:83]]."
        g "There is also a little note..."
        g "[corset['Description'] [136:]]"
        g "It's amazing to be able to study sketches like this."
        g "Even though some corsets didn't survive to the present day, we can still get a glimpse of how they looked back then."

        hide drawingcorset
        with Dissolve (.5)


hide billyrenpy
with Dissolve (.5)

show maria antonietta at right
with Dissolve (.5)

show giulio happy at left
with Dissolve (.5)

if 'envelope' in bag:
    m "Thank goodness the last corset was just a drawing!{p}Considering your irresistible urge to try them on."
    m "But now..."

m "I hope you've recharged your energy, dear [name_player]."
m "If I were you, I'd get ready. Your adventure has only begun..."
m "To move on to the 19th century, you will need to pass through the hole beneath the ancient tree in the garden."
m "It is right behind those flowers."


hide maria antonietta
with Dissolve (.5)

scene bggardenchapone
with Dissolve (.5)

show giulio happy at left
with Dissolve (.5)

show billyrenpy at right
with Dissolve(.5)


g "Let's go now."

stop music fadeout 1



scene bgshopfinal1
with Dissolve(2)


play music "shop.mp3"

"Welcome back. How is your time travel going?"
"Your current score: [points]."
"You can buy just one object, so think carefully."

label shop2:
    menu:
        "What would you like to buy?"
        "Red ball (30 points)":
            jump choice6_redball
        "Tiny key (10 points)":
            jump choice6_tinykey

    label choice6_redball:
        if points >= 30:
            play sound "buy.wav" volume 0.2
            $ points -= 30
            "You bought a red ball!"
            stop music fadeout 1
            $ bag.append("red ball")
            "Thank you for your purchase. See you soon!"
        else:
            "You don't have enough points!"
            jump shop2
    
        jump choice6_done

    label choice6_tinykey:
        if points >= 10:
            play sound "buy.wav" volume 0.2
            $ points -= 10
            "You bought a tiny key!"
            stop music fadeout 1
            $ bag.append("tiny key")
            "Thank you for your purchase. See you soon!"
        else:
            "You don't have enough p..."
            show billyrenpy at right
            with Dissolve (.5)
            play sound "billy sound.wav" volume 0.2
            b "Hey!{p}Look what I found next to the tree."
            b "10 points for you!"
            b "You can use them for the tiny key."
            play sound "buy.wav"
            
            "You have a tiny key now!"
            stop music fadeout 1
            $ bag.append("tiny key")

            hide billyrenpy
            with Dissolve (.5)
        jump choice6_done
    

    label choice6_done:


stop music fadeout 1

jump chapter2




#api call for the study collection
python:
        import requests

        url = 'https://heron.libis.be/momu/api/items?search=mrr53k'
        #search=IDitem
        response = requests.get(url)

        if response.status_code == 200:  
            data = response.json()
            date_corset = data[0]['dcterms:date'][0]['@value']
        else:
            date_corset = "Not available"

    
window show
g "Time span of the corset: [date_corset]"




label chapter2:

    scene bgchaptwointro
    with Dissolve (3)

    scene bgchap2real
    with Dissolve (3)


    play music "goldberg.mp3"
    

    show queen vic
    with Dissolve (1)

    "What are you doing in my garden?"

    show queen vic at right
    with Dissolve (.5)

    show giuliosad at left
    with Dissolve (.5)

    g "Sorry! I am Giulio, this is my dog Billy and this is [name_player]."

    
    g "We're stuck in this time travel mess because of me..."
    "And how did you get end up here?"
    g "Well, it started with a corset from the Fashion Museum..."
    "Very silly of you."
    "But I'll help you.{p}Let me tell you about what happened in this century and how the corset evolves."

    hide giuliosad
    show giulio happy at left


    "My dear Giulio, my dear [name_player], welcome to the 19th century."


    hide giulio happy
    with Dissolve (.5)

    show industrialrv at Transform(xpos=1, ypos=1, zoom=1) 
    with Dissolve(.5)
   

    "A century full of significant events like the {a=https://www.britannica.com/event/Industrial-Revolution}Industrial Revolution{/a} and the {a=https://www.britannica.com/event/Revolutions-of-1848}Revolutions of 1848{/a}."
    "This is {i}Pont Boieldieu in Rouen, Rainy Weather{/i} by Pisarro."
    "It is an 1896 painting depicting the busy industrial section of the town of Rouen."

    "I think this painting gives you an idea of what the Industrial Era is like..."
    "But now, let me introduce myself..."

    hide industrialrv
    with Dissolve (.5)
    q "I am Queen Victoria.{p}I was born in 1819 and in 1837, I ascend to the throne of England."
    q "My reign begins during a time of major change: the recent electoral reform has opened Parliament to the industrial classes..."
    q "And strong republican sentiments have spread due to the {a=https://www.historic-uk.com/HistoryUK/HistoryofBritain/George-IV/}scandals{/a} of King George IV's reign."
    q "With the support of Lord Melbourne, I quickly learn the duties of a queen."
    q "In short, I have quite a lot to manage."

    q "After the French Revolution, the ideas of fraternity, equality, and liberty started to spread across Europe, changing politics and society."

    show giuliosad at left
    with Dissolve(.5)

    g "That sounds great and all, but... how does this tie into the history of corsets?"

    q "Don’t rush me! You might think these things are unrelated, but the corset was more than just clothing."

    hide giuliosad
    show giulio happy at left

    q "In the previous century, boned stays were starting to fall out of fashion."
    q "But surprisingly, in 1814, they made a comeback."
    q "That is likely because of the Restoration’s anti-revolutionary ideas. Wearing a dress without a corset is actually seen as...{p}well, revolutionary."


    hide giulio happy
    show giuliosad at left

    g "But if it is so uncomfortable and cause so much pain...{p}Then why do women keep wearing it?"

    hide giuliosad
    with Dissolve (.5)

    show queen vic 
    with Dissolve (.5)

    q "The corset is not just about comfort. It is about conforming to the beauty and social standards of the time."
    q "Even though it is painful, women wear it because it is the thing to do."
    

    
    show giulio happy at left
    with Dissolve (.5)

    label question:
    menu:
        q "Do you have any questions for me?"
        "Role of mothers":
            jump choice7_mothers
        "Corset in the Victorian Age":
            jump choice7_victorian
        

    label choice7_mothers:
        q "Wearing a corset is part of fitting into the beauty standards of the time. And, of course, it improves a woman's chances of finding a husband."
        q "Corsets are not just about style. They are about preparing girls to fit into society’s expectations."
        q "Mothers even encourage tight lacing, thinking it might help their daughters marry well and secure a wealthy husband."
        menu:
            q "Do you have more questions?"
            "Corset in the Victorian Age":
                jump choice7_victorian
            "Move on":
                jump choice7_done



        jump choice7_done
    
    label choice7_victorian:
        q "During my reign (1837-1901), it is considered proper for girls to wear a corset to dress ‘respectably'."
        q "The corset is also a way for women to express their sexuality...{p}within the social norms, of course."
        menu:
            q "Do you have more questions?"
            "Role of mothers":
                jump choice7_mothers
            "Move on":
                jump choice7_done
        jump choice7_done
    
    label choice7_done:


    q "During this period, another historical event significantly contributes to the history and use of the corset:{p}the Industrial Revolution."

    menu:
        q "How do you think it might have changed?"
        "More women have access to corsets":
            jump choice8_morewomen
        "Fewer women have access to corsets and they fall out of use":
            jump choice8_fewerwomen
        
    label choice8_morewomen:
        play sound "correct.wav" volume 0.2
        $ points += 10
        q "Right."
        
        jump choice8_done
    
    label choice8_fewerwomen:
        hide giulio happy
        show giuliosad at left
        play sound "wrong.mp3" volume 0.2
        q "Actually, this is not really right..."
        jump choice8_done
    
    label choice8_done:
    
    q "Thanks to the Industrial Revolution, many more women have access to corset.{p}For this reason, the corset now thrives."
    q "It becomes a mass phenomenon, no longer reserved only for the nobility.{p}Now the beauty ideal is applied to all the women."
    q "In addition, steam-moulded corsets make it possible to produce corsets without needing custom measurements...{p}Further promoting mass production."
    q "As a result, even the poorest women can afford a corset."

    show queen vic at right
    with Dissolve (.5)

    hide giuliosad

    show giulio happy at left
    with Dissolve (.5)

    g "Got it...but are corsets still very uncomfortable now?"
    q "Let's say yes, although around 1820, the elastic corsets are introduced."
    q "It is precisely during this period that more importance begins to be placed on comfort."

    q "Oh..."
    q "A couple of guests have just arrived."
    q "If you wish, you can join us and chat with one of them."

    menu:
        q "Who would you like to talk to?"
        "Pregnant woman":
            jump choice9_pregnant
        "Little girl":
            jump choice9_girl
        
    label choice9_pregnant:
        hide queen vic
        with Dissolve (.5)

        show pregnantlady at right
        with Dissolve (.5)

        l "Nice to meet you, Giulio and [name_player].{p}I am Alice and I am expecting a girl."
        g "Congrats!{p}But why are you wearing a corset even if you are pregnant?"
        l "The doctors are neither for nor against the corset, and I have decided to wear it."
        l "Nevertheless, they are starting to warn women that tight corsets are dangerous for pregnancies."
        l "Don't tell to anybody but...{p}It is believed that some women use corsets to hide pregnancies or even to induce abortions."
        l "Anyway...would you like to see one of my corsets?"
        g "Yes, of course."

        hide giulio happy
        with Dissolve (.5)


        show corsettwo at Transform(xpos=1, ypos=1, zoom=.8) 
        with Dissolve(.5) #st1002

        python:
            import requests

            url = 'https://heron.libis.be/momu/api/items?search=ark:34546/mf1vp9'
            response = requests.get(url)

            if response.status_code == 200:  
                data = response.json()
                location_corset = data[0]['cidoc:P55_has_current_location'][0]['display_title']
            else:
                location_corset = "unknown location"

    
        window show
        l "..."
        l "This corset belongs to the MoMu collection."
        l "Precisely, it is located in [location_corset]."

        $ corset = get_corset_by_id("st1002")
        

        l "It dates back to around [corset['Year 1']]."
        l "The material are [corset['Material']]."
        l "Talking about decorations...the decoration of this piece is [corset['Decorations']]."

        hide corsettwo
        with Dissolve (.5)

        show giulio happy at left
        with Dissolve (.5)

        g "Will you make your daughter wear the corset?"
        l "Of course. I want her to have a nice life with a good husband."
        l "It was nice to meet you, Giulio and [name_player].{p}Now I have to go."


        hide pregnantlady
        with Dissolve (.5)


        menu:
            q "What would you like to do?"
            "Talk to the little girl":
                jump choice9_girl
            "Move on":
                jump choice9_done


        
        jump choice9_done
    
    label choice9_girl:
        hide queen vic
        with Dissolve (.5)

        show kids at right
        with Dissolve (.5)
        a "Hello! My name is Amelia."
        a "Do you know that we girls also wear corsets?"
        hide giulio happy
        with Dissolve (.5)


        show catkids at Transform(xpos=1, ypos=1, zoom=1.5) 
        with Dissolve(.5)
        a "Now, little girls wear corsets made for children, not miniature versions of adult ones like in the 18th century."
        a "This is a catalogue from 1890. As shown, now there are different types of corset for every age."

        hide catkids
        with Dissolve (.5)

        

        a "Also my doll wears a corset!"
        show giulio happy at left
        with Dissolve(.5)
        g "Really? Can I see it?"
        a "Only if you have the key to open my doll's wardrobe."
        a "For a tiny wardrobe...{p}You need a tiny key."
        if 'tiny key' in bag:
            hide kids
            with Dissolve (.5)


            show billyrenpy at right
            with Dissolve(.5)

            b "You do have a tiny key in your bag!"
            g "Amazing."
            play sound "unlockdoor.mp3" volume 0.2

            hide billyrenpy
            with Dissolve (.5)



            show corsetthree at Transform(xpos=.4, ypos=.2, zoom=1.1) 
            with Dissolve(1)


            python:
                import requests

                url = 'https://heron.libis.be/momu/api/items?search=ark:34546/mz617w'
                response = requests.get(url)

                if response.status_code == 200:  
                    data = response.json()
                    date_corset = data[0]['dcterms:date'][0]['@value']
                else:
                    date_corset = "unknown date"

    
            window show
            a "..."
            a "Here is the corset. It also belongs to the MoMu collection."
            a "It dates back to around [date_corset]."

            $ corset = get_corset_by_id("st2025") 


            a "The materials are [corset['Material']]."
            a "The decorations of this corset are [corset['Decorations']]."
            
            hide corsetthree
            with Dissolve (.5)

            show kids at right
            with Dissolve (.5)
            a "Isn't it beautiful?"
            a "Now it's time to play with my doll. See you soon!"

            hide kids
            with Dissolve (.5)

        
        if 'red ball' in bag:

            hide kids
            with Dissolve(.5)



            show billyrenpy at right
            with Dissolve(.5)

            b "You don't have any tiny key, but only a ball..."
            a "A ball?!{p}If you let me play with the ball, I'll show you my doll's corset."
            g "Deal then. Here's the ball."
            a "Thank you. This is the tiny key."
            play sound "unlockdoor.mp3" volume 0.2
            g "..."

            hide billyrenpy
            

            show corsetthree at Transform(xpos=.4, ypos=.2, zoom=1.1) 
            with Dissolve(.5)

            $ corset = get_corset_by_id("st2025")

            a "Here is the corset. It also belongs to the MoMu collection."
            a "It dates back to around [corset['Year 1']]."
            a "The materials are [corset['Material']]."
            a "The decoration of this piece is [corset['Decorations']]."
            
            hide corsetthree
            with Dissolve (.5)

            show kids at right
            with Dissolve (.5)
            a "Now it's time to play with the ball. See you soon!"

            hide kids
            with Dissolve (.5)

        menu:
            q "What would you like to do?"
            "Talk to the pregnant woman":
                jump choice9_pregnant
            "Move on":
                jump choice9_done

        jump choice9_done
    
    label choice9_done:

    show queen vic at right
    with Dissolve (.5)
    show giulio happy at left
    with Dissolve (.5)


    q "I hope you enjoyed your time with my guests."
    q "Your journey through this century is almost over...get ready for the 20th century."
    
    q "You will need to pass through the hole behind that tree."
    q "Good luck."

    hide queen vic
    with Dissolve (.5)

    show billyrenpy at right
    with Dissolve(.5)

    g "Let's go."

    stop music fadeout 1

    

    
scene bgshopfinal1
with Dissolve(2)


play music "shop.mp3"

"Hello again."

if points < 10:
    "Your wallet is a little bit empty...isn't it?"
"Your current score: [points]."
"You can buy just one object, so think carefully."

label shop3:
    menu:
        "What would you like to buy?"
        "Doll dress (20 points)":
            jump choice10_dolldress
        "Dog treat (10 points)":
            jump choice10_dogtreat
        "Nothing":
            stop music fadeout 1
            jump chapter3


    label choice10_dolldress:
        if points >= 20:
            play sound "buy.wav" volume 0.2
            $ points -= 20
            "You bought doll dress!"
            stop music fadeout 1
            $ bag.append("doll dress")
            "Thank you for your purchase. See you soon!"
        else:
            "You don't have enough points!"
            jump shop3
        
        jump choice10_done

    label choice10_dogtreat:
        if points >= 10:
            play sound "buy.wav" volume 0.2
            $ points -= 10
            "You bought a dog treat!"
            stop music fadeout 1
            $ bag.append("dog treat")
            "Thank you for your purchase. See you soon!"
        else:
            "You don't have enough poi..."
            show kids
            with Dissolve (.5)

            a "Hey."
            a "Looks like you are in troubles."
            a "It's not a lot...but I can give you 10 points."
            a "Use them in the shop and come back to your century."
            
            
            play sound "buy.wav" volume 0.2
            
            "You have a dog treat now!"
            stop music fadeout 1
            $ bag.append("dog treat")


            a "Good luck, my friends."

            hide kids
            with Dissolve (.5)
        jump choice10_done
    

    label choice10_done:


stop music fadeout 1



label chapter3:

    play music "musiccap3.mp3" 

    scene bgchapthree
    with Dissolve (3)
    

    scene bgparis
    with Dissolve (3)


    show giulio happy 
    with Dissolve (.5)

    g "And where are we now...?"

    show giulio happy at left
    with Dissolve (.5)

    show cocochanel at right 
    with Dissolve(.5)

    "Hello Giulio, hello [name_player]. I've been waiting for you."
    "Your journey through time is coming to an end. It won't be easy to make it through this century though..."
    "The 20th century is filled with historical events that changed humanity forever: {a=https://ushistoryscene.com/article/second-industrial-revolution/}the Second Industrial Revolution{/a}, {a=https://www.britannica.com/topic/positivism}Positivism{/a}..."
    "But most importantly, the World Wars and the Cold War."
    c "I am {a=https://www.britannica.com/biography/Coco-Chanel}Coco Chanel{/a}."
    c "I was born in France in 1883. I live my whole life fully in the 20th century."
    c "I am a French fashion designer."
    c "My designs encourage women to give up uncomfortable clothing...{p}Like corsets."
    c "In short... I revolutionize the fashion industry."
    c "Wealthy women start showing interest in my creations, as they are looking for relief from corsets."
    g "What happens during World War II?"
 
    c "In 1939, I have to close my couture house."

    c "Enough about me.{p}Now, let's move on to corsets."
    

    c "In the early years of the 20th century, the straight front corset become very popular, as it flattens the stomach."
    c "In fact, between 1907 and 1910, the beauty standard is represented by the slender young girl:{p}a young woman with slim hips."



    hide giulio happy
    with Dissolve (.5)

    show imagefivetd at Transform(xpos=1, ypos=1, zoom=1.5) #chatgpt
    with Dissolve (.5)
    

    c "This is an article from {i}The Delineator{/i}."
    c "It is a magazine for women of the late 19th and 20th centuries."
    c "The magazine also includes tips on how to achieve the trendy slender figure."

    hide imagefivetd
    with Dissolve (.5)

    show giulio happy at left
    with Dissolve (.5)
    g "What about corsets of this age? Can I see one?"
    c "Of course."

    hide giulio happy
    with Dissolve (.5)

    show corsetfour at Transform(xpos=1, ypos=1, zoom=1.8) 
    with Dissolve (.5)
    #t94/479 ccby

    $ corset = get_corset_by_id("t94/479")

    
    c "This is a corset belonging to this century from the MoMu collection."
    c "It dates back to around [corset['Year 1']]."
    c "The main material is [corset['Material']]."
    c "There are several decorations here...[corset['Decorations']]."
            

    hide corsetfour
    with Dissolve (.5)

    show giulio happy at left
    with Dissolve (.5)

    c "Until 1919, corsets still have some boning, but there is a predominance of rubber-coated steel rather than whalebone."

    hide giulio happy
    show giuliosad at left
    g "But...how does it change during the World War I?"


    c "The {a=https://www.britannica.com/event/World-War-I}First World War{/a} changes everything..."
    c "Frieda Dauphin-Verhees will tell you how the corset changes right in this period."
    stop music fadeout 1
    
    c "As you click, the video will start. {p}It lasts about a minute. Once you are ready to move on, just click again."
    

    $ renpy.movie_cutscene("talkaboutcorsn.webm")
    #source:https://vimeo.com/254847187
    play music "musiccap3.mp3"
    
    hide giuliosad
    show giulio happy at left
    with Dissolve (.5)

    c "She held a {a=https://vimeo.com/254847187}talk{/a} during an event for the Study Collection."
    g "She talks about you, too."
    c "Glad that my work is still being talked about."

    c "I was wondering..."
    


    menu:
        c "Do you think that metal in corsets is used for military supplies during the war?"
        "Yes":
            jump choice11_correct
        "No":
            jump choice11_incorrect
        

    label choice11_correct:
        play sound "correct.wav" volume 0.2
        $ points += 10
        c "Correct."
        jump choice11_done
    
    label choice11_incorrect:
        hide giulio happy
        show giuliosad at left
        play sound "wrong.mp3" volume 0.2
        c "Mh...not really right."
        jump choice11_done

    label choice11_done:
    

    c "Around 1917, it is asked to women to stop buying corsets: in this way, the metal used for the corset frames can be used for ammunition."
    c "This contributes to the birth of the modern bra."

    c "Although the metal used in corsets is redirected for wartime purposes, this does not mark the end of the corset."
    

    hide giulio happy
    with Dissolve (.5)

    hide giuliosad
    with Dissolve (.5)

    show imagetwotd at Transform(xpos=1, ypos=1, zoom=1.5) 
    with Dissolve (.5)

    c "Since the 1920s, the traditional boned corset has gradually disappeared. Alternatives to the corset, such as brassieres, are born."

    hide imagetwotd
    with Dissolve (.5)

    show giulio happy at left
    with Dissolve (.5)
    
    g "And what about the Second World War? Is corset metal still used for military purposes?"
    c "Exactly, during {a=https://www.britannica.com/event/World-War-II}World War II{/a} the situation repeates itself."
    g "Oh! Something has fallen from your purse."
    play sound "openenvelope.mp3" volume 0.2
    g "It looks like...{p}a magazine."
    c "Ah...{p}This is a 1950 {a=https://underpinningsmuseum.com/museum-collections/aldrex-corsets-brassieres-catalogue/}catalogue{/a} of corsets and brassieres. You can browse through it if you like."
    c ""
    
    c "Young friend, dear [name_player]...your journey is almost over."
    c "To return to the 21st century, you just need to step into that shop right around this corner."
    c "Good luck."

    play sound "opendoorshop.wav" volume 0.2
    scene finalshop
    with Dissolve (3)

    show sartamarcelle at right
    with Dissolve (1)

    "Hello."

    show giulio happy at left
    with Dissolve (1)

    g "Hello, I am here becaus..."
    "I know why you are here."

    hide giulio happy
    show giuliosad at left
    g "Who are you?"
    "Marcelle."
    g "Okay...{p}Where is the door to go back to my century?"
    "Right there.{p}But I cannot let you go before a little game..."
    g "Another one..."
    "You could have left that corset alone."
    "I do not care for people who mess around with museum pieces, treating them like toys.{p}But I'll help you..."

    hide sartamarcelle
    show sartahappy at right
    "Only because your dog is absolutely adorable."

    play sound "billy sound.wav" volume 0.2
    b "Indeed."

    hide sartahappy
    show sartamarcelle at right

    "Let's start. Hope you are ready."
    g "Sure..."
    "..."


    #questions for the end of the game
    
    #question 1
    
    menu:
        "Did men wear corsets too?"
        "Yes":
            jump choice12_correct
        "No":
            jump choice12_incorrect
        

    label choice12_correct:
        hide giuliosad
        show giulio happy at left
        play sound "correct.wav" volume 0.2
        $ points += 10
        "Correct."
        jump choice12_done
    
    label choice12_incorrect:
        play sound "wrong.mp3" volume 0.2
        "Mh...not really right."
        jump choice12_done

    label choice12_done:

    #question 2

    menu:
        "Which material was commonly used for corset boning before steel?"
        "Plastic":
            jump choice13_incorrect
        "Whalebone":
            jump choice13_correct
    
    label choice13_incorrect:
        hide giulio happy
        show giuliosad at left
        play sound "wrong.mp3" volume 0.2
        "Mh...not really right."
        jump choice13_done

    label choice13_correct:
        hide giuliosad
        show giulio happy at left
        hide sartamarcelle
        show sartahappy at right
        play sound "correct.wav" volume 0.2
        $ points += 10
        "Correct."
        jump choice13_done
    label choice13_done:
    
    #question 3

    
    if points > 20:
        "What term was used to name the corset in the 18th century?"
        "Mh...{p}Okay, I will help you a little bit."
        "It rhymes with 'day' and start with 'S'."

    $ answerthree = renpy.input("What term was used to name the corset in the 18th century?", length=4, default="").strip().lower()


    if answerthree == "stay":
        hide giuliosad
        show giulio happy at left

        hide sartamarcelle
        show sartahappy at right

        play sound "correct.wav" volume 0.2
        $ points += 10
        "Correct."
    else:
        hide giulio happy
        show giuliosad at left
        hide sartahappy
        show sartamarcelle at right
        "This is not correct."

    
    "Let's see if you have a good eye...take a close look at this corset."

    hide giulio happy
    with Dissolve (.5)

    hide giuliosad
    with Dissolve (.5)

    show corsetfinal at Transform(xpos=1, ypos=1, zoom=1.7)
    with Dissolve (.5)
    #af195 ccby

    "Take your time."

    menu:
        "From which century might this corset be?"
        "18th":
            jump choice14_incorrect
        "20th":
            jump choice14_correct
    
    label choice14_incorrect:
        hide corsetfinal 
        with Dissolve (.5)
        hide giulio happy
        show giuliosad at left
        with Dissolve (.5)

        hide sartahappy
        show sartamarcelle at right
        play sound "wrong.mp3" volume 0.2
        "Mh...not really right."
        jump choice14_done

    label choice14_correct:
        hide sartamarcelle
        show sartahappy at right
        play sound "correct.wav" volume 0.2
        $ points += 10
        "Correct."
        jump choice14_done
    label choice14_done:

    stop music fadeout 1

    if points <= 20:
        "You are not as skilled as I am...but I'll let you go."
        "The door you are looking for is behind the fitting room."
    
    if points > 20:
        hide sartamarcelle
        show sartahappy at right
        "You are doing well...I am surprised.{p}Continue your journey, and have a safe trip home."
        "The door you are looking for is behind the fitting room."
    
   

    play music "musicfinaldoor.mp3"



    scene bgporta1
    with Dissolve (1)

    show giuliosad at left
    with Dissolve (.5)

    show billyrenpy at right
    with Dissolve (.5)

    b "Uh...{p}There is a riddle to solve in order to open the door."
    "{i}You do it each day, no need to recall.{p}
    But try it in corsets: you’ll struggle, that’s all."

    if 'doll dress' in bag:

        hide billyrenpy
        with Dissolve (.5)
        show kids at right
        with Dissolve (.5)

        a "Seems like you need help."
        a "But this time my help has a price..."
        g "What price?"
        g "I would give you anything to go back to my century..."
        a "...."
        a "What about that nice dress for my doll?"
        g "Okay, it's yours."
        a "Thank you."
        a "Here there is the hint."
        a "{i}Anyone can hold me, even without their hands, yet no one can do it for long."
        hide kids
        with Dissolve(.5)
        show billyrenpy at right
        with Dissolve(.5)
       
    
    if 'dog treat' in bag:
        show billyrenpy at right
        with Dissolve (.5)
        b "..."
        b "Troubles?"
        b "Maybe I can give you a little hint..."
        b "..."
        g "..."
        b "..."
        g "...{p}Why are you looking at me like that?"
        b "Do you have a little treat for me?"
        g "I do. Here it is, but now help me. Please."
        b "Thank you."
        b "{i}You take it in to stay alive, but let it go with every sigh."

    
    $ answerfour = renpy.input("What is the secret word?", length=6, default="").strip().lower()
    if answerfour == "breath":
        hide giuliosad
        show giulio happy at left
        
        stop music fadeout 1
        play sound "correct.wav" volume 0.2
        b "Correct!!!"
        b "Now we can finally come back to the 21st century..."
        jump endings

       
    
    else:
        hide giulio happy
        show giuliosad at left
        b "This is not correct..."
        g "Now there is no way to open this door..."
        b "We need to find another way to get back home."

        scene finalshop
        with Dissolve (1)

        show sartamarcelle at right
        with Dissolve (.5)

        show giuliosad at left 
        with Dissolve (.5)

        "Couldn't find the right word, huh?"
        g "No...can you help us?"
        "No. I can't help you anymore.{p}You'll have to manage on your own now."

        scene bgparis
        with Dissolve (1)

        show giuliosad at left
        with Dissolve(.5)

        show billyrenpy at right
        with Dissolve(.5)

        
        g "I don't know where to go..."
        g "I don't want to stay here forever."
        b "Wait..."
        b "I found another way back!"

        scene bg black
        with Dissolve(1.5)

        show giuliosad at left
        with Dissolve(.5)

        show billyrenpy at right
        with Dissolve(.5)

        
        g "We are going back?"
        b "Let's hurry."
        g "We are going to cross...{p}the catacombs of Paris?"
        
        b "You'll get a bit dirty, but at least we will be home. Let's go!"

        hide giuliosad
        with Dissolve(1)
        hide billyrenpy
        with Dissolve (1)

        g "Cannot see anything..."


        label maze:
            menu:
                g "Which way should I go?"
                "Right":
                    jump choice15_right
                "Left":
                    jump choice15_left
        
            label choice15_right:
                
                menu:
                    g "I took the right path. Now where?"
                    "Right":
                        jump choice16_right
                    "Left":
                        jump choice16_left
                        

                label choice16_right:
                    g "This just circles back... I'm at the beginning again."
                    jump maze

                label choice16_left:
                    stop music fadeout 1
                    g "Wait... I think this is the exit!"
                    jump endings

                jump choice15_done

            label choice15_left:
                menu:
                    g "I took the left path. Now where?"
                    "Right":
                        stop music fadeout 1
                        g "I think this might be the way out!"
                        jump endings
                    "Left":
                        g "Dead end... I'm back where I started."
                        jump maze
                jump choice15_done



            
         
     
    
    label endings:
        if points > 20:
            jump happyending
        else:
            jump sadending


label happyending:
    play music "Sonata13Bb.mp3"
    play sound "opendoorshop.wav" volume 0.2
    scene bg momu tour2
    with Dissolve(1.5)

    show guide at right
    with Dissolve(1)

    show giulio happy at left
    with Dissolve(1)

    u "And that was the last piece of our permanent collection."
    g "How wonderful! Back home!"
    g "And most important...{p}I am not wearing the corset anymore!"
    u "Excuse me?{p}Are you the boy who got lost?"
    u "I am glad I found you again...{p}But it is a shame you missed the guided tour."
    u "But if you’d like to come back to the MoMu, you will always be welcome."
    u "In case you need some information for {a=https://www.momu.be/en/visitor-information}visitors{a}..."
    u "See you soon!"

    
    jump feedback



label sadending:
    play music "musicfinaldoor.mp3"
    play sound "opendoorshop.wav" volume 0.2
    scene bg momu tour2
    with Dissolve(1.5)

    show giulio happy at left
    with Dissolve (1)
    g "Finally, the Fashion Museum!"
    g "I am back!"
    
    hide giulio happy
    show giuliosad at left

    g "Oh no...{p}I am still wearing the corset."
    g "There is no way to take it off..."


    show guidecorset at right
    with Dissolve(1)

    u "And that was the last piece of our permanent collection."


    u "Hello boy...?{p}Are you the one who got lost?"
    g "I am..."
    g "I ran into a little...problem."
    u "I am glad I found you again...{p}But it is a shame you missed the guided tour."
    u "I really have to go home now, my shift is over and this corset...{p}Well, it's killing me."
    u "But if you’d like to come back to the MoMu, you will always be welcome."
    u "In case you need some information for {a=https://www.momu.be/en/visitor-information}visitors{a}..."
    u "Well... good luck out there."
    

    jump feedback


label feedback:

    scene bg entrance momu2
    with Dissolve(3)

    show giulio happy at left
    with Dissolve (.5)

    show billyrenpy at right
    with Dissolve(.5)
    g "I hope you enjoyed the novel."  
    g "We’ve been on quite an adventure..."  
    g "But now I need your help."  
    g "Why not click {a=https://docs.google.com/forms/d/e/1FAIpQLSfGaRemL5NLzhTfbfhStdkeQh4qSlQ6ZtY4AVoo1czdBsscXA/viewform?usp=dialog}here{/a} and fill out this short form?"  
    g "It’s not for me, it’s for Giulia."  
    g "An honest feedback would really help her with her thesis."
    g "Thanks for playing.{p}Goodbye!"
    play sound "billy sound.wav" volume 0.2
    b "..."
    

    hide giulio happy
    with Dissolve (.5)

    hide billyrenpy
    with Dissolve (.5)



label credits:
    "Credits:{p}Written and designed by Giulia Nuvoli."
    "Historical sources:{p}'The Corset: A Cultural History' Valerie Steele.{p}'Bra History: How a War Shortage Reshaped Modern Shapewear' Melissa Pandika."
    "Information about Marie Antoinette and Queen Victoria: Treccani.{p}'The Delineator, Vol. 104 (April 1924)' Internet Archive."
    "Information about Coco Chanel: Britannica."
    "The shop background and all characters: AI-generated.{p}Background photos: original photography by Giulia."

    "Introduction:{p}Mozart Piano Sonata No. 13 in B-flat major, K. 333.{p}Mozart Piano Sonata No. 12, K. 332."
    "Beethoven Symphony No. 5.{p}Shop music: Clementi Six Sonatinas, Op. 36."

    "Chapter 1:{p}Beethoven Moonlight Sonata, Op. 27 No. 2 (III. Allegretto)."
    "Background: Castle of Ghent.{p}Garden: Botanical Garden of Leuven."
    "Painting and corset: Wikimedia Commons.{p}Drawing: Europeana."
    "Corset: t12/123/o11.{p}Attribution: Corset, 1770-1790. Jacoba de Jonge Collection in MoMu / Photo by Hugo Maertens, Bruges."

    "Chapter 2:{p}Bach Goldberg Variations, BWV 988."
    "Background: Botanical Garden of Leuven.{p}Painting: Wikimedia Commons."
    "Corset (pregnant woman): st1002. Europeana.{p}Attribution: Corset, 2010. MoMu / Photo by Stany Dederen."
    "Corset (young girl): st2025. MoMu Study Collection.{p}Attribution: Collection MoMu Antwerp / Photo Stany Dederen."
    "Historical Catalog: Fall and Winter 1890/91, H. O’Neill & Co. Internet Archive."

    stop music fadeout 1

    "Chapter 3:{p}Chopin Nocturnes, Op. 9.{p}Mozart String Quartet No. 19 in C major 'Dissonant', K. 465."
    "Visuals:{p}Paris (photo), shops (AI-generated):"
    "Corset one: t94/479. Europeana.{p}Attribution: Corset, 1900/1910. MoMu / Photo by Daniel Rys."
    "Corset two: af195.{p}Attribution: MoMu / Photo by Daniel Rys."
 
    
    #/https://musopen.org/music/20-piano-sonata-no-13-k-333/#google_vignette pd
    
    #https://musopen.org/music/29243-6-sonatinas-op-36/#google_vignette pd
    
    #https://musopen.org/music/19-piano-sonata-no-12-k-332/ pd

    #https://archive.org/details/SymphonyNo.5 pd

    #"Chapter 1:"
   
    #https://musopen.org/music/2547-piano-sonata-no-14-in-c-sharp-minor-moonlight-sonata-op-27-no-2/ pd
    #source=https://commons.wikimedia.org/wiki/File:Eug%C3%A8ne_Delacroix_-_La_libert%C3%A9_guidant_le_peuple.jpg pd
    #source: https://www.treccani.it/enciclopedia/maria-antonietta-d-asburgo-lorena_(Dizionario-di-Storia)/
    #https://commons.wikimedia.org/wiki/File:Corset,_1770-1790._MoMu_-_Fashion_Museum_Province_of_Antwerp,_www.momu.be._Photo_by_Hugo_Maertens,_Bruges..jpg some copyright
    #https://www.europeana.eu/it/item/2048208/europeana_fashion_OBJ45552 pd
 

    #"Chapter 2:"
    
    #https://musopen.org/music/4107-goldberg-variations-bwv-988/ pd
    #source: https://commons.wikimedia.org/wiki/File:Pissarro_-_Pont_Boieldieu_in_Rouen,_Rainy_Weather.jpg pd
    ##source: https://www.treccani.it/enciclopedia/vittoria-regina-del-regno-unito-di-gran-bretagna-e-irlanda-imperatrice-delle-indie/
    #https://archive.org/details/fallwinter18909100hone

    #"Chapter 3:"
    #source:https://musopen.org/music/108-nocturnes-op-9/ pd
    #https://archive.org/details/delineator104olou/page/n473/mode/2up
    #source: https://musopen.org/music/3002-string-quartet-no-19-in-c-major-dissonant-k-465/ pd
    #sound effects are public domain


return

