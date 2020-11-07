#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Conversions import Conversions
x=Conversions(12,2,3,4,5,66,6,7)

option=0
while option!=5:
    print("What would like to convert?: ")
    print("1-Length")
    print("2-Mass")
    print("3-Temperature")
    print("4-Time")
    print("5-Quit")
    option=int(input("Select from options 1-5: "))
    print()
    
    #Option 1
    if option==1:
        option2=0
        while option2!=2:
            print("Choose from the following options: ")
            print("1 - Feet to meters")
            print("2 - Inches to meters")
            option2= int(input("Select from options 1-2: "))
            print()
            
            if option2==1:
                #feet to  meters coversion
                feet=int(input("Enter a value in feets: "))
                if feet>0:
                    print(f"The value in meters is: ", x.feetToMeters(feet))
                    print()
                else:
                    print("Invalid value.It must be greater than zero")
                    
            elif option2==2:
                #inches to meters
                inches=int(input("Enter a value in inches: "))
                if inches>0:
                    print("The value in meters is: ", x.inchesToMeters(inches))
                    print()
                else:
                    print("Invalid value.It must be greater than zero")
            
            else:
                print("Invalid selection.Select from option 1-2")
                
    
    #Option 2
    elif option==2:
        option2=0
        while option2!=2:
            print("Choose from the following options: ")
            print("1- Pounds to kilograms")
            print("2- Kilograms to pounds")
            option2= int(input("Select from options 1-2: "))
         
            if option2==1:
                #Pounds to kilograms
                pounds=int(input("Give a value in pounds: "))
                if pounds>0:
                    print("The value in kilograms is: ", x.poundsToKilograms(pounds))
                    print()
                else:
                    print("Invalid value.It must be greater than zero")
        
            elif option2==2:
                #Kilograms to pounds
                kilograms=int(input("Give a value in kilograms: "))
                if kilograms>0:
                    print("The value in pounds is: ", x.kilogramsToPounds(kilograms))
                    print()
                else:
                    print("Invalid value.It must be greater than zero")    
        
            else:
                print("Invalid selection.Select from option 1-2")
    
    #Option 3
    elif option==3:
        option2=0
        while option2!=2:
            print("Choose from the following options: ")
            print("1- Kelvin to celcius")
            print("2- Celcius to Kelvin")
            option2= int(input("Select from options 1-2: "))
         
            if option2==1:
                #Kelvin to Celcius
                kelvin=int(input("Give a temperature in kelvin: "))
                if kelvin>-273:
                    print("The value in celcius is: ", x.kelvinToCelcius(kelvin))
                    print()
                else:
                    print("Invalid value.It must be greater than -273")
        
            elif option2==2:
                #Celcius to kelvin
                celcius=int(input("Give a temperature in Celcius: "))
                if celcius>0:
                    print("The temperature in kelvin is: ", x.celciusToKelvin(celcius))
                    print()
                else:
                    print("Invalid value.It must be greater than 0" )   
        
            else:
                print("Invalid selection.Select from option 1-2")                
    
    #Option 4
    elif option==4:
        option2=0
        while option2!=2:
            print("Choose from the following options: ")
            print("1- Hours to seconds")
            print("2- Minutes to seconds")
            option2= int(input("Select from options 1-2: "))
         
            if option2==1:
                #Hours to seconds
                hours=int(input("Give time in hours: "))
                if hours>0:
                    print("The time in seconds is: ", x.hoursToSeconds(hours))
                    print()
                else:
                    print("Invalid value.It must be greater than 0")
        
            elif option2==2:
                #Minutes to seconds
                minutes=int(input("Give time in minutes: "))
                if minutes>0:
                    print("The time in seconds is: ", x.minutesToSeconds(minutes))
                    print()
                else:
                    print("Invalid value.It must be greater than 0" )   
        
            else:
                print("Invalid selection.Select from option 1-2")  

    elif option==5:
        print("Quit")
        break
      


# In[ ]:





# In[ ]:





# In[ ]:




