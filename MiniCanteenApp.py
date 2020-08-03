from tkinter import *
import random
import time
import os
import webbrowser

# for printing local time
localtime = time.asctime(time.localtime(time.time()))
app_folder = os.path.dirname(__file__)
price_list = os.path.join(app_folder, "price_list.txt")
log = os.path.join(app_folder, "account_log.txt")
data = ""

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='1600x800+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom = geom

# window
mini = Tk()
mini.title("Mini Canteen -NITC")
FullScreenApp(mini)

# Frames
ftframes = Frame(mini, width=800, height=200, bg="MediumOrchid4", relief=SUNKEN)
ftframes.pack(side=TOP)

title = Label(ftframes, font=('arial', 50, 'bold'), text="MINI CANTEEN NITC", fg="MediumOrchid1", bd=10, anchor='w')
title.grid(row=0, column=0)
title = Label(ftframes, font=('arial', 50, 'bold'), text=localtime, fg="MediumOrchid4", bd=10, anchor='w')
title.grid(row=1, column=0)
Lframe = Frame(mini, width=800, height=800, bg="Plum3", relief=SUNKEN)
Lframe.pack(side=RIGHT)
Rframe = Frame(mini, width=800, height=800, relief=SUNKEN)
Rframe.pack(side=LEFT)


# =============================Functions===========================

def writetolog():
    global data
    if data != "":
        file = open(log,"a")
        file.write("\n\n" + data)
        file.close()
        data = ""
    return

def arrdata(item,no,cost): #arrange in good format
    if no == 0:
        return ""
    det = "\n" + item + (25-len(item)) * " " + str(no)
    det = det + (40-len(det))* " " + str(cost)
    return det

def viewlog():
    webbrowser.open(log)
    return

# ====================Calculator_function==========================

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btncleardisplay():
    global operator
    operator = ""
    text_input.set("")


def btnequalsinput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


# =======================Function for Total=======================
def Ref():
    global data
    data = ""
    x = random.randint(54151, 969594)
    randomRef = str(x)
    rand.set(randomRef)

    if len(Meals.get())==0:
        No_of_Meals=0
    else:
        No_of_Meals = float(Meals.get())
#------------------------------------------------
    if len(Porotta.get())==0:
        No_of_Porotta=0
    else:
        No_of_Porotta = float(Porotta.get())
#------------------------------------------------
    if len(Chappati.get())==0:
        No_of_Chappati = 0
    else:
        No_of_Chappati = float(Chappati.get())
#---------------------------------------------------
    if len(Kubbus.get())==0:
        No_of_Kubbus=0
    else:
        No_of_Kubbus = float(Kubbus.get())
#---------------------------------------------------
    if len(Chicken65.get())==0:
        No_of_Chicken65=0
    else:
        No_of_Chicken65 = float(Chicken65.get())
#--------------------------------------------------
    if len(BeefFry.get())==0:
        No_of_BeefFry=0
    else:
        No_of_BeefFry = float(BeefFry.get())
#-----------------------------------------------------
    if len(ChickenFriedRice.get())==0:
        No_of_ChickenFriedRice=0
    else:
        No_of_ChickenFriedRice = float(ChickenFriedRice.get())
#---------------------------------------------------------
    if len(VegCurry.get())==0:
        No_of_VegCurry=0
    else:
        No_of_VegCurry = float(VegCurry.get())
#------------------------------------------------------------
    if len(EggFriedRice.get())==0:
        No_of_EggFriedRice=0
    else:
        No_of_EggFriedRice = float(EggFriedRice.get())

