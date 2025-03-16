# Course-Catalog
In this lab, you will utilize a Binary Search Tree to store and organize courses.

A course is uniquely identified by its department code and course ID (e.g., CMPSC 9 has the department code "CMPSC" and the course ID 9). In addition to these two attributes, a course also has a course name, a lecture, and several sections.

You will store the details of each course in a binary search tree node defined by class CourseCatalogNode and organize all the courses in a binary search tree defined by class CourseCatalog. The nodes will be ordered first by department code in lexicographical order, and then by course ID in numerical order.

You will also write a test file to verify your implementation. Note: While this lab writeup provides sample test cases for reference, the Gradescope autograder will use different, more complex test cases.

Note: It is important that you start this lab early so you can utilize our office hours to seek assistance / ask clarifying questions during the weekdays before the deadline if needed!

Instructions
You will need to create four files:

Event.py
CourseCatalogNode.py
CourseCatalog.py
testFile.py
Event.py
The Event.py file will contain the definition of the Event class, which is used to represent the lecture and the section. The Event class is structured as follows:

Attributes:

day - a string representing the event days. It is a combination of "M", "T", "W", "R", "F" (e.g., "MW", "TR", "F")
time - a tuple of two integers representing the event’s start and end times, using a 24-hour format. For example, (1530, 1645) indicates an event starts at 15:30 (3:30 PM) and ends at 16:45 (4:45 PM)
location - a string representing the event’s location. Note, this attribute is stored in uppercase
Methods:

__init__(self, day, time, location) - initializes an Event object with the specified day, time, and location
__eq__(self, rhs) - compares two events for equality. Two events are considered identical if they have the same day, time, and location
__str__(self) - returns a string representation of the event in the format: "[day] [time], [location]"
Example:

e1 = Event("TR", (1530, 1645), "td-w 1701")
e2 = Event("TR", (1530, 1645), "td-w 1702")
print(e1 == e2)
print(e1)
Output:

False
TR 15:30 - 16:45, TD-W 1701
🔧 The following is a helper function you can use to convert the time attribute, a (int, int) tuple, to a readable string.

def format(time):
    return f"{time[0]//100:0>2}:{time[0]%100:0>2} - {time[1]//100:0>2}:{time[1]%100:0>2}"

assert format((800, 1550)) == "08:00 - 15:50"
CourseCatalogNode.py
The CourseCatalogNode.py file will contain the definition of the CourseCatalogNode class, which is used to represent a course in a Binary Search Tree. Each node’s key is determined by a course’s department code and course ID. The nodes are ordered first by department code in lexicographical order, followed by course ID in numerical order. The CourseCatalogNode class is structured as follows:

Attributes:

department - a string representing the department code of the course, which serves as the first key of the node. You need to store this attribute in uppercase
courseId - an integer representing the course ID, which serves as the second key of the node
courseName - a string representing the name of the course. You need to store this attribute in uppercase
lecture - an Event object that stores the lecture’s day, time, and location
sections - a list of Event objects, where each element stores a section’s day, time, and location
parent - the reference to a parent node. This attribute is None if it has no parent (it is the root)
left - the reference to a left child node. This attribute is None if it has no left child
right - the reference to a right child node. This attribute is None if it has no right child
Methods:

__init__(self, department, courseId, courseName, lecture, sections) - initializes an CourseCatalogNode object with the specified parameters
__str__(self) - returns a string representation of the course including the lecture and sections (if any). See example format below:
Example:

# create one lecture event
lecture = Event("TR", (1530, 1645), "td-w 1701")

# create four section events
section1 = Event("W", (1400, 1450), "north hall 1109")
section2 = Event("W", (1500, 1550), "north hall 1109")
section3 = Event("W", (1600, 1650), "north hall 1109")
section4 = Event("W", (1700, 1750), "girvetz hall 1112")
sections = [section1, section2, section3, section4]

# initialize a CMPSC 9 course node
node = CourseCatalogNode("cmpsc", 9, "intermediate python", lecture, sections)

print(node)
Output:

CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 15:00 - 15:50, NORTH HALL 1109
 + Section: W 16:00 - 16:50, NORTH HALL 1109
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112

Note that each Event (lecture and sections) will contain a \n character at the end of the line. Also note the single space at the start of each lecture / section line.

CourseCatalog.py
The CourseCatalog.py file will contain the definition of the CourseCatalog class, which is a Binary Search Tree that manages all CourseCatalogNode objects keyed by department and courseId. An example Binary Search Tree structure is illustrated below when the course keys (department and courseId) are inserted in the following order:

CMPSC, 9
CMPSC, 270
CMPSC, 8
PSTAT, 131
example.png

The CourseCatalog class is structured according to the specifications below. Gradescope will test all methods listed below, but your solution can contain (and is recommended to use) additional helper methods that support the functionality.

