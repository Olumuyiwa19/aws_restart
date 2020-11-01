#This code estimate the 
Yes = True
while Yes:

    Grain_Type = str(input("Enter the type of your grain: "))
    Wg = float(input("What is the weight of your grain? "))
    MC_Wg = int(input("what is the moisture content of your wet grain? "))
    MC_Dg = int(input("what is your desired final moisture content for the grain? "))
    #Determine the standard measuring system in Bushel
    Initial_Bu = Wg / 56
    print(f"The weight of your grain in Bushel is: {Initial_Bu:1.2f}")

    MC_Shrinkage_Dict = {16.0:1.190, 15.5:1.183, 15.0:1.176, 14.5:1.170, 14.0:1.163, 13.5:1.156, 13.0:1.149, 12.5:1.143, 12.0:1.136}

    #Determine mositure points which is same as moisture difference
    moisture_pt = MC_Wg - MC_Dg

    #Determine the percentage shrinkage and amount of shrinkage
    shrinkage_percent = moisture_pt * MC_Shrinkage_Dict[13.0]
    print(str(shrinkage_percent) + "%")
    shrinkage_decimal = shrinkage_percent / 100

    #Determine the amount of shrinkages in the grain after drying
    shrinkage_Amt = Initial_Bu * shrinkage_decimal
    print("The amount of shrinkages in Bushel is: " + str(f"{shrinkage_Amt: 1.2f}"))

    #Determine the final weight of grain after drying 
    Final_Bu = Initial_Bu - shrinkage_Amt
    print("The weight of your grain in Bushel after drying to 13% moisture content is: " + str(f"{Final_Bu: 1.2f}"))

    #Determine the final price of grain at $3.50/Bushel
    Final_Price = Final_Bu * 3.5
    print("The price for your grain is: " + "$" + str(f"{Final_Price:1.2f}"))
Yes = input("Do you want to carryout another grain moisture estimate? yes or no: ").lower()
if Yes != "yes":
    print("Goodbye for now")
    quit