#-----------------------------------------------------------
    Cost_of_Meals = No_of_Meals * price_of_Meals
    Cost_of_Porotta = No_of_Porotta * price_of_Porotta
    Cost_of_Chappati = No_of_Chappati * price_of_Chappati
    Cost_of_Kubbus = No_of_Kubbus * price_of_Kubbus
    Cost_of_Chicken65 = No_of_Chicken65 * price_of_Chicken65
    Cost_of_BeefFry = No_of_BeefFry * price_of_BeefFry
    Cost_of_ChickenFriedRice = No_of_ChickenFriedRice * price_of_ChickenFriedRice
    Cost_of_VegCurry = No_of_VegCurry * price_of_VegCurry
    Cost_of_EggFriedRice = No_of_EggFriedRice * price_of_EggFriedRice

    Subtotal = Cost_of_Meals + Cost_of_Porotta + Cost_of_Chappati + Cost_of_Kubbus + Cost_of_Chicken65 + Cost_of_BeefFry + Cost_of_ChickenFriedRice + Cost_of_VegCurry + Cost_of_EggFriedRice
    Tax = Subtotal * decimal_of_GST

    Taxalias = "Rs.", str('%.2f' % Tax)
    Totalalias = "Rs.", str('%.2f' % (Subtotal + Tax))
    GST.set(Taxalias)
    Total.set(Totalalias)

    if  Subtotal + Tax != 0:

        data = data  + "Ref ID: " + randomRef + "  Time: " + localtime
        data = data  + arrdata("Item", "Quantity", "Price")
        data = data  + arrdata("Meals", No_of_Meals,Cost_of_Meals)
        data = data  + arrdata("Porotta", No_of_Porotta,Cost_of_Porotta)
        data = data  + arrdata("Chappati", No_of_Chappati,Cost_of_Chappati)
        data = data  + arrdata("Kubbus", No_of_Kubbus,Cost_of_Kubbus)
        data = data  + arrdata("Chicken65", No_of_Chicken65,Cost_of_Chicken65)
        data = data  + arrdata("BeefFry", No_of_BeefFry, Cost_of_BeefFry)
        data = data  + arrdata("ChickenFriedRice", No_of_ChickenFriedRice, Cost_of_ChickenFriedRice)
        data = data  + arrdata("VegCurry", No_of_VegCurry, Cost_of_VegCurry)
        data = data  + arrdata("EggFriedRice", No_of_EggFriedRice, Cost_of_EggFriedRice)
        data = data  + "\n" + arrdata("", "Total",Subtotal + Tax)


# ==================Function for Reset=============
def Resett():
    global data
    data = ""
    rand.set("")
    Meals.set("")
    Porotta.set("")
    Chappati.set("")
    Kubbus.set("")
    Chicken65.set("")
    BeefFry.set("")
    ChickenFriedRice.set("")
    VegCurry.set("")
    EggFriedRice.set("")
    GST.set("")
    Total.set("")

# ==============Function for Reset price==================
def writetopricefile(index,value):
    file = open(price_list,"r")
    plist = file.readlines()
    plist[index] = str(value)

    content = open(price_list,"w")
    file.writelines(plist)
    file.close()
    return