Attributes:

root - the root of the tree. Note: CourseCatalog should only have 1 attribute root. Any extra attribute may break the test code
Methods:

__init__(self) - initializes an empty binary search tree.
addCourse(self, department, courseId, courseName, lecture, sections) - returns a boolean value. Insert a course into the binary search tree. If a course with the same department and courseId already exists, return False and do nothing. Otherwise, insert a new course node in the Binary Search Tree and return True. Note: The department parameter may not necessarily be in uppercase
addSection(self, department, courseId, section) - returns a boolean value. Insert a section into the Binary Search Tree to the course identified by department and courseId. If the course does not exist, return False and do nothing. Otherwise, append the new section to the end of the corresponding node’s sections list (sections) and return True. Note: The department parameter may not necessarily be in uppercase
inOrder(self) - returns a string containing the information for all courses using an in-order traversal of the Binary Search Tree
preOrder(self) - returns a string containing the information for all courses using a pre-order traversal of the Binary Search Tree
postOrder(self) - returns a string containing the information for all courses using a post-order traversal of the Binary Search Tree
getAttendableSections(self, department, courseId, availableDay, availableTime) - given a course identified by department and courseId, finds all sections of it held on availableDay and within the time period availableTime. Returns a string containing the information of all such sections. An empty string is returned if there are no attendable sections. Note: The department parameter may not necessarily be in uppercase
countCoursesByDepartment(self) - returns a dictionary. Counts the number of courses in each department within the binary search tree. The keys of the dictionary are department codes, and the values are integers representing the count of courses in the corresponding department
Example:

cc = CourseCatalog()

# add a new course: cmpsc 9
lecture = Event("TR", (1530, 1645), "td-w 1701")
section1 = Event("W", (1400, 1450), "north hall 1109")
section2 = Event("W", (1500, 1550), "north hall 1109")
section3 = Event("W", (1600, 1650), "north hall 1109")
section4 = Event("W", (1700, 1750), "girvetz hall 1112")
sections = [section1, section2, section3, section4]
assert True == cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

# add a new section to cmpsc 9
section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
assert True == cc.addSection("cmpsc", 9, section5)

# add a new course: art 10
lecture = Event("TR", (1300, 1550), "arts 2628")
sections = []
assert True == cc.addCourse("art", 10, "introduction to painting", lecture, sections)

print("----- in-order traversal -----")
print(cc.inOrder())

print("----- pre-order traversal -----")
print(cc.preOrder())

print("----- post-order traversal -----")
print(cc.postOrder())

print("Task: find all cmpsc 9 sections held on Wednesday and within 15:00 - 17:00 time period")
print(cc.getAttendableSections("cmpsc", 9, "W", (1500, 1700)))

print("Task: count courses by department")
print(cc.countCoursesByDepartment())
Output:

----- in-order traversal -----
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 15:00 - 15:50, NORTH HALL 1109
 + Section: W 16:00 - 16:50, NORTH HALL 1109
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112
 + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101

----- pre-order traversal -----
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 15:00 - 15:50, NORTH HALL 1109
 + Section: W 16:00 - 16:50, NORTH HALL 1109
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112
 + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628

----- post-order traversal -----
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 15:00 - 15:50, NORTH HALL 1109
 + Section: W 16:00 - 16:50, NORTH HALL 1109
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112
 + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101

Task: find all cmpsc 9 sections held on Wednesday and within 15:00 - 17:00 time period
W 15:00 - 15:50, NORTH HALL 1109
W 16:00 - 16:50, NORTH HALL 1109

Task: count courses by department
{'ART': 1, 'CMPSC': 1}

In this lab, you will build upon your Lab08 code by adding two new methods to the CourseCatalog class: removeSection and removeCourse.

removeSection - removes a section from a course node in the Binary Search Tree
removeCourse - removes a course node from the Binary Search Tree
You will also write a test file to verify your implementation. Note: while this lab writeup provides sample test cases for reference, the Gradescope autograder will use different, more complex test cases.

Note: It is important that you start this lab early so you can utilize our office hours to seek assistance / ask clarifying questions during the weekdays before the deadline if needed!

Instructions
The lab specifications in Lab08 apply to this lab, but this lab will specifically focus on removal functionality (courses and sections) in the Course Catalog Binary Search Tree. Lab08 tests are included in Lab09’s Gradescope tests in case you were unable to finish Lab08 by the deadline and would like to check your Lab08 functionality in this lab.

CourseCatalog.py
The CourseCatalog.py file will contain the definition of the CourseCatalog class, which is a Binary Search Tree that manages all CourseCatalogNode objects keyed by department and courseId. For additional details about the existing requirements, please refer to the Lab08 instructions. Especially, please note: CourseCatalog should only have 1 attribute root. Any extra attribute may break the test code

