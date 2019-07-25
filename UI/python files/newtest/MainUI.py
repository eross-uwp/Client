import pandas as pd



def fill_course_list(UI):
    courses = pd.read_csv('C:\\Users\\yangz\\Documents\\GitHub\\Server\\Data\\unique_courses.csv')
    count = 0
    for each_course in courses['courses'].values:
        UI.Scrolledlistbox1.insert(count, each_course)
        count = + 1