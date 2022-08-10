import deckofcards
from tkinter import *
from PIL import Image, ImageTk
import random
import turtle

root=Tk()
root.title ("Tarot Reading")
root.geometry ("2000x2000")

cardindex=0

class Card():
    def __init__(self, cardname, filename):
        
        self.cardname=cardname
        self.filename=filename
        self.reverse=False

    def __str__(self):
        return self.cardname
    def display_card (self):
        card_image=Image.open (self.filename)
        card_image=card_image.resize ((100, 175))
        if self.reverse==True:
            card_image=card_image.rotate(180)
            
        card_image.show()
    def reverse_card (self):
        if self.reverse==True:
            self.reverse=False
        else:
            self.reverse=True




    

    
    
def create_deck():
    
    cardlist=[]
    for x in deckofcards.tarot:
        filename= (deckofcards.tarot [x])
        card=Card(x, filename)
        
        cardlist.append (card)
    
    
    
    
    return cardlist
        
def draw_card():
    global cardindex, cardlist
    
    card=cardlist[cardindex]
    cardindex+=1
    return card


    
def reshuffle_cards (event):
    global cardindex, cardlist, card_space
    cardindex=0
    card_space=Frame(root, bg="pink", width=2000, height=1850)

    card_space.place (x=110, y=0)
    card_space.grid_propagate=False
    for c in cardlist:
        reverse=random.randrange (0,5)
        if reverse==4:
            c.reverse_card()
    random.shuffle (cardlist)
    return cardlist
    

def make_label(event):
    
    global cardindex, card_space
    ourcard=draw_card()
    card_image=ourcard.filename
    display_card=Image.open(card_image)
    display_card=display_card.resize ((100, 175))
    if ourcard.reverse==True:
        display_card=display_card.rotate (180)
    display_card_prepped=ImageTk.PhotoImage(display_card)
    display_card_label=Label(card_space, image=display_card_prepped)
    display_card_label.image=display_card_prepped
    display_card_label.pack ()
    display_card_label.place (x=125*cardindex, y=25)
    
        


   
   

background_image=PhotoImage(file="bg.gif")
    
cardback_image=PhotoImage(file="CardBacks.gif")
    
   

card_button=Button(root, image=cardback_image, width=100, height=175)
card_button.pack ()
card_button.place (x=0, y=0)
card_button.bind("<Button-1>", make_label)
        
reshuffle_button=Button (root, bg="pink", text="Shuffle")
reshuffle_button.pack()
reshuffle_button.place (x=0, y=300)
reshuffle_button.bind("<Button-1>", reshuffle_cards)

cardlist=create_deck()
card_space=Frame(root, bg="pink", width=2000, height=1850)

card_space.place (x=110, y=0)
card_space.grid_propagate=False



Tk.mainloop(root)


    
    