def Reset_price():
    global var_p_Meals
    global var_p_Porotta
    global var_p_Chappati
    global var_p_Kubbus
    global var_p_Chicken65
    global var_p_BeefFry
    global var_p_VegCurry
    global var_p_ChickenFriedRice
    global var_p_EggFriedRice
    global var_GST
    global Prices

    p_change = Tk()
    p_change.geometry("600x700")
    p_change.title("Price change window")

    a = StringVar(p_change, str(var_p_Meals.get()))
    b = StringVar(p_change, str(var_p_Porotta.get()))
    c = StringVar(p_change, str(var_p_Chappati.get()))
    d = StringVar(p_change, str(var_p_Kubbus.get()))
    e = StringVar(p_change, str(var_p_Chicken65.get()))
    f = StringVar(p_change, str(var_p_BeefFry.get()))
    g = StringVar(p_change, str(var_p_VegCurry.get()))
    h = StringVar(p_change, str(var_p_ChickenFriedRice.get()))
    i = StringVar(p_change, str(var_p_EggFriedRice.get()))
    j = StringVar(p_change, str(var_GST.get()))

    p_ftframes = Frame(p_change, width=500, height=150, bg="White", relief=SUNKEN)
    p_ftframes.pack(side=TOP)
    title = Label(p_ftframes, font=('arial', 50, 'bold'), text="Price change", fg="Red", bd=10, anchor='w')
    title.grid(row=0, column=0)
    p_Rframe = Frame(p_change, width=800, height=800, relief=SUNKEN)
    p_Rframe.pack(side=LEFT)

    lbl_p_price = Label(p_Rframe, font=('arial', 16, 'bold'), text="Price(Rs.)", fg="Black", bd=10)
    lbl_p_price.grid(row=0, column=1)

    price_of_Meals = DoubleVar()
    lblMeals = Label(p_Rframe, font=('arial', 16, 'bold'), text="Meals", fg="MediumOrchid4", bd=10)
    lblMeals.grid(row=1, column=0)
    txtMeals = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=a, bd=4, width=10, bg="powder blue",
                           justify='right')
    txtMeals.grid(row=1, column=1)

    lblPorotta = Label(p_Rframe, font=('arial', 16, 'bold'), text="Porotta", fg="MediumOrchid4", bd=10)
    lblPorotta.grid(row=2, column=0)
    txtPorotta = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=b, bd=4, width=10, bg="powder blue",
                       justify='right')
    txtPorotta.grid(row=2, column=1)

    lblChappati = Label(p_Rframe, font=('arial', 16, 'bold'), text="Chappati", fg="MediumOrchid4", bd=10)
    lblChappati.grid(row=3, column=0)
    txtChappati = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=c, bd=4, width=10, bg="powder blue",
                        justify='right')
    txtChappati.grid(row=3, column=1)

    lblKubbus = Label(p_Rframe, font=('arial', 16, 'bold'), text="Kubbus", fg="MediumOrchid4", bd=10)
    lblKubbus.grid(row=4, column=0)
    txtKubbus = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=d, bd=4, width=10, bg="powder blue",
                      justify='right')
    txtKubbus.grid(row=4, column=1)

    lblChicken65 = Label(p_Rframe, font=('arial', 16, 'bold'), text="Chicken65", fg="MediumOrchid4", bd=10)
    lblChicken65.grid(row=5, column=0)
    txtChicken65 = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=e, bd=4, width=10, bg="powder blue",
                         justify='right')
    txtChicken65.grid(row=5, column=1)

    lblBeefFry = Label(p_Rframe, font=('arial', 16, 'bold'), text="Beef Fry", fg="MediumOrchid4", bd=10)
    lblBeefFry.grid(row=6, column=0)
    txtBeefFry = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=f, bd=4, width=10, bg="powder blue",
                       justify='right')
    txtBeefFry.grid(row=6, column=1)

    lblVegCurry = Label(p_Rframe, font=('arial', 16, 'bold'), text="Veg Curry", fg="MediumOrchid4", bd=10)
    lblVegCurry.grid(row=7, column=0)
    txtVegCurry = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=g, bd=4, width=10, bg="powder blue",
                        justify='right')
    txtVegCurry.grid(row=7, column=1)

    lblChickenFriedRice = Label(p_Rframe, font=('arial', 16, 'bold'), text="Chicken FriedRice", fg="MediumOrchid4",
                                bd=10, )
    lblChickenFriedRice.grid(row=8, column=0)
    txtChickenFriedRice = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=h, bd=4, width=10,
                                bg="powder blue", justify='right')
    txtChickenFriedRice.grid(row=8, column=1)

    lblEggFriedRice = Label(p_Rframe, font=('arial', 16, 'bold'), text="EggFriedRice", fg="MediumOrchid4", bd=10)
    lblEggFriedRice.grid(row=9, column=0)
    txtEggFriedRice = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=i, bd=4, width=10,
                            bg="powder blue", justify='right')
    txtEggFriedRice.grid(row=9, column=1)

    lblGST = Label(p_Rframe, font=('arial', 16, 'bold'), text="GST", fg="MediumOrchid4", bd=10)
    lblGST.grid(row=1, column=3)
    txtGST = Entry(p_Rframe, font=('arial', 16, 'bold'), textvariable=j, bd=10, width=10, bg="powder blue",
                   justify='right')
    txtGST.grid(row=1, column=4)


    def editprice():
        global Prices

        new = [txtMeals.get(), txtPorotta.get(), txtChappati.get(), txtKubbus.get(), txtChicken65.get(),
               txtBeefFry.get(),
               txtVegCurry.get(), txtChickenFriedRice.get(), txtEggFriedRice.get(), txtGST.get()]

        Prices = new
        plist = Prices
        file = open(price_list, "w")
        l = ""
        for i in plist:
            l = l + i + "\n"
        file.write(l)
        file.close()
        loadprices()

        return

    Resetp = Button(p_Rframe, padx=16, bd=8, fg="black", font=('arial', 16, 'bold'), text="Set price", width=6,
                         command=editprice).grid(row = 9,column =4)


