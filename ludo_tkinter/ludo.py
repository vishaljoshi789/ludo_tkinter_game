from tkinter import *
import random
from PIL import ImageTk, Image
root = Tk()
number = 0
turn = "green"
# button = ''
m = 1
# gui window
window_width = 750
window_height = 750
root.geometry(("750x750"))
root.title("Ludo By Vishal")
root.maxsize(window_width, window_height)
root.minsize(window_width, window_height)
old = 0


# canvas
shape = Canvas(root, width=window_width, height=window_height)
shape.pack()


def numberzero():
    global number
    number = 0

# def buttonblank():
#     global button
#     button = ""
# function
# dicefunction

def chaturn():
    global turn

    if turn == "blue":
            turn = "red"
            shape.create_rectangle(10, 10, 290, 290, width=10, outline="blue")
            shape.create_rectangle(460, 10, 740, 290, width=10)
            r1.place(x=r1.winfo_x(), y=r1.winfo_y())
            r2.place(x=r2.winfo_x(), y=r2.winfo_y())
            r3.place(x=r3.winfo_x(), y=r3.winfo_y())
            r4.place(x=r4.winfo_x(), y=r4.winfo_y())
            print("red turn")
    elif turn == "red":
            turn = "yellow"
            shape.create_rectangle(460, 10, 740, 290, width=10, outline="red")
            shape.create_rectangle(460, 460, 740, 740, width=10)
            y1.place(x=y1.winfo_x(), y=y1.winfo_y())
            y2.place(x=y2.winfo_x(), y=y2.winfo_y())
            y3.place(x=y3.winfo_x(), y=y3.winfo_y())
            y4.place(x=y4.winfo_x(), y=y4.winfo_y())
            print("yellow turn")
    elif turn == "yellow":
            turn = "green"
            shape.create_rectangle(460, 460, 740, 740, width=10, outline="yellow")
            shape.create_rectangle(10, 460, 290, 740, width=10)
            g1.place(x=g1.winfo_x(), y=g1.winfo_y())
            g2.place(x=g2.winfo_x(), y=g2.winfo_y())
            g3.place(x=g3.winfo_x(), y=g3.winfo_y())
            g4.place(x=g4.winfo_x(), y=g4.winfo_y())
            print("green turn")
    elif turn == "green":
            turn = "blue"
            shape.create_rectangle(10, 460, 290, 740, width=10, outline="green")
            shape.create_rectangle(10, 10, 290, 290, width=10)
            b1.place(x=b1.winfo_x(), y=b1.winfo_y())
            b2.place(x=b2.winfo_x(), y=b2.winfo_y())
            b3.place(x=b3.winfo_x(), y=b3.winfo_y())
            b4.place(x=b4.winfo_x(), y=b4.winfo_y())
            print("blue turn")