In addition to the previously created methods, the following new methods are required to be implemented:

Methods:

removeCourse(self, department, courseId) - returns a boolean value. Remove a course node identified by department and courseId from the Binary Search Tree. If the course does not exist, return False and do nothing. Otherwise, remove the course node and return True. Note: The department parameter may not necessarily be in uppercase
removeSection(self, department, courseId, section) - returns a boolean value. Remove a section (containing the same section Event fields) from a course node in the Binary Search Tree. If the course identified by department and courseId does not exist in the Course Catalog, or if the course exists but the section does not exist, return False and do nothing. Otherwise, remove the section from the Course Catalog Node’s sections list (sections) and return True. You can assume there are no duplicate sections in a course node’s sections list. Note: The department parameter may not necessarily be in uppercase
Note: When removing a course node with two children (case 3), use the technique of replacing it with its successor as discussed in the lecture and textbook. You may find it useful to implement a getSuccessor helper method to find the successor of a node, following the approach outlined in the textbook.

Example:

cc = CourseCatalog()

# add a new course: cmpsc 9
lecture = Event("TR", (1530, 1645), "td-w 1701")
section1 = Event("W", (1400, 1450), "north hall 1109")
section2 = Event("W", (1500, 1550), "north hall 1109")
section3 = Event("W", (1600, 1650), "north hall 1109")
section4 = Event("W", (1700, 1750), "girvetz hall 1112")
sections = [section1, section2, section3, section4]
assert True == cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

# add a new course: art 10
lecture = Event("TR", (1300, 1550), "arts 2628")
sections = []
assert True == cc.addCourse("art", 10, "introduction to painting", lecture, sections)

'''
                                                                   root
                                             ------------------------------------------------
                                            | CMPSC 9: INTERMEDIATE PYTHON                   |
                                            |  * Lecture: TR 15:30 - 16:45, TD-W 1701        |
                                            |  + Section: W 14:00 - 14:50, NORTH HALL 1109   |
                                            |  + Section: W 15:00 - 15:50, NORTH HALL 1109   |
                                            |  + Section: W 16:00 - 16:50, NORTH HALL 1109   |
                                            |  + Section: W 17:00 - 17:50, GIRVETZ HALL 1112 |
                                             ------------------------------------------------
                                            /
     -----------------------------------------
    | ART 10: INTRODUCTION TO PAINTING        |
    |  * Lecture: TR 13:00 - 15:50, ARTS 2628 |
     -----------------------------------------
'''

print("----- in-order traversal -----")
print(cc.inOrder())

print("----- pre-order traversal -----")
print(cc.preOrder())

# remove a section from cmpsc 9
section = Event("W", (1500, 1550), "north hall 1109")
assert True == cc.removeSection("cmpsc", 9, section)

'''
                                                                   root
                                             ------------------------------------------------
                                            | CMPSC 9: INTERMEDIATE PYTHON                   |
                                            |  * Lecture: TR 15:30 - 16:45, TD-W 1701        |
                                            |  + Section: W 14:00 - 14:50, NORTH HALL 1109   |
                                            |  + Section: W 16:00 - 16:50, NORTH HALL 1109   |
                                            |  + Section: W 17:00 - 17:50, GIRVETZ HALL 1112 |
                                             ------------------------------------------------
                                            /
     -----------------------------------------
    | ART 10: INTRODUCTION TO PAINTING        |
    |  * Lecture: TR 13:00 - 15:50, ARTS 2628 |
     -----------------------------------------
'''

print("----- in-order traversal -----")
print(cc.inOrder())

print("----- pre-order traversal -----")
print(cc.preOrder())

# remove cmpsc 9
assert True == cc.removeCourse("cmpsc", 9)

'''
                       root
     -----------------------------------------
    | ART 10: INTRODUCTION TO PAINTING        |
    |  * Lecture: TR 13:00 - 15:50, ARTS 2628 |
     -----------------------------------------
'''

print("----- in-order traversal -----")
print(cc.inOrder())

print("----- pre-order traversal -----")
print(cc.preOrder())
Output:

----- in-order traversal -----
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 15:00 - 15:50, NORTH HALL 1109
 + Section: W 16:00 - 16:50, NORTH HALL 1109
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112

----- pre-order traversal -----
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 15:00 - 15:50, NORTH HALL 1109
 + Section: W 16:00 - 16:50, NORTH HALL 1109
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628

----- in-order traversal -----
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 16:00 - 16:50, NORTH HALL 1109
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112

----- pre-order traversal -----
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 16:00 - 16:50, NORTH HALL 1109
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628

----- in-order traversal -----
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628

----- pre-order traversal -----
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628
