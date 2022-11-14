"""
------------------------------------------------------------------------------------------------------------------------------------

 Program Name: M03 Lab - Car Profiler

 GitHub Filepath: jlanier7/M02_SDEV220/M03_Lab.py

 Author: Josh Lanier 

 SDEV 220

 11/13/22

 Program Purpose: 
  
1. Constants and variables:     
INITIALIZED:  
    - vehTypeAcceptable (tuple)     tuple with the acceptable value for vehType variable assignment input
    - doorsAcceptable   (tuple)     tuple with the acceptable values for doors variable assignment input
    - roofAcceptable    (tuple)     tuple with the acceptable values for roof variable assignment input
IN-LINE:
    - vehType           (string)    variable that holds input value for type of vehicle, to eventually pass to Car() as argument
    - year              (string)    variable that holds input value for year of vehicle, to eventually pass to Car() as argument
    - make              (string)    variable that holds input value for make of vehicle, to eventually pass to Car() as argument
    - model             (string)    variable that holds input value for model of vehicle, to eventually pass to Car() as argument    
    - doors             (string)    variable that holds input value for number of doors on the vehicle, to eventually pass to Car() as argument
    - roof              (string)    variable that holds input value for type of roof on vehicle, to eventually pass to Car() as argument
    - auto              (object)    object of class Car, created by variables gathering input in the while loop, that pass as attribute arguments at the end of the while 
                                    loop in the program
  
2. Inputs

- vehicle type          (string)
- vehicle year          (string)
- vehicle make          (string)
- vehicle model         (string)
- veh. number of doors  (string)
- vehicle roof type     (string)

3. Computations (pseudocode)

not included for this assignment

4. Outputs   

not included for this assignment

------------------------------------------------------------------------------------------------------------------------------------
"""
# importing libraries

from Vehicle import *

# no variables to initialize

vehTypeAcceptable = ('car',)
doorsAcceptable = ('2', '4')
roofAcceptable = ('solid', 'sunroof')

print('Welcome to the Car Profiler!')
print('Please enter the type of vehicle you want to profile, which is a car in this case, or "quit" to quit:')

while True:
    
    vehType = input()
    if vehType == 'quit':
        break

    while True:
        if vehType not in vehTypeAcceptable:
            print('Vehicle type must be "car" for this example. Please input "car", we can do other types at another time.')
            vehType = input('Enter the type of vehicle you want to profile, please ("car"), or "quit" to quit: ')
            continue            
        else:
            break

    year = input('Enter the year of the car: ')
    make = input('Enter the make of the car: ')
    model = input('Enter the model of the car: ')

    while True:
        doors = input('Enter the number of doors of the car (2 or 4): ')
        if doors in doorsAcceptable:
            break
        else:
            print('Vehicle must have 2 or 4 doors here, we can make 1 or 3 door cars in another program.')
            continue

    while True:
        roof = input('Enter the type of roof on the car ("solid" or "sunroof"): ')
        if roof in roofAcceptable:
            break
        else:
            print('Vehicle must be "solid" or "sunroof" in this program, thank you for your cooperation.')
            continue

    auto = Automobile(vehType, year, make, model, doors, roof)

    print('Thank you for profiling a car with us today. Here is the car profile you just created:\n \n---------------------\n ')
    auto.dataPrint()

    print("--------------------- \n \n If you'd like to profile another car, please enter the type of vehicle you want to profile (which is still 'car'), or 'quit' if you're done:")
    

print('We hope you enjoyed using our Car Profiler. Come again!')