# =========Calculator=============================

operator = ""
text_input = StringVar()

# ===================Entry and Buttons==============
txtDsiplay = Entry(Lframe, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue",
                   justify='right').grid(columnspan=4)
btn7 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7",
              command=lambda: btnclick(7)).grid(row=1, column=0)
btn8 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8",
              command=lambda: btnclick(8)).grid(row=1, column=1)
btn9 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9",
              command=lambda: btnclick(9)).grid(row=1, column=2)
btn4 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4",
              command=lambda: btnclick(4)).grid(row=2, column=0)
btn5 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5",
              command=lambda: btnclick(5)).grid(row=2, column=1)
btn6 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6",
              command=lambda: btnclick(6)).grid(row=2, column=2)
btn1 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1",
              command=lambda: btnclick(1)).grid(row=3, column=0)
btn2 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2",
              command=lambda: btnclick(2)).grid(row=3, column=1)
btn3 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3",
              command=lambda: btnclick(3)).grid(row=3, column=2)
btn0 = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0",
              command=lambda: btnclick(0)).grid(row=4, column=0)
addition = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+",
                  command=lambda: btnclick("+")).grid(row=2, column=3)
subtraction = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-",
                     command=lambda: btnclick("-")).grid(row=1, column=3)
multiplication = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*",
                        command=lambda: btnclick("*")).grid(row=3, column=3)
division = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/",
                  command=lambda: btnclick("/")).grid(row=4, column=3)
point = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=".",
               command=lambda: btnclick(".")).grid(row=4, column=1)
equals = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=",
                command=lambda: btnequalsinput()).grid(row=4, column=2)
Clear = Button(Lframe, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C",
               command=lambda: btncleardisplay()).grid(row=5, column=0)

# ======================Management System================================================

# ======================Variables========================================================
rand = StringVar()
Meals = StringVar()
Porotta = StringVar()
Chappati = StringVar()
Kubbus = StringVar()
Chicken65 = StringVar()
BeefFry = StringVar()
ChickenFriedRice = StringVar()
VegCurry = StringVar()
EggFriedRice = StringVar()
GST = StringVar()
Total = StringVar()

var_p_Meals=DoubleVar()
var_p_Porotta=DoubleVar()
var_p_Chappati=DoubleVar()
var_p_Kubbus=DoubleVar()
var_p_Chicken65=DoubleVar()
var_p_BeefFry=DoubleVar()
var_p_VegCurry=DoubleVar()
var_p_ChickenFriedRice=DoubleVar()
var_p_EggFriedRice=DoubleVar()
var_GST=DoubleVar()
price_of_Meals = float()
price_of_Porotta = float()
price_of_Chappati = float()
price_of_Kubbus = float()
price_of_Chicken65 = float()
price_of_BeefFry = float()
price_of_VegCurry = float()
price_of_ChickenFriedRice = float()
price_of_EggFriedRice = float()
decimal_of_GST = float()


