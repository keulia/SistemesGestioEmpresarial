'''
Design the class "School" for a program a that allows the complete management of several schools. For each school, the "School" class that we define now will be instantiated:

-Class School: it will contain the information of the schools (name, location, person in charge ...) as well as the different teachers and the different groups of students, using the following proposed classes. It must have methods to add / remove students, teachers. In an auxiliary way in the "School" class, the following classes have to be created:

-Teacher Class: it will contain information about the teachers who work there (name, type (science, letters or mixed)).

-Class Student: it will contain the information of the students of the school (name, course, responsible teacher (only one teacher)).

There is not one student who goes to two different schools, nor two teachers who work in different schools. Therefore you choose the most suitable object structure for its correct storage. The classes must be declared in a separate file from the program. What's more:
-The relationships between classes have to be represented.
-They must have methods to correctly manage all the elements, with their corresponding operations (insertion, modification, deletion, visualization, etc.).
Finally, make an example code that allows you to test the capabilities of your design.
'''


class School:
        def __init__(self, name, location, personInCharge):
                self.name = name
                self.location = location
                self.personInCharge = personInCharge
    
    