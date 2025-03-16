# testFile.py

from Event import Event
from CourseCatalogNode import CourseCatalogNode
from CourseCatalog import CourseCatalog

def test_event():
    e1 = Event("MWF", (1000, 1050), "campbell hall")
    e2 = Event("TR", (1230, 1345), "ilp 1203")
    e3 = Event("TR", (1230, 1345), "ilp 1203")
    print(e1 == e2)
    print(e2 == e3)
    print(e1)

def test_coursecatalognode_creation():
    lecture = Event("MWF", (1000, 1050), "campbell hall")
    section1 = Event("M", (1100, 1150), "ilp 3203")
    section2 = Event("W", (1400, 1450), "ilp 3203")
    sections = [section1, section2]
    
    node = CourseCatalogNode("econ", 1, "microeconomics", lecture, sections)
    
    assert node.department == "ECON"
    assert node.courseId == 1
    assert node.courseName == "MICROECONOMICS"
    assert node.lecture == lecture
    assert node.sections == sections
    assert node.parent is None
    assert node.left is None
    assert node.right is None

def test_coursecatalognode_string():
    lecture = Event("MWF", (1000, 1050), "campbell hall")
    section1 = Event("M", (1100, 1150), "ilp 3203")
    section2 = Event("W", (1400, 1450), "ilp 3203")
    sections = [section1, section2]
    
    node = CourseCatalogNode("econ", 1, "microeconomics", lecture, sections)
    
    expected = (
        "ECON 1: MICROECONOMICS\n"
        " * Lecture: MWF 10:00 - 10:50, CAMPBELL HALL\n"
        " + Section: M 11:00 - 11:50, ILP 3203\n"
        " + Section: W 14:00 - 14:50, ILP 3203\n"
    )
    assert str(node) == expected

def test_coursecatalognode_case_conversion():
    lecture = Event("MWF", (1000, 1050), "campbell hall")
    sections = []
    
    node = CourseCatalogNode("econ", 1, "microeconomics", lecture, sections)
    
    assert node.department == "ECON"
    assert node.courseName == "MICROECONOMICS"

def test_coursecatalognode_empty_sections():
    lecture = Event("MWF", (1000, 1050), "campbell hall")
    sections = []
    
    node = CourseCatalogNode("math", 3, "calculus", lecture, sections)
    
    expected = (
        "MATH 3: CALCULUS\n"
        " * Lecture: MWF 10:00 - 10:50, CAMPBELL HALL\n"
    )
    assert str(node) == expected

def test_coursecatalog():
    cc = CourseCatalog()

    lecture = Event("TR", (1230, 1345), "ilp 1203")
    section1 = Event("M", (1400, 1450), "north hall 1109")
    section2 = Event("M", (1500, 1550), "north hall 1109")
    section3 = Event("M", (1600, 1650), "north hall 1109")
    section4 = Event("M", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]

    assert cc.addCourse("econ", 1, "microeconomics", lecture, sections) == True

    section5 = Event("T", (1000, 1050), "south hall 1101")
    assert cc.addSection("econ", 1, section5) == True

    lecture = Event("MWF", (1000, 1050), "campbell hall")
    sections = []
    assert cc.addCourse("pstat", 10, "data science principles", lecture, sections) == True

    assert cc.addCourse("ECON", 1, "microeconomics", lecture, sections) == False
    assert cc.addSection("ECON", 1, section5) == True

    result = cc.getAttendableSections("econ", 1, "M", (1400, 1600))
    expected = "M 14:00 - 14:50, NORTH HALL 1109\nM 15:00 - 15:50, NORTH HALL 1109\n"
    assert result == expected

    counts = cc.countCoursesByDepartment()
    assert counts == {"ECON": 1, "PSTAT": 1}

    in_order = cc.inOrder()
    assert "ECON 1: MICROECONOMICS" in in_order
    assert "PSTAT 10: DATA SCIENCE PRINCIPLES" in in_order

    pre_order = cc.preOrder()
    assert "ECON 1: MICROECONOMICS" in pre_order
    assert "PSTAT 10: DATA SCIENCE PRINCIPLES" in pre_order

    post_order = cc.postOrder()
    assert "ECON 1: MICROECONOMICS" in post_order
    assert "PSTAT 10: DATA SCIENCE PRINCIPLES" in post_order
    
def test_remove_section():
    cc = CourseCatalog()
    
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    sections = [section1, section2, section3]
    assert True == cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    assert True == cc.removeSection("cmpsc", 9, section2)
    assert False == cc.removeSection("cmpsc", 9, section2)
    assert False == cc.removeSection("math", 3, section1)
    non_existent_section = Event("F", (1200, 1250), "phelps 1401")
    assert False == cc.removeSection("cmpsc", 9, non_existent_section)
    assert True == cc.removeSection("CMPSC", 9, section1)

def test_remove_course_case1():
    cc = CourseCatalog()
    
    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    lecture2 = Event("MWF", (1000, 1050), "phelps 1401")
    sections = []
    
    cc.addCourse("cmpsc", 9, "intermediate python", lecture1, sections)
    cc.addCourse("math", 3, "calculus", lecture2, sections)
    
    assert True == cc.removeCourse("math", 3)  
    assert False == cc.removeCourse("math", 3)  
    assert "" == cc.getAttendableSections("math", 3, "MWF", (1000, 1050))  

def test_remove_course_case2():
    cc = CourseCatalog()
    
    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    lecture2 = Event("MWF", (1000, 1050), "phelps 1401")
    lecture3 = Event("TR", (1400, 1515), "hssb 1201")
    sections = []
    
    cc.addCourse("cmpsc", 9, "intermediate python", lecture1, sections)
    cc.addCourse("art", 7, "drawing", lecture2, sections)
    cc.addCourse("art", 1, "intro art", lecture3, sections)
    
    assert True == cc.removeCourse("art", 7)
    assert "ART 1: INTRO ART" in cc.inOrder()
    assert "CMPSC 9: INTERMEDIATE PYTHON" in cc.inOrder()

def test_remove_course_case3():
    cc = CourseCatalog()
    
    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    lecture2 = Event("MWF", (1000, 1050), "phelps 1401")
    lecture3 = Event("TR", (1400, 1515), "hssb 1201")
    sections = []
    
    cc.addCourse("cmpsc", 9, "intermediate python", lecture1, sections)
    cc.addCourse("cmpsc", 8, "intro python", lecture2, sections)
    cc.addCourse("cmpsc", 16, "advanced python", lecture3, sections)
    
    assert True == cc.removeCourse("cmpsc", 9)
    
    tree_str = cc.inOrder()
    assert "CMPSC 8: INTRO PYTHON" in tree_str
    assert "CMPSC 16: ADVANCED PYTHON" in tree_str
    assert "CMPSC 9: INTERMEDIATE PYTHON" not in tree_str

def test_remove_course_root():
    cc = CourseCatalog()
    
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    sections = []
    
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    
    assert True == cc.removeCourse("cmpsc", 9) 
    assert "" == cc.inOrder()  
    assert False == cc.removeCourse("cmpsc", 9)
