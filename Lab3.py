# -*- coding: utf-8 -*-
"""
Timothy Queva
CS3010 Lab3
Feb. 5, 2021

This program will calculate the future value of an investment at a given
interest rate for a specified number of years. We are using the API tool
tkinter to present a basic GUI to the user.
"""

from tkinter import *

class interest:
    def __init__(self,invest,years,rate):
        self.invest = invest
        self.years = years
        self.rate = rate
    
    def calculate(self):
        return (self.invest * (1+self.rate)**(self.years*12))

class window:
    __return__ = float(0)
    
    
    def __init__(self):
        window = Tk()
        window.title("Investments Returns Calculator")
        
        #Investment amount frame
        invest_frame = Frame(window)
        invest_frame.pack()
        invest_label = Label(invest_frame,text = "Investment Amount:",anchor="w",width = 16)
        self.invest_amnt = DoubleVar()
        invest_field = Entry(invest_frame, textvariable = self.invest_amnt,justify=RIGHT)
        invest_label.grid(row = 1, column = 1)
        invest_field.grid(row = 1, column = 2)
        
        #captures number of years for investment
        years_frame = Frame(window)
        years_frame.pack()
        years_label = Label(years_frame,text = "Number of years:",anchor="w",width = 16)
        self.nyears = DoubleVar()
        years_field = Entry(years_frame, textvariable = self.nyears,justify=RIGHT)
        years_label.grid(row = 1, column = 1)
        years_field.grid(row = 1, column = 2)
        
        #Interest rate
        irate_frame = Frame(window)
        irate_frame.pack()
        irate_label = Label(irate_frame,text = "Interest Rate:",anchor="w",width=16)
        self.irate = DoubleVar()
        irate_field = Entry(irate_frame, textvariable = self.irate,justify=RIGHT)
        irate_label.grid(row = 1, column = 1)
        irate_field.grid(row = 1, column = 2)
        
        
        #Potential Returns
        returns_frame = Frame(window)
        returns_frame.pack()
        returns_label = Label(returns_frame,text = "Potential returns:",
                              anchor="w",width=18)
        self.amnt = DoubleVar()
        amnt_label = Label(returns_frame,textvariable = self.amnt,anchor="e",
                           width=15)
        returns_label.grid(row = 1, column = 1)
        amnt_label.grid(row=1,column = 2)
        
        #calculate button
        calc_frame = Frame(window)
        calc_frame.pack(side=RIGHT)
        calc_button = Button(calc_frame, text = "Calculate",
                             command = self.calculate)
        calc_button.grid(row = 6, column = 3)
        
        window.mainloop()
    
    def calculate(self):
        obj = interest(self.invest_amnt.get(),self.nyears.get(),
                       self.irate.get())
        __return__ = obj.calculate()
        __return__ = int(__return__*100)/100
        self.amnt.set(__return__)

#"Main" starts here
window()

'''
futureValue = investAmount *(1+monthlyInterestRate)**(years*12)

Investment Amount
years
Annual Interest Rate

Future Value (output)
calculate (button)

'''