import deckofcards
from tkinter import *
from PIL import Image, ImageTk
import random
import turtle

root=Tk()
root.title ("Tarot Reading")
root.geometry ("2000x2000")

cardindex=0
spread_reference_dictionary={"Past/Present/Future":{1:[200, 25, "Past"], 2: [500, 25, "Present"], 3:[800, 25, "Future"], 4: [200, 225, ""], 5:[200, 425, ""]},
                             "Goal/Challenge/Outcome": {1:[200, 25, "Goal"], 2: [500, 25, "Challenge"], 3:[800, 25, "Outcome"]},
                             "You/Them/Relationship": {1:[200, 25, "You"], 2: [500, 25, "Them"], 3:[800, 25, "Relationship"]},
                             "Default": {1:[100, 15, ""], 2: [250 ,15 ,""], 3:[400, 15, ""], 4: [550, 15, ""], 5: [700, 15, ""], 6: [850, 15, ""],7:[1000, 15, ""],
                                         8:[100, 215, ""], 9:[250, 215, ""], 10:[400, 215, ""], 11:[550, 215,""],12: [700, 215, ""], 13:[850, 215, ""], 14:[1000, 215, ""],
                                         15: [100, 415, ""], 16:[250, 415,""], 17: [400, 415, ""], 18: [550, 415, ""], 19: [700, 415, ""], 20: [850, 415, ""], 21: [1000, 415,""]}}
                             

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




class Spread_Position:
    def __init__ (self, xcoord, ycoord, label):
        self.xcoord=xcoord
        self.ycoord=ycoord
        self.label=label
    def define_position (self, frame):
        spread_position=Label (frame, height=13, width=13, anchor="s", text=self.label, relief="solid", bg="medium aquamarine")
        spread_position.pack()
        spread_position.place (x=self.xcoord, y=self.ycoord)

    
        
        
def create_spread():
    global card_space, spread_reference_dictionary, spreadname
    cardspacelist=[]
    
        
    attrib_dict=spread_reference_dictionary.get(spreadname)
    for k in attrib_dict:
        attrib_list=attrib_dict.get (k)
            
        xcoord=attrib_list[0]
        ycoord=attrib_list[1]
        label=attrib_list[2]
        card_place=Spread_Position(xcoord, ycoord, label)
        cardspacelist.append (card_place)
        card_place.define_position (card_space)
    
        
    
            
        

    
    
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



    
def shuffle_cards (event):
    global cardindex, card_space, cardlist, spreadname
    for widget in card_space.winfo_children():
            widget.destroy()
    spreadname=""
    cardindex=0
    for c in cardlist:
        reverse=random.randrange (0,5)
        if reverse==4:
            c.reverse_card()
    random.shuffle (cardlist)
    cardindex=0
    
    
    
    
    
    
def make_label():
    
    
    ourcard=draw_card()
    card_image=ourcard.filename
    display_card=Image.open(card_image)
    display_card=display_card.resize ((100, 175))
    if ourcard.reverse==True:
        display_card=display_card.rotate (180)
    display_card_prepped=ImageTk.PhotoImage(display_card)
    display_card_label=Label(card_space, image=display_card_prepped)
    display_card_label.image=display_card_prepped
    return display_card_label
    
def place_card(event):
    global spreadname, spread_reference_dictionary, card_space, cardindex
    if spreadname=="":
        
        spreadname="Default"
    
    dictref=spread_reference_dictionary.get (spreadname)
    
    
    lookup=cardindex+1
    placetogo=dictref.get(lookup)
    if placetogo!=None:
            
        card=make_label()
            
        
            
        xcoord=placetogo[0]
        ycoord=placetogo[1]
        card.pack()
        card.place(x=xcoord, y=ycoord)
    
            
            
    
        
    


        
        
        
        
        
    


def option_handler(event):
    global spreadname, cardindex
    for widget in card_space.winfo_children():
            widget.destroy()
    cardindex=0
    selection=choice.get()
    spreadname=selection
    
    
    
    
    
       
    create_spread ()
        
    

   


background_image=PhotoImage(file="bg.gif")
    
cardback_image=PhotoImage(file="CardBacks.gif")
    
   

card_button=Button(root, image=cardback_image, width=100, height=175)
card_button.pack ()
card_button.place (x=0, y=0)
card_button.bind("<Button-1>", place_card)

shuffle_button=Button (root, bg="pink", text="Clear and Shuffle")
shuffle_button.pack()
shuffle_button.place (x=0, y=250)
shuffle_button.bind("<Button-1>", shuffle_cards)

choice=StringVar(root)
choice.set("Spread")
option=OptionMenu (root, choice, "Past/Present/Future", "Goal/Challenge/Outcome", "You/Them/Relationship", command=option_handler)
option.config(width=15)
option.pack()
option.place (x=0, y=350)

cardlist=create_deck()
card_space=Frame(root, bg="pink", width=2000, height=1850)



card_space.place (x=110, y=0)
card_space.grid_propagate=False

spreadname=""

Tk.mainloop(root)


    
    

