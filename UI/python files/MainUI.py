import os

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


def fill_course_list(course_list_slb, predictive_model, model_type):
    if predictive_model == 0:
        temp = 'GBT_model_'
    else:
        temp = 'LR_model_'
    count = 0
    for filename in os.listdir('..\\Data\\models\\' + temp + model_type):
        course_list_slb.insert(count, filename[:-4])
        count = + 1


def get_prereqs(prereq_type, course_name):
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

    return prerequisites
def check_duplicates(prereqs, course):
    for item in prereqs:
        if course == item:
            return False
    return True