def loadprices():
    global var_p_Meals
    global var_p_Porotta
    global var_p_Chappati
    global var_p_Kubbus
    global var_p_Chicken65
    global var_p_BeefFry
    global var_p_VegCurry
    global var_p_ChickenFriedRice
    global var_p_EggFriedRice
    global var_GST

    global price_of_Meals
    global price_of_Porotta
    global price_of_Chappati
    global price_of_Kubbus
    global price_of_Chicken65
    global price_of_BeefFry
    global price_of_VegCurry
    global price_of_ChickenFriedRice
    global price_of_EggFriedRice
    global decimal_of_GST

    price_file = open(price_list,"r")
    Prices = price_file.readlines()

    price_of_Meals= float(Prices[0])
    price_of_Porotta= float(Prices[1])
    price_of_Chappati= float(Prices[2])
    price_of_Kubbus= float(Prices[3])
    price_of_Chicken65= float(Prices[4])
    price_of_BeefFry= float(Prices[5])
    price_of_VegCurry= float(Prices[6])
    price_of_ChickenFriedRice= float(Prices[7])
    price_of_EggFriedRice= float(Prices[8])
    decimal_of_GST=float(Prices[9])
    price_file.close()

    var_p_Meals.set(price_of_Meals)
    var_p_Porotta.set(price_of_Porotta)
    var_p_Chappati.set(price_of_Chappati)
    var_p_Kubbus.set(price_of_Kubbus)
    var_p_Chicken65.set(price_of_Chicken65)
    var_p_BeefFry.set(price_of_BeefFry)
    var_p_VegCurry.set(price_of_VegCurry)
    var_p_ChickenFriedRice.set(price_of_ChickenFriedRice)
    var_p_EggFriedRice.set(price_of_EggFriedRice)
    var_GST.set(decimal_of_GST)

loadprices()
# ==================Label and Entries====================================================


lblreference = Label(Rframe, font=('arial', 16, 'bold'), text="REFERENCE ID", fg="MediumOrchid4", bd=10)
lblreference.grid(row=1, column=0)
txtreference = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=rand, bd=4, width = 10, bg="powder blue",
                     justify='right')
txtreference.grid(row=1, column=1)

lblprice = Label(Rframe, font=('arial', 16, 'bold'), text="Price(Rs.)", fg="Black", bd=10)
lblprice.grid(row=1, column=2)

lblMeals = Label(Rframe, font=('arial', 16, 'bold'), text="Meals", fg="MediumOrchid4", bd=10)
lblMeals.grid(row=2, column=0)
txtMeals = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=Meals, bd=4, width = 10, bg="powder blue",
                 justify='right')
txtMeals.grid(row=2, column=1)
lblprice_meal=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_Meals, fg="Black", bd=10)
lblprice_meal.grid(row=2, column=2)

lblPorotta = Label(Rframe, font=('arial', 16, 'bold'), text="Porotta", fg="MediumOrchid4", bd=10)
lblPorotta.grid(row=3, column=0)
txtPorotta = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=Porotta, bd=4, width = 10, bg="powder blue",
                   justify='right')
txtPorotta.grid(row=3, column=1)
lblprice_Porotta=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_Porotta, fg="Black", bd=10)
lblprice_Porotta.grid(row=3, column=2)

lblChappati = Label(Rframe, font=('arial', 16, 'bold'), text="Chappati", fg="MediumOrchid4", bd=10)
lblChappati.grid(row=4, column=0)
txtChappati = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=Chappati, bd=4, width = 10, bg="powder blue",
                    justify='right')
txtChappati.grid(row=4, column=1)
lblprice_Chappati=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_Chappati, fg="Black", bd=10)
lblprice_Chappati.grid(row=4, column=2)

lblKubbus = Label(Rframe, font=('arial', 16, 'bold'), text="Kubbus", fg="MediumOrchid4", bd=10)
lblKubbus.grid(row=5, column=0)
txtKubbus = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=Kubbus, bd=4, width = 10, bg="powder blue",
                  justify='right')
txtKubbus.grid(row=5, column=1)
lblprice_Kubbus=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_Kubbus, fg="Black", bd=10)
lblprice_Kubbus.grid(row=5, column=2)

lblChicken65 = Label(Rframe, font=('arial', 16, 'bold'), text="Chicken65", fg="MediumOrchid4", bd=10)
lblChicken65.grid(row=6, column=0)
txtChicken65 = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=Chicken65, bd=4, width = 10, bg="powder blue",
                     justify='right')