def dicerolled():
    global number, old
    number = random.randint(1, 6)
    if number == 1:
        img = "1.png"
    elif number == 2:
        img = "2.png"
    elif number == 3:
        img = "3.png"
    elif number == 4:
        img = "4.png"
    elif number == 5:
        img = "5.png"
    elif number == 6:
        img = "6.png"
    img = Image.open(img)
    img = img.resize((100, 100), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    # img = shape.create_image(375, 365, image=image)
    # Canvas.tag_raise(img)
    if old!=6:    
        chaturn()
        print(number)
    else:
        print(turn, "turn")
        print(number)
    img = Label(root, image=image)
    img.image = image
    img.place(x=325, y=310) 
    old = number
    
    return number

    
def bottoncheck(button_id):
    global button
    if button_id == "b1":
        button = b1
    elif button_id == "b2":
        button = b2
    elif button_id == "b3":
        button = b3
    elif button_id == "b4":
        button = b4
    elif button_id == "r1":
        button = r1
    elif button_id == "r2":
        button = r2
    elif button_id == "r3":
        button = r3
    elif button_id == "r4":
        button = r4
    elif button_id == "g1":
        button = g1
    elif button_id == "g2":
        button = g2
    elif button_id == "g3":
        button = g3
    elif button_id == "g4":
        button = g4
    elif button_id == "y1":
        button = y1
    elif button_id == "y2":
        button = y2
    elif button_id == "y3":
        button = y3
    elif button_id == "y4":
        button = y4
    chance()


def chance():
    if turn == "blue":
        if button in [b1, b2, b3, b4]:
            path()
           
        else:
            print("ITS BLUE TURN!!")
    elif turn == "red":
        if button in [r1, r2, r3, r4]:
            path()
            
        else:
            print("ITS RED TURN!!")
    elif turn == "yellow":
        if button in [y1, y2, y3, y4]:
            path()
            
        else:
            print("ITS YELLOW TURN!!")
    elif turn == "green":
        if button in [g1, g2, g3, g4]:
            path()
            
        else:
            print("ITS GREEN TURN!!")




# def overlaping():
#     blue_x = {"b1" : b1.winfo_x(), "b2" : b2.winfo_x(), "b3" : b3.winfo_x(), "b4": b4.winfo_x()}
#     blue_y = {"b1" : b1.winfo_y(), "b2" : b2.winfo_y(), "b3" : b3.winfo_y(), "b4": b4.winfo_y()}

#     green_x = {"g1" : g1.winfo_x(), "g2" : g2.winfo_x(), "g3" : g3.winfo_x(), "g4" : g4.winfo_x()}
#     green_y = {"g1" : g1.winfo_y(), "g2" : g2.winfo_y(), "g3" : g3.winfo_y(), "g4" : g4.winfo_y()}

#     red_x = {"r1" : r1.winfo_x(), "r2" : r2.winfo_x(), "r3" : r3.winfo_x(), "r4" : r4.winfo_x()}
#     red_y = {"r1" : r1.winfo_y(), "r2" : r2.winfo_y(), "r3" : r3.winfo_y(), "r4" : r4.winfo_y()}

#     yellow_x = {"y2" : y1.winfo_x(), "y2" : y2.winfo_x(), "y3" : y3.winfo_x(), "y4" : y4.winfo_x()}
#     yellow_y = {"y2" : y1.winfo_y(), "y2" : y2.winfo_y(), "y3" : y3.winfo_y(), "y4" : y4.winfo_y()}

#     buttonx = button.winfo_x()
#     buttony = button.winfo_y()

#     if turn=="blue":
#         if buttonx in green_x.values() and buttony in green_y.values():
#             if green_x.keys()[green_x.values().index[buttonx]] in [g1, g2, g3, g4]:

#                 count = 3
#                 while count>=0:
#                     a = list(green_x.keys())[count]
#                     b = list(green_y.keys())[count]
#                     if buttonx == a and buttony == b:
#                         if count == 0:
#                             g1.place(x = 50, y = 500)
#                         elif count == 1:
#                             g2.place(x = 175, y = 500)
#                         elif count == 2:
#                             g3.place(x = 50, y = 650)
#                         elif count == 3:
#                             g4.place(x = 175, y = 650)
#                     count-=1
#             else:
#                 print("task 1 failed")
#         else:
#             print("task 2 failed")
#         print(button.winfo_x(), button.winfo_y())
#         elif buttonx in red_x and buttony in red_y:
#             count = 3
#             while count>=0:
#                 a = red_x[count]
#                 b = red_y[count]
#                 if buttonx == a and buttony == b:
#                     if count == 0:
#                         r1.place(x = 500, y = 50)
#                     elif count == 1:
#                         r2.place(x = 650, y = 50)
#                     elif count == 2:
#                         r3.place(x = 500, y = 200)
#                     elif count == 3:
#                         r4.place(x = 650, y = 200) 
#                 count-=1
#         elif buttonx in yellow_x and buttony in yellow_y:
#             count = 3
#             while count>=0:
#                 a = yellow_x[count]
#                 b = yellow_y[count]
#                 if buttonx == a and buttony == b:
#                     if count == 0:
#                         y1.place(x = 500, y = 500)
#                     elif count == 1:
#                         y2.place(x = 650, y = 50)
#                     elif count == 2:
#                         y3.place(x = 500, y = 650)
#                     elif count == 3:
#                         y4.place(x = 650, y = 650)
#                 count-=1
    
        
        
#     elif turn!="red":
#         count = 3
#         while count>=0:
#             x = red_x[count]
#             y = red_y[count]
#             if buttonx == x and buttony == y:
#                 if r1.winfo_x() == buttonx:
#                     r1.place(x = 500, y = 50)
#                 if r2.winfo_x() == buttonx:
#                     r2.place(x = 650, y = 50)
#                 if r3.winfo_x() == buttonx:
#                     r3.place(x = 500, y = 200)
#                 if r4.winfo_x() == buttonx:
#                     r4.place(x = 650, y = 200) 
#             count-=1
        
#     elif turn!="green":
#         count = 3
#         while count>=0:
#             x = green_x[count]
#             y = green_y[count]
#             if buttonx == x and buttony == y:
#                 if g1.winfo_x() == buttonx:
#                     g1.place(x = 50, y = 500)
#                 if g2.winfo_x() == buttonx:
#                     g2.place(x = 175, y = 500)
#                 if g3.winfo_x() == buttonx:
#                     g3.place(x = 50, y = 650)
#                 if g4.winfo_x() == buttonx:
#                     g4.place(x = 175, y = 650) 
#             count-=1
        
#     elif turn!="yellow":
#         count = 3
#         while count>=0:
#             x = yellow_x[count]
#             y = yellow_y[count]
#             if buttonx == x and buttony == y:
#                 if y1.winfo_x() == buttonx:
#                     y1.place(x = 500, y = 500)
#                 if y2.winfo_x() == buttonx:
#                     y2.place(x = 650, y = 50)
#                 if y3.winfo_x() == buttonx:
#                     y3.place(x = 500, y = 650)
#                 if y4.winfo_x() == buttonx:
#                     y4.place(x = 650, y = 650) 
#             count-=1
                        





def path():
    buttonx = button.winfo_x()
    buttony = button.winfo_y()
    if number == 6 and (buttonx == 500 and buttony == 50):
        button.place(x=400, y=50)
        numberzero()
    elif number == 6 and (buttonx == 175 and buttony == 50):
        button.place(x=50, y=300)
        numberzero()
    elif number == 6 and (buttonx == 50 and buttony == 200):
        button.place(x=50, y=300)
        numberzero()
    elif number == 6 and (buttonx == 175 and buttony == 200):
        button.place(x=50, y=300)
        numberzero()

    elif number == 6 and (buttonx == 500 and buttony == 50):
        button.place(x=400, y=50)
        numberzero()
    elif number == 6 and (buttonx == 650 and buttony == 50):
        button.place(x=400, y=50)
        numberzero()
    elif number == 6 and (buttonx == 500 and buttony == 200):
        button.place(x=400, y=50)
        numberzero()
    elif number == 6 and (buttonx == 650 and buttony == 200):
        button.place(x=400, y=50)
        numberzero()

    elif number == 6 and (buttonx == 50 and buttony == 500):
        button.place(x=300, y=650)
        numberzero()
    elif number == 6 and (buttonx == 175 and buttony == 500):
        button.place(x=300, y=650)
        numberzero()
    elif number == 6 and (buttonx == 50 and buttony == 650):
        button.place(x=300, y=650)
        numberzero()
    elif number == 6 and (buttonx == 175 and buttony == 650):
        button.place(x=300, y=650)
        numberzero()

    elif number == 6 and (buttonx == 500 and buttony == 500):
        button.place(x=650, y=400)
        numberzero()
    elif number == 6 and (buttonx == 650 and buttony == 500):
        button.place(x=650, y=400)
        numberzero()
    elif number == 6 and (buttonx == 500 and buttony == 650):
        button.place(x=650, y=400)
        numberzero()
    elif number == 6 and (buttonx == 650 and buttony == 650):
        button.place(x=650, y=400)
        numberzero()
    elif buttonx in range(0, 251, 50) and buttony == 300:
        if buttonx+50*number in range(0, 251, 50):
            button.place(x=buttonx + 50*number, y=300)
            numberzero()
        else:
            count = number-((250-buttonx)//50)
            button.place(x=300, y=buttony-50*(count))
            numberzero()
    elif buttonx == 300 and buttony in range(0, 251, 50):
        if buttony-50*number in range(0, 251, 50):
            button.place(y=buttony - 50*number, x=300)
            numberzero()
        else:
            count = number-((buttony)//50)
            if button in [r1, r2, r3, r4]:
                if count>1:
                        count-=1
                        button.place(x=350,y=50*count)
                        numberzero()
                elif count==1:
                        button.place(x=350,y=0)
                        numberzero()
            else:
                
                if count > 2:
                    count -= 2
                    button.place(x=400, y=count*50)
                    numberzero()
                else:
                    button.place(x=300+(count*50), y=0)
                    numberzero()

    elif buttony in range(0, 301, 50) and buttonx == 350:
        if button in [r1, r2, r3, r4]:
            if buttonx==350 and buttony in range(0,301,50):
                if buttony+50*number in range(0, 251, 50):
                        button.place(y=buttony + 50*number, x=350)
                        numberzero()
                elif buttony+50*number == 300:
                        button.destroy()
                        numberzero()
        else:
            count = number
            if count == 1:
                button.place(x=400, y=0)
                numberzero()
            elif count > 1:
                count -= 1
                button.place(x=400, y=50*count)
                numberzero()
    elif buttonx == 400 and buttony in range(0, 251, 50):
        if buttony+50*number in range(0, 251, 50):
            button.place(y=buttony + 50*number, x=400)
            numberzero()
        else:
            count = number-((250-buttony)//50)
            button.place(y=300, x=buttonx+50*(count))
            numberzero()

    elif buttony == 300 and buttonx in range(450, 701, 50):
        if buttonx+50*number in range(450, 701, 50):
            button.place(x=buttonx + 50*number, y=300)
            numberzero()
        else:
            count = number-((700 - buttonx)//50)
            if button in [y1, y2, y3, y4]:
                if count>1:
                        count-=1
                        button.place(y=350,x=700 - 50*count)
                        numberzero()
                elif count==1:
                        button.place(y=350,x=700)
                        numberzero()
            else:
                if count > 2:
                    count -= 2
                    button.place(y=400, x=700-(count*50))
                    numberzero()
                else:
                    button.place(y=300+(count*50), x=700)
                    numberzero()

    elif buttony == 350 and buttonx in range(400,701, 50):
        if button in [y1, y2, y3, y4]:
            if buttony==350 and buttonx in range(400,701, 50):
                if buttonx-50*number in range(450,701, 50):
                        button.place(x=buttonx - 50*number, y=350)
                        numberzero()
                elif buttonx-50*number == 400:
                        button.destroy()
                        numberzero()
        else:
            count = number
            if count == 1:
                button.place(y=400, x=700)
                numberzero()
            elif count > 1:
                count -= 1
                button.place(y=400, x=700 - (50*count))
                numberzero()

    elif buttony == 400 and buttonx in range(450, 701, 50):
        if buttonx-50*number in range(450, 701, 50):
            button.place(x=buttonx - 50*number, y=400)
            numberzero()
        else:
            count = number - ((buttonx - 450)//50)
            button.place(x=400, y=400+(count*50))
            numberzero()

    elif buttonx == 400 and buttony in range(450, 701, 50):
        if buttony+50*number in range(450, 701, 50):
            button.place(y=buttony + 50*number, x=400)
            numberzero()
        else:
            count = number-((700-buttony)//50)
            if button in [g1, g2, g3, g4]:
                if count>1:
                        count-=1
                        button.place(x=350,y=700 - 50*count)
                        numberzero()
                elif count==1:
                        button.place(x=350,y=700)
                        numberzero()
            else:
                if count > 2:
                    count -= 2
                    button.place(x=300, y=700 - (count*50))
                    numberzero()
                else:
                    button.place(y=700, x=400-(count*50))
                    numberzero()

    elif buttonx == 350 and buttony in range(400,701, 50):
        if button in [g1, g2, g3, g4]:
            if buttonx==350 and buttony in range(400,701, 50):
                if buttony-50*number in range(450,701, 50):
                        button.place(y=buttony - 50*number, x=350)
                        numberzero()
                elif buttony-50*number == 400:
                        button.destroy()
                        numberzero()
        else:
            count = number
            if count > 1:
                count -= 1
                button.place(x=300, y=700 - (count*50))
                numberzero()
            elif count == 1:
                button.place(x=300, y=700)
                numberzero()

    elif buttonx == 300 and buttony in range(450, 701, 50):
        if buttony-50*number in range(450, 701, 50):
            button.place(y=buttony - 50*number, x=300)
            numberzero()
        else:
            count = number-((buttony - 450)//50)
            button.place(x=300 - (count*50), y=400)
            numberzero()

    elif buttonx in range(0, 251, 50) and buttony == 400:
        if buttonx-50*number in range(0, 251, 50):
            button.place(x=buttonx - 50*number, y=400)
            numberzero()
        else:
            count = number - ((buttonx)//50)
            if button in [b1, b2, b3, b4]:
                if count>1:
                        count-=1
                        button.place(y=350,x=50*count)
                        numberzero()
                elif count==1:
                        button.place(y=350,x=0)
                        numberzero()
            else:
                if count > 2:
                    count -= 2
                    button.place(x=count*50, y=300)
                    numberzero()
                else:
                    button.place(x=0, y=400-(count*50))
                    numberzero()

    elif buttonx in range(0,301, 50) and buttony == 350:
        if button in [b1, b2, b3, b4]:
            if buttony==350 and buttonx in range(0,301, 50):
                if buttonx+50*number in range(0,301, 50):
                        button.place(x=buttonx + 50*number, y=350)
                        numberzero()
                elif buttonx+50*number == 400:
                        button.destroy()
                        numberzero()
        else:
            count = number
            if count == 1:
                button.place(x=0, y=300)
                numberzero()
            elif count > 1:
                count -= 1
                button.place(x=count*50, y=300)
                numberzero()
    print(button.winfo_x(), button.winfo_y())

    







# rectangle
blue_rectangle = shape.create_rectangle(0, 0, 300, 300, fill="blue", width=3)
red_rectangle = shape.create_rectangle(450, 0, 750, 300, fill="red", width=3)
green_rectangle = shape.create_rectangle(
    0, 450, 300, 750, fill="green", width=3)
yellow_rectangle = shape.create_rectangle(
    450, 450, 750, 750, fill="yellow", width=3)
# victory_rectangle = shape.create_rectangle(
#     300, 300, 450, 450, fill="grey", width=3)


# lines

shape.create_line(300, 0, 450, 0, width=3)
shape.create_line(750, 300, 750, 450, width=3)
shape.create_line(300, 750, 450, 750, width=3)
shape.create_line(0, 300, 0, 450, width=3)

shape.create_line(350, 0, 350, 300, width=3)
shape.create_line(400, 0, 400, 300, width=3)
shape.create_line(450, 400, 750, 400, width=3)
shape.create_line(450, 350, 750, 350, width=3)
shape.create_line(350, 450, 350, 750, width=3)
shape.create_line(400, 450, 400, 750, width=3)
shape.create_line(0, 400, 300, 400, width=3)
shape.create_line(0, 350, 300, 350, width=3)

shape.create_line(300, 50, 450, 50, width=3)
shape.create_line(300, 100, 450, 100, width=3)
shape.create_line(300, 150, 450, 150, width=3)
shape.create_line(300, 200, 450, 200, width=3)
shape.create_line(300, 250, 450, 250, width=3)

shape.create_line(700, 300, 700, 450, width=3)
shape.create_line(500, 300, 500, 450, width=3)
shape.create_line(550, 300, 550, 450, width=3)
shape.create_line(600, 300, 600, 450, width=3)
shape.create_line(650, 300, 650, 450, width=3)

shape.create_line(300, 700, 450, 700, width=3)
shape.create_line(300, 500, 450, 500, width=3)
shape.create_line(300, 550, 450, 550, width=3)
shape.create_line(300, 600, 450, 600, width=3)
shape.create_line(300, 650, 450, 650, width=3)

shape.create_line(50, 300, 50, 450, width=3)
shape.create_line(100, 300, 100, 450, width=3)
shape.create_line(150, 300, 150, 450, width=3)
shape.create_line(200, 300, 200, 450, width=3)
shape.create_line(250, 300, 250, 450, width=3)


# gotiyan
b1 = Button(root, width=3, height=2, bg="blue", highlightbackground="black",
            activebackground="#1589FF", command=lambda: [bottoncheck("b1")])
b1.place(x=50, y=50)
b2 = Button(root, width=3, height=2, bg="blue", highlightbackground="black",
            activebackground="#1589FF", command=lambda: [bottoncheck("b2")])
b2.place(x=175, y=50)
b3 = Button(root, width=3, height=2, bg="blue", highlightbackground="black",
            activebackground="#1589FF", command=lambda: [bottoncheck("b3")])
b3.place(x=50, y=200)
b4 = Button(root, width=3, height=2, bg="blue", highlightbackground="black",
            activebackground="#1589FF", command=lambda: [bottoncheck("b4")])
b4.place(x=175, y=200)

r1 = Button(root, width=3, height=2, bg="red", highlightbackground="black",
            activebackground="#E41B17", command=lambda: [bottoncheck("r1")])
r1.place(x=500, y=50)
r2 = Button(root, width=3, height=2, bg="red", highlightbackground="black",
            activebackground="#E41B17", command=lambda: [bottoncheck("r2")])
r2.place(x=650, y=50)
r3 = Button(root, width=3, height=2, bg="red", highlightbackground="black",
            activebackground="#E41B17", command=lambda: [bottoncheck("r3")])
r3.place(x=500, y=200)
r4 = Button(root, width=3, height=2, bg="red", highlightbackground="black",
            activebackground="#E41B17", command=lambda: [bottoncheck("r4")])
r4.place(x=650, y=200)

g1 = Button(root, width=3, height=2, bg="green", highlightbackground="black",
            activebackground="#3EA055", command=lambda: [bottoncheck("g1")])
g1.place(x=50, y=500)
g2 = Button(root, width=3, height=2, bg="green", highlightbackground="black",
            activebackground="#3EA055", command=lambda: [bottoncheck("g2")])
g2.place(x=175, y=500)
g3 = Button(root, width=3, height=2, bg="green", highlightbackground="black",
            activebackground="#3EA055", command=lambda: [bottoncheck("g3")])
g3.place(x=50, y=650)
g4 = Button(root, width=3, height=2, bg="green", highlightbackground="black",
            activebackground="#3EA055", command=lambda: [bottoncheck("g4")])
g4.place(x=175, y=650)

y1 = Button(root, width=3, height=2, bg="yellow", highlightbackground="black",
            activebackground="#FFF380", command=lambda: [bottoncheck("y1")])
y1.place(x=500, y=500)
y2 = Button(root, width=3, height=2, bg="yellow", highlightbackground="black",
            activebackground="#FFF380", command=lambda: [bottoncheck("y2")])
y2.place(x=650, y=500)
y3 = Button(root, width=3, height=2, bg="yellow", highlightbackground="black",
            activebackground="#FFF380", command=lambda: [bottoncheck("y3")])
y3.place(x=500, y=650)
y4 = Button(root, width=3, height=2, bg="yellow", highlightbackground="black",
            activebackground="#FFF380", command=lambda: [bottoncheck("y4")])
y4.place(x=650, y=650)


# ROLL BUTTON
roll = Button(root, text="Roll", bg="#7bccb5", highlightbackground="black",
              font="Monaco", activebackground="#7fffd4", command=dicerolled)
roll.place(x=347, y=418)


# safe areas

safe1 = shape.create_rectangle(50, 300, 100, 350, fill="grey", width=2)
safe2 = shape.create_rectangle(300, 100, 350, 150, fill="grey", width=2)
safe3 = shape.create_rectangle(400, 50, 450, 100, fill="grey", width=2)
safe4 = shape.create_rectangle(650, 300, 600, 350, fill="grey", width=2)
safe5 = shape.create_rectangle(700, 400, 650, 450, fill="grey", width=2)
safe6 = shape.create_rectangle(400, 600, 450, 650, fill="grey", width=2)
safe7 = shape.create_rectangle(300, 650, 350, 700, fill="grey", width=2)
safe8 = shape.create_rectangle(100, 400, 150, 450, fill="grey", width=2)
safe = [safe1, safe2, safe3, safe4, safe5, safe6, safe7, safe8]


root.mainloop()
