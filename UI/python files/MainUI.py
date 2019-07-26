import pandas as pd
from TreeScripts.TreeMaker import TreeMaker

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

__COMBINED_COURSE_STRUCTURE_FILEPATH = '..\\Data\\combined_course_structure.csv'



def fill_course_list(course_list_slb):
    courses = pd.read_csv('..\\Data\\unique_courses.csv')
    for each_course in courses['courses'].values:
        course_list_slb.insert(tk.END, each_course)


def fill_prereq(prereq_slb, prereq_type, course_name):
    prereq_slb.delete(0, tk.END)
    prerequisites = []
    prerequisite_tree_maker = TreeMaker(__COMBINED_COURSE_STRUCTURE_FILEPATH)
    tree = prerequisite_tree_maker.process(course_name)
    if prereq_type is 'root':
        prereqs = tree.get_all_prereqs()
        for k in list(prereqs):
            if k.does_have_prereq() == 1:
                prereqs.remove(k)
        for each_course in prereqs:
            if check_duplicates(prerequisites, each_course.get_name()):
                prerequisites.append(each_course.get_name())

    if prereq_type is 'all':
        prereqs = tree.get_all_prereqs()
        for each_course in prereqs:
            if check_duplicates(prerequisites, each_course.get_name()):
                prerequisites.append(each_course.get_name())

    if prereq_type is 'imme':
        prereqs = tree.get_immediate_prereqs()
        for each_course in prereqs:
            if check_duplicates(prerequisites, each_course.get_name()):
                prerequisites.append(each_course.get_name())

    for course in prerequisites:
        prereq_slb.insert(tk.END, course)

def check_duplicates(prereqs, course):
    for item in prereqs:
        if course == item:
            return False
    return True

def tt():
    print('aaa')