txtChicken65.grid(row=6, column=1)
lblprice_Chicken65=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_Chicken65, fg="Black", bd=10)
lblprice_Chicken65.grid(row=6, column=2)

lblBeefFry = Label(Rframe, font=('arial', 16, 'bold'), text="Beef Fry", fg="MediumOrchid4", bd=10)
lblBeefFry.grid(row=7, column=0)
txtBeefFry = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=BeefFry, bd=4, width = 10, bg="powder blue",
                   justify='right')
txtBeefFry.grid(row=7, column=1)
lblprice_BeefFry=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_BeefFry, fg="Black", bd=10)
lblprice_BeefFry.grid(row=7, column=2)

lblVegCurry = Label(Rframe, font=('arial', 16, 'bold'), text="Veg Curry", fg="MediumOrchid4", bd=10)
lblVegCurry.grid(row=8, column=0)
txtVegCurry = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=VegCurry, bd=4, width = 10, bg="powder blue",
                    justify='right')
txtVegCurry.grid(row=8, column=1)
lblprice_VegCurry=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_VegCurry, fg="Black", bd=10)
lblprice_VegCurry.grid(row=8, column=2)

lblChickenFriedRice = Label(Rframe, font=('arial', 16, 'bold'), text="Chicken FriedRice", fg="MediumOrchid4", bd=10,)
lblChickenFriedRice.grid(row=9, column=0)
txtChickenFriedRice = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=ChickenFriedRice, bd=4, width = 10,
                            bg="powder blue", justify='right')
txtChickenFriedRice.grid(row=9, column=1)
lblprice_ChickenFriedRice=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_ChickenFriedRice, fg="Black", bd=10)
lblprice_ChickenFriedRice.grid(row=9, column=2)

lblEggFriedRice = Label(Rframe, font=('arial', 16, 'bold'), text="EggFriedRice", fg="MediumOrchid4", bd=10)
lblEggFriedRice.grid(row=10, column=0)
txtEggFriedRice = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=EggFriedRice, bd=4, width = 10,
                        bg="powder blue", justify='right')
txtEggFriedRice.grid(row=10, column=1)
lblprice_EggFriedRice=Label(Rframe, font=('arial', 16, 'bold'), textvariable=var_p_EggFriedRice, fg="Black", bd=10)
lblprice_EggFriedRice.grid(row=10, column=2)

lblGST = Label(Rframe, font=('arial', 16, 'bold'), text="GST", fg="MediumOrchid4", bd=10)
lblGST.grid(row=4, column=4)
txtGST = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=GST, bd=10, width = 10, bg="powder blue",
               justify='right')
txtGST.grid(row=4, column=5)

lblTotal = Label(Rframe, font=('arial', 16, 'bold'), text="Total", fg="MediumOrchid4", bd=10)
lblTotal.grid(row=5, column=4)
txtTotal = Entry(Rframe, font=('arial', 16, 'bold'), textvariable=Total, bd=10, width = 10, bg="light green",
                 justify='right')
txtTotal.grid(row=5, column=5)

# ==============================Buttons=========================================================================

btnTotal = Button(Rframe, padx=16, bd=8, fg="black", font=('arial', 16, 'bold'), text="Total", width = 6,command=Ref).grid(row=5,
                                                                                                                 column=4)

btnReset = Button(Rframe, padx=16, bd=8, fg="black", font=('arial', 16, 'bold'), text="Reset", width = 6,command=Resett).grid(
    row=1, column=4)

btnSavetolog = Button(Rframe, padx=16, bd=8, fg="black", font=('arial', 14, 'bold'), text="Save to\naccount", command=writetolog).grid(row=6,
                                                                                                                 column=5)

btnSeeLog = Button(Rframe, padx=16, bd=8, fg="black", font=('arial', 10, 'bold'), text="View Account\nlogs", command=viewlog).grid(row=8,
                                                                                                                 column=4)

btnReset_price = Button(Rframe, padx=16, bd=8, fg="black", font=('arial', 16, 'bold'), text="Reset price", width = 6,command=Reset_price).grid(
    row=8, column=5)
# looping begins here

mini.mainloop()
