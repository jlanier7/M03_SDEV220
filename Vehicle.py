"""
------------------------------------------------------------------------------------------------------------------------------------

 Program Name: Vehicle

 GitHub Filepath: jlanier7/M03_SDEV220/Vehicle.py

 Author: Josh Lanier 

 SDEV 220

 11/5/22

 Program Purpose: To hold the classes Vehicle and Automobile for use by other programs. Class Vehicle holds an attribute for vehicle type.
    Class Automobile is a child class of Vehicle, and containts attribues for year, make, model, doors (2 or 4), and roof.
    
1. Constants and variables:     
INITIALIZED:  
    - 
IN-LINE:
    - messDL:       (string)         message printed if student qualifies for the Dean's List, using f-string insertion of nameLast and nameFirst as it was at the time of messDL last variable 
                                     assignment
    - messHR:       (string)         message printed if student qualifies for the Honor Roll, using f-string insertion of nameLast and nameFirst as it was at the time of messHR last variable 
                                     assignment
    - messNeither:  (string)         message printed if student does not qualify for either Dean's List or Honor Roll, using f-string insertion of nameLast and nameFirst as it was at the time 
                                     of messNeither last variable assignment  
  
2. Inputs

- student's last name  (string)
- student's first name (string)
- student's GPA        (float)

3. Computations (pseudocode)

    initialize variables and constants

    initial priming user input for nameLast

    while nameLast does not equal escape variable ('ZZZ' or 'zzz')

        user input for nameFirst
        user input for gpa

        if gpa is less than or equal to Dean's List GPA minimum
            action flag is assigned Dean's List flag
        else if gpa is less than or equal to Honor Roll GPA minimum
            action flag is assigned Honor Roll flag
        (no if statement for if GPA is less than both minimums, because flag is already set for this scenario. if it is less, it will pass right through both of these, and the first two 'if' 
          evaluations of the next decision structure, and be found True for the 'else' evaluation of that decision strucure)

        message variable declared for what will be printed if student meets Dean's List qualifications
        message variable declared for what will be printed if student meets Honor Roll qualifications
        message variable declared for what will be printed if student does not meet either qualifications

        if action flag is assigned to Dean's List flag
            output the Dean's List message variable
        else if action flag is assigned to Honor Role flag
            output the Honor Roll message variable
        else (only option left is they didn't qualify for either)
            output the 'didn't meet either qualification' message variable

        reset the action flag to the empty string (so it will pass through the first decision structure and trigger an evaluation in the second that the student does not qualify for either 
        Dean's List or Honor Roll unless explicitly changed by the structure)

        user input of nameLast to be evaluated at the beginning of the next iteration of the 'while' loop

    output message thanking user for using the program

4. Outputs   

- inital welcome statement at beginning of program
- message stating whether a student qualifies for either honor, or doesn't meet either of them
- message thanking user for using the program

------------------------------------------------------------------------------------------------------------------------------------
"""

# initializing variables and constants

class Vehicle():
    '''
    Class that holds and applies methods to an object describing a vehicle type, with attribue 'vehType'.
    '''
    def __init__(self, vehType):
        'Instantiates a Vehicle class object'
        self.vehType = vehType



class Automobile(Vehicle):
    '''
    Class that holds and applies methods to an object describing an automobile, with attributes 'vehType', \
        'year', 'make', 'model', 'doors' [with default value of 2], roof [with default value of 'solid']
    '''
    def __init__(self, vehType, year, make, model, doors=2, roof='solid'):
        'Instantiates an Automobile class object'
        super().__init__(vehType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def dataPrint(self):
        'Pretty prints the attributes of the Automobile object'
        print('Vehicle type:', self.vehType)
        print('Year:', self.year)
        print('Make:', self.make)
        print('Model:', self.model)
        print('Number of doors:', self.doors)
        print('Type of roof:', self.roof, '\n')
