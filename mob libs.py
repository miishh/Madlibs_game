from tkinter import *
root=Tk()
root.geometry("600x300")
root.title("MadLibs")
root.config(bg="lightcyan2")
Label(root,text="Come On! Lets Build Our Own Story ",font="Fixedsys 20 bold",fg="deeppink",bg="lightcyan2").pack()
Label(root,text="Have Fun!! \n",font="ComicSansMS 18 bold",fg="gray3",bg="lightcyan2").pack()
Label(root,text="Choose any one story you want to construct!",font="ComicSansMS 18 bold",fg="royalblue",bg="lightcyan2").pack()

      
def madlibs1():
    print("Lets Begin!(❁´◡`❁) ")
    holiday=input(" Tell your favourite holiday :")
    noun=input("Give a noun :")
    place=input("A place you'd love to vist :")
    person=input("Name down a person you know :")
    adjective=input("Need an adjective :")
    bodypart=input("We are almost there! o(^▽^)o \nTell a plural body part :")
    verb=input("Type down a verb(present tense) :")
    noun1=input("Another noun Needed! :")
    food=input("Your favourite food :")
    noun2=input("Last one! \nTell a plural noun :")
    
    print("Here comes your story!! (●ˇ∀ˇ●)\n")

    print("I can't believe its already "+ holiday +"! I can't wait to put on my "+ noun +" and visit every "+ place+ " in my neighbourhood.This year, I am going to dress up as "
        + person+ " with " + adjective +" "+ bodypart+ " . Before I "+ verb +" ,I make sure to grab my "+ noun1+ " to hold all of my "+ food+ " . Finally,all of my "+ noun2+
        " are ready to go! \n \nGood Job! It was fun!! ヾ(≧ ▽ ≦)ゝ \n \n")
    
def madlibs2():
    print("Lets Begin!(❁´◡`❁) ")
    toy=input("Tell your favourite toy :")
    musicalinstrument=input("Any musical instrument you like :")
    noun=input("Give a noun(place):")
    desert=input("Name your favourite dessert :")
    snack=input("Tell a snack :")
    verb=input("Write down a verb :")
    animal=input("Give an animal(s) name :")
    noun1=input("Another noun(plural) :")
    number=input("Tell a number of your choice :")
    noun2=input("We are almost there! o(^▽^)o \nGive one more noun :")
    number1=input("Another number Needed :")
    number2=input("One more number (^_+):")
    vehicle=input("A vehicle of your choice :")
    animal1=input("And here we finish\nAnimal you'd like to pet : ")

    print("Here comes your story!! (●ˇ∀ˇ●)\n")
    
    print("If I was Principal of my school, I'd put " +toy+ " and "+musicalinstrument+ " in every "+noun+" and have the caffeteria serve "+ desert +
          " and "+snack+ " for lunch. We would have ' "+verb+ " and Tell' every day,where students can bring " +animal+ " and "+ noun1+
          " to share in class.Students would give teachers homework,like "+number+ " page book reports about "+noun2+ " and "+number1+ " math problems.Recess would last for "+number2+
          " hours,and instead of buses,i'd have "+vehicle+ " and "+animal1+" take the kids to and from school. \n \nGood Job! It was fun!! ヾ(≧ ▽ ≦)ゝ\n \n")




def madlibs3():
    print("Lets Begin!(❁´◡`❁) ")
    noun=input("Give a noun(plural) :")
    adjective=input("Tell an adjective :")
    animal=input("A plural noun :")
    noun1=input("Another noun required :")
    adjective1=input("One more adjective :")
    color=input("A color You prefer :")
    adjective2=input("Tell an adjective :")
    noun2=input("Give another noun :")
    noun3=input("We are almost there! o(^▽^)o \nWant one more noun :")
    adjective3=input("Another adjective :")
    verb=input("Mention a verb :")
    noun4=input("Give another noun :")
    verb1=input("Another verb required(past tense):")
    noun4=input("Need a noun :")
    adjective4=input("And here's the last one \nTell an adjective :")

    print("Here comes your story!! (●ˇ∀ˇ●) \n")
    
    print("Unicorns aren't like other " +noun+ " ;they are "+adjective+ " .They look like "+animal+" ,with "+ noun1 +
          " for feet and a " + adjective1 + " mane of hair.But unicorns are "+color+ " and have a " + adjective2 +" "  + noun2 +
          " on their head.Some "+ noun3 + " don't believe unicorns are "+adjective3 + " but I believe in them.I would love to "+verb + " a unicorn to faraway "+noun4+
          " .One thing I've always "+verb1+ " about is whether unicorns' poop is rainbow coloured,or is their "+ noun4 +" "  + adjective4+ " like other animals?  \n \nGood Job! It was fun!!ヾ(≧ ▽ ≦)ゝ\n \n")
    

                
Button(root, text= "Unicorns", font ='arial 15', command= madlibs3, bg = 'pink' ,fg="gray25").place(x=40, y=160)
Button(root, text= 'If I was principal', font ='arial 15', command= madlibs2, bg = 'pink' ,fg="gray25").place(x=190, y=160)
Button(root, text= 'The Halloween', font ='arial 15', command= madlibs1, bg = 'pink' ,fg="gray25").place(x=420, y=160)

root.mainloop()





