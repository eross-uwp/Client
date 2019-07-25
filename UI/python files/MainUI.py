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

__COMBINED_COURSE_STRUCTURE_FILEPATH = 'C:\\Users\\yangz\\Documents\\GitHub\\Server\Data\\combined_course_structure.csv'



def fill_course_list(course_list_slb):
    courses = pd.read_csv('C:\\Users\\yangz\\Documents\\GitHub\\Server\\Data\\unique_courses.csv')
    count = 0
    for each_course in courses['courses'].values:
        course_list_slb.insert(count, each_course)
        count = + 1


def fill_prereq(prereq_slb, prereq_type, course_name):
    prereq_slb.delete(0, tk.END)
    prerequisite_tree_maker = TreeMaker(__COMBINED_COURSE_STRUCTURE_FILEPATH)
    tree = prerequisite_tree_maker.process(course_name)
    count = 0
    if prereq_type is 'root':
        prereqs = tree.get_all_prereqs()
        for k in list(prereqs):
            if k.does_have_prereq() == 1:
                prereqs.remove(k)
        for each_course in prereqs:
            prereq_slb.insert(count, each_course)
            count = + 1

    if prereq_type is 'all':
        prereqs = tree.get_all_prereqs()
        for each_course in prereqs:
            prereq_slb.insert(count, each_course.get_name())
            count = + 1
    if prereq_type is 'imme':
        prereqs = tree.get_immediate_prereqs()
        for each_course in prereqs:
            prereq_slb.insert(count, each_course)
            count = + 1


def tt():
    print('aaa')


