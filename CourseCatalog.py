# CourseCatalog.py

from Event import Event
from CourseCatalogNode import CourseCatalogNode

class CourseCatalog:

    def __init__(self):
        self.root = None

    def addCourse(self, department, courseId, courseName, lecture, sections):
        if self.root is None:
            self.root = CourseCatalogNode(department, courseId, courseName, lecture, sections)
            return True
        
        current = self.root
        while True:
            if current.department == department.upper() and current.courseId == courseId:
                return False
            
            if department.upper() < current.department or \
               (department.upper() == current.department and courseId < current.courseId):
                if current.left is None:
                    current.left = CourseCatalogNode(department, courseId, courseName, lecture, sections)
                    current.left.parent = current
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = CourseCatalogNode(department, courseId, courseName, lecture, sections)
                    current.right.parent = current
                    return True
                current = current.right

    def addSection(self, department, courseId, section):
        current = self.root
        while current is not None:
            if current.department == department.upper() and current.courseId == courseId:
                current.sections.append(section)
                return True
            if department.upper() < current.department or \
               (department.upper() == current.department and courseId < current.courseId):
                current = current.left
            else:
                current = current.right
        return False

    def _inOrderHelper(self, node):
        if node is None:
            return ""
        return self._inOrderHelper(node.left) + str(node) + self._inOrderHelper(node.right)

    def inOrder(self):
        return self._inOrderHelper(self.root)

    def _preOrderHelper(self, node):
        if node is None:
            return ""
        return str(node) + self._preOrderHelper(node.left) + self._preOrderHelper(node.right)

    def preOrder(self):
        return self._preOrderHelper(self.root)

    def _postOrderHelper(self, node):
        if node is None:
            return ""
        return self._postOrderHelper(node.left) + self._postOrderHelper(node.right) + str(node)

    def postOrder(self):
        return self._postOrderHelper(self.root)

    def getAttendableSections(self, department, courseId, availableDay, availableTime):
        department = department.upper()
        current = self.root
        result = ''
        while current is not None:
            if current.department == department and current.courseId == courseId:
                for section in current.sections:
                    if section.day == availableDay:
                        section_start, section_end = section.time
                        available_start, available_end = availableTime
                        if section_start >= available_start and section_end <= available_end:
                            result += f"{section.day} {section.time[0]//100:0>2}:{section.time[0]%100:0>2} - {section.time[1]//100:0>2}:{section.time[1]%100:0>2}, {section.location.upper()}\n"
            
                return result
        
            if department < current.department or (department == current.department and courseId < current.courseId):
                current = current.left
            else:
                current = current.right

        return "" 

    def _countCoursesHelper(self, node, counts):
        if node is None:
            return
        counts[node.department] = counts.get(node.department, 0) + 1
        self._countCoursesHelper(node.left, counts)
        self._countCoursesHelper(node.right, counts)

    def countCoursesByDepartment(self):
        counts = {}
        self._countCoursesHelper(self.root, counts)
        return counts

    def getSuccessor(self, node):
        if node.right is not None:
            current = node.right
            while current.left is not None:
                current = current.left
            return current
        return None

    def removeCourse(self, department, courseId):
        department = department.upper()
        current = self.root
        parent = None
        
        while current is not None and not (current.department == department and current.courseId == courseId):
            parent = current
            if department < current.department or (department == current.department and courseId < current.courseId):
                current = current.left
            else:
                current = current.right
                
        if current is None: 
            return False
            

        if current.left is None and current.right is None:
            if parent is None:  
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
                
        elif current.left is None:  
            if parent is None:  
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            current.right.parent = parent
            
        elif current.right is None:  
            if parent is None:  
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            current.left.parent = parent
            
        else:
            successor = self.getSuccessor(current)
            successorDept = successor.department
            successorId = successor.courseId
            successorName = successor.courseName
            successorLecture = successor.lecture
            successorSections = successor.sections
            self.removeCourse(successor.department, successor.courseId)
            current.department = successorDept
            current.courseId = successorId
            current.courseName = successorName
            current.lecture = successorLecture
            current.sections = successorSections
            
        return True

    def removeSection(self, department, courseId, section):
        department = department.upper()
        current = self.root
        
        while current is not None:
            if current.department == department and current.courseId == courseId:
                for i, s in enumerate(current.sections):
                    if s == section:
                        current.sections.pop(i)
                        return True
                return False  
            
            if department < current.department or (department == current.department and courseId < current.courseId):
                current = current.left
            else:
                current = current.right
                
        return False

