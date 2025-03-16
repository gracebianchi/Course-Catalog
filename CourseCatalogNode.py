# CourseCatalogNode.py

from Event import Event

class CourseCatalogNode:

    def __init__(self, department, courseId, courseName, lecture, sections):
        self.department = department.upper()
        self.courseId = courseId
        self.courseName = courseName.upper()
        self.lecture = lecture
        self.sections = sections
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        result = f"{self.department} {self.courseId}: {self.courseName}\n"
        result += f" * Lecture: {self.lecture}\n"
        for section in self.sections:
            result += f" + Section: {section}\n"
        return result


