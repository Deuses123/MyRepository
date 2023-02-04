class Student:
    def __init__(object, name, surname, dateOfBirth, scores):
        object.name = name
        object.surname = surname
        object.dateOfBirth = dateOfBirth
        object.scores = scores
        object.GPA = object.calculate_GPA()

    def calculate_GPA(object):
        sum = 0
        for score in object.scores:
            sum += score
        average = sum / len(object.scores)
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def info(object):
        print("Name:", object.name)
        print("Surname:", object.surname)
        print("Date of Birth:", object.dateOfBirth)
        print("Scores:", object.scores)
        print("GPA:", object.GPA)

scores = [90, 85, 82, 78, 95]
student = Student("Sanzhar", "Kalibekov", "15/09/2002", scores)
student.info()
