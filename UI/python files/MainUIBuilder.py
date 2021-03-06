#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#    Jul 26, 2019 01:42:15 PM CDT  platform: Windows NT
import os
import pickle
import sys
import pandas as pd
import MainUI
import joblib
import Pred

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

import MainUIBuilder_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    MainUIBuilder_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    MainUIBuilder_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        self.postreq = ""
        self.prereq_storage = []
        self.prereqs = []
        self.prereq_grade_df = None

        self.model_type = None

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
            [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1123x728+331+78")
        top.title("Grade Prediction")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.predict_btn = tk.Button(top)
        self.predict_btn.place(relx=0.597, rely=0.852, height=24, width=48)
        self.predict_btn.configure(activebackground="#ececec")
        self.predict_btn.configure(activeforeground="#000000")
        self.predict_btn.configure(background="#d9d9d9")
        self.predict_btn.configure(disabledforeground="#a3a3a3")
        self.predict_btn.configure(font=font9)
        self.predict_btn.configure(foreground="#000000")
        self.predict_btn.configure(highlightbackground="#d9d9d9")
        self.predict_btn.configure(highlightcolor="black")
        self.predict_btn.configure(pady="0")
        self.predict_btn.configure(text='''Predict''')
        self.predict_btn.configure(command=self.predict_callback)

        self.menubar = tk.Menu(top, font=font9, bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.course_list_slb = ScrolledListBox(top)
        self.course_list_slb.place(relx=0.009, rely=0.151, relheight=0.831
                                   , relwidth=0.304)
        self.course_list_slb.configure(background="white")
        self.course_list_slb.configure(disabledforeground="#a3a3a3")
        self.course_list_slb.configure(font="TkFixedFont")
        self.course_list_slb.configure(foreground="black")
        self.course_list_slb.configure(highlightbackground="#d9d9d9")
        self.course_list_slb.configure(highlightcolor="#d9d9d9")
        self.course_list_slb.configure(selectbackground="#c4c4c4")
        self.course_list_slb.configure(selectforeground="black")
        self.course_list_slb.configure(width=10)
        self.course_list_slb.configure(exportselection =False)
        self.course_list_slb.bind('<<ListboxSelect>>', self.select_callback)

        self.course_list_lbl = ttk.Label(top)
        self.course_list_lbl.place(relx=0.116, rely=0.124, height=19, width=62)
        self.course_list_lbl.configure(background="#d9d9d9")
        self.course_list_lbl.configure(foreground="#000000")
        self.course_list_lbl.configure(font="TkDefaultFont")
        self.course_list_lbl.configure(relief="flat")
        self.course_list_lbl.configure(text='''Course List''')

        self.prereq_lbl = ttk.Label(top)
        self.prereq_lbl.place(relx=0.508, rely=0.096, height=19, width=107)
        self.prereq_lbl.configure(background="#d9d9d9")
        self.prereq_lbl.configure(foreground="#000000")
        self.prereq_lbl.configure(font=font9)
        self.prereq_lbl.configure(relief="flat")
        self.prereq_lbl.configure(text='''Prerequisite Classes''')

        self.enter_btn = tk.Button(top)
        self.enter_btn.place(relx=0.436, rely=0.735, height=24, width=38)
        self.enter_btn.configure(activebackground="#ececec")
        self.enter_btn.configure(activeforeground="#000000")
        self.enter_btn.configure(background="#d9d9d9")
        self.enter_btn.configure(disabledforeground="#a3a3a3")
        self.enter_btn.configure(font=font9)
        self.enter_btn.configure(foreground="#000000")
        self.enter_btn.configure(highlightbackground="#d9d9d9")
        self.enter_btn.configure(highlightcolor="black")
        self.enter_btn.configure(pady="0")
        self.enter_btn.configure(text='''Enter''')
        self.enter_btn.configure(command=self.enter_callback)

        self.remove_btn = tk.Button(top)
        self.remove_btn.place(relx=0.499, rely=0.735, height=24, width=54)
        self.remove_btn.configure(activebackground="#ececec")
        self.remove_btn.configure(activeforeground="#000000")
        self.remove_btn.configure(background="#d9d9d9")
        self.remove_btn.configure(disabledforeground="#a3a3a3")
        self.remove_btn.configure(font=font9)
        self.remove_btn.configure(foreground="#000000")
        self.remove_btn.configure(highlightbackground="#d9d9d9")
        self.remove_btn.configure(highlightcolor="black")
        self.remove_btn.configure(pady="0")
        self.remove_btn.configure(text='''Remove''')
        self.remove_btn.configure(command=self.remove_callback)

        self.prereq_slb = ScrolledListBox(top)
        self.prereq_slb.place(relx=0.427, rely=0.137, relheight=0.474
                              , relwidth=0.277)
        self.prereq_slb.configure(background="white")
        self.prereq_slb.configure(disabledforeground="#a3a3a3")
        self.prereq_slb.configure(font="TkFixedFont")
        self.prereq_slb.configure(foreground="black")
        self.prereq_slb.configure(highlightbackground="#d9d9d9")
        self.prereq_slb.configure(highlightcolor="#d9d9d9")
        self.prereq_slb.configure(selectbackground="#c4c4c4")
        self.prereq_slb.configure(selectforeground="black")
        self.prereq_slb.configure(width=10)
        self.prereq_slb.configure(exportselection=False)
        self.prereq_slb.bind('<<ListboxSelect>>', self.prereq_select_callback)

        vcmd = (top.register(self.validate_gpa),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.termgpa_ety = tk.Entry(top, validate = 'key', validatecommand=vcmd)
        self.termgpa_ety.place(relx=0.739, rely=0.701, height=20, relwidth=0.128)
        self.termgpa_ety.configure(background="white")
        self.termgpa_ety.configure(disabledforeground="#a3a3a3")
        self.termgpa_ety.configure(font=font9)
        self.termgpa_ety.configure(foreground="#000000")
        self.termgpa_ety.configure(highlightbackground="#d9d9d9")
        self.termgpa_ety.configure(highlightcolor="black")
        self.termgpa_ety.configure(insertbackground="black")
        self.termgpa_ety.configure(selectbackground="#c4c4c4")
        self.termgpa_ety.configure(selectforeground="black")

        self.cumulativegpa_ety = tk.Entry(top, validate = 'key', validatecommand=vcmd)
        self.cumulativegpa_ety.place(relx=0.739, rely=0.659, height=20
                                     , relwidth=0.128)
        self.cumulativegpa_ety.configure(background="white")
        self.cumulativegpa_ety.configure(disabledforeground="#a3a3a3")
        self.cumulativegpa_ety.configure(font=font9)
        self.cumulativegpa_ety.configure(foreground="#000000")
        self.cumulativegpa_ety.configure(highlightbackground="#d9d9d9")
        self.cumulativegpa_ety.configure(highlightcolor="black")
        self.cumulativegpa_ety.configure(insertbackground="black")
        self.cumulativegpa_ety.configure(selectbackground="#c4c4c4")
        self.cumulativegpa_ety.configure(selectforeground="black")

        self.cumulativegpa_lbl = tk.Label(top)
        self.cumulativegpa_lbl.place(relx=0.579, rely=0.659, height=21
                                     , width=173)
        self.cumulativegpa_lbl.configure(activebackground="#f9f9f9")
        self.cumulativegpa_lbl.configure(activeforeground="black")
        self.cumulativegpa_lbl.configure(background="#d9d9d9")
        self.cumulativegpa_lbl.configure(disabledforeground="#a3a3a3")
        self.cumulativegpa_lbl.configure(font=font9)
        self.cumulativegpa_lbl.configure(foreground="#000000")
        self.cumulativegpa_lbl.configure(highlightbackground="#d9d9d9")
        self.cumulativegpa_lbl.configure(highlightcolor="black")
        self.cumulativegpa_lbl.configure(text='''First Prereq Cumulative GPA''')
        self.cumulativegpa_lbl.configure(width=173)

        self.termgpa_lbl = tk.Label(top)
        self.termgpa_lbl.place(relx=0.614, rely=0.701, height=21, width=120)
        self.termgpa_lbl.configure(activebackground="#f9f9f9")
        self.termgpa_lbl.configure(activeforeground="black")
        self.termgpa_lbl.configure(background="#d9d9d9")
        self.termgpa_lbl.configure(disabledforeground="#a3a3a3")
        self.termgpa_lbl.configure(font=font9)
        self.termgpa_lbl.configure(foreground="#000000")
        self.termgpa_lbl.configure(highlightbackground="#d9d9d9")
        self.termgpa_lbl.configure(highlightcolor="black")
        self.termgpa_lbl.configure(text='''First Prereq Term GPA''')
        self.termgpa_lbl.configure(width=120)

        self.struggled_lbl = tk.Label(top)
        self.struggled_lbl.place(relx=0.579, rely=0.742, height=21, width=165)
        self.struggled_lbl.configure(activebackground="#f9f9f9")
        self.struggled_lbl.configure(activeforeground="black")
        self.struggled_lbl.configure(background="#d9d9d9")
        self.struggled_lbl.configure(disabledforeground="#a3a3a3")
        self.struggled_lbl.configure(font=font9)
        self.struggled_lbl.configure(foreground="#000000")
        self.struggled_lbl.configure(highlightbackground="#d9d9d9")
        self.struggled_lbl.configure(highlightcolor="black")
        self.struggled_lbl.configure(text='''Struggled Up Until First Prereq''')

        self.struggled_combobox = ttk.Combobox(top)
        self.struggled_combobox.place(relx=0.739, rely=0.742, relheight=0.029
                                      , relwidth=0.127)
        self.struggled_combobox.configure(font=font9)
        self.struggled_combobox.configure(takefocus="")
        self.struggled_combobox.configure(state="readonly")
        self.struggled_combobox.configure(values=["Good", "Struggled", "Extremely Struggled"])
        self.struggled_combobox.current(0)

        self.prediction = tk.IntVar()

        self.root_rbtn = tk.Radiobutton(top)
        self.root_rbtn.place(relx=0.018, rely=0.069, relheight=0.034
                             , relwidth=0.047)
        self.root_rbtn.configure(activebackground="#ececec")
        self.root_rbtn.configure(activeforeground="#000000")
        self.root_rbtn.configure(background="#d9d9d9")
        self.root_rbtn.configure(disabledforeground="#a3a3a3")
        self.root_rbtn.configure(font=font9)
        self.root_rbtn.configure(foreground="#000000")
        self.root_rbtn.configure(highlightbackground="#d9d9d9")
        self.root_rbtn.configure(highlightcolor="black")
        self.root_rbtn.configure(justify='left')
        self.root_rbtn.configure(text='''Root''')
        self.root_rbtn.configure(variable=self.prediction)
        self.root_rbtn.configure(value=0)
        self.root_rbtn.configure(command=lambda : self.select_callback('root'))

        self.all_rbtn = tk.Radiobutton(top)
        self.all_rbtn.place(relx=0.125, rely=0.069, relheight=0.034
                            , relwidth=0.037)
        self.all_rbtn.configure(activebackground="#ececec")
        self.all_rbtn.configure(activeforeground="#000000")
        self.all_rbtn.configure(background="#d9d9d9")
        self.all_rbtn.configure(disabledforeground="#a3a3a3")
        self.all_rbtn.configure(font=font9)
        self.all_rbtn.configure(foreground="#000000")
        self.all_rbtn.configure(highlightbackground="#d9d9d9")
        self.all_rbtn.configure(highlightcolor="black")
        self.all_rbtn.configure(justify='left')
        self.all_rbtn.configure(text='''All''')
        self.all_rbtn.configure(variable=self.prediction)
        self.all_rbtn.configure(value=1)
        self.all_rbtn.configure(command=lambda : self.select_callback('all'))

        self.imme_rbtn = tk.Radiobutton(top)
        self.imme_rbtn.place(relx=0.205, rely=0.069, relheight=0.034
                             , relwidth=0.076)
        self.imme_rbtn.configure(activebackground="#ececec")
        self.imme_rbtn.configure(activeforeground="#000000")
        self.imme_rbtn.configure(background="#d9d9d9")
        self.imme_rbtn.configure(disabledforeground="#a3a3a3")
        self.imme_rbtn.configure(font=font9)
        self.imme_rbtn.configure(foreground="#000000")
        self.imme_rbtn.configure(highlightbackground="#d9d9d9")
        self.imme_rbtn.configure(highlightcolor="black")
        self.imme_rbtn.configure(justify='left')
        self.imme_rbtn.configure(text='''Immediate''')
        self.imme_rbtn.configure(variable=self.prediction)
        self.imme_rbtn.configure(value=2)
        self.imme_rbtn.configure(command=lambda : self.select_callback('imme'))

        self.model_type_lbl = ttk.Label(top)
        self.model_type_lbl.place(relx=0.116, rely=0.027, height=19, width=67)
        self.model_type_lbl.configure(background="#d9d9d9")
        self.model_type_lbl.configure(foreground="#000000")
        self.model_type_lbl.configure(font=font9)
        self.model_type_lbl.configure(relief="flat")
        self.model_type_lbl.configure(text='''Model Type''')
        self.model_type_lbl.configure(width=67)

        self.grade_entry_combobox = ttk.Combobox(top)
        self.grade_entry_combobox.place(relx=0.454, rely=0.694, relheight=0.029
                                        , relwidth=0.074)
        self.grade_entry_combobox.configure(width=83)
        self.grade_entry_combobox.configure(state="readonly")
        self.grade_entry_combobox.configure(values=["None", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"])
        self.grade_entry_combobox.current(0)

        self.prereq_grades_listbox = ScrolledListBox(top)
        self.prereq_grades_listbox.place(relx=0.703, rely=0.137, relheight=0.474
                                         , relwidth=0.09)
        self.prereq_grades_listbox.configure(background="white")
        self.prereq_grades_listbox.configure(disabledforeground="#a3a3a3")
        self.prereq_grades_listbox.configure(font="TkFixedFont")
        self.prereq_grades_listbox.configure(foreground="black")
        self.prereq_grades_listbox.configure(highlightbackground="#d9d9d9")
        self.prereq_grades_listbox.configure(highlightcolor="#d9d9d9")
        self.prereq_grades_listbox.configure(selectbackground="#c4c4c4")
        self.prereq_grades_listbox.configure(selectforeground="black")
        self.prereq_grades_listbox.configure(width=10)
        self.prereq_grades_listbox.configure(exportselection =False)

        self.prereq_grades_lbl = ttk.Label(top)
        self.prereq_grades_lbl.place(relx=0.721, rely=0.096, height=19, width=47)

        self.prereq_grades_lbl.configure(background="#d9d9d9")
        self.prereq_grades_lbl.configure(foreground="#000000")
        self.prereq_grades_lbl.configure(font=font9)
        self.prereq_grades_lbl.configure(relief="flat")
        self.prereq_grades_lbl.configure(takefocus="0")
        self.prereq_grades_lbl.configure(text='''Grades''')

        self.prereq_grade_entry_lbl = ttk.Label(top)
        self.prereq_grade_entry_lbl.place(relx=0.445, rely=0.659, height=19
                                          , width=107)
        self.prereq_grade_entry_lbl.configure(background="#d9d9d9")
        self.prereq_grade_entry_lbl.configure(foreground="#000000")
        self.prereq_grade_entry_lbl.configure(font=font9)
        self.prereq_grade_entry_lbl.configure(relief="flat")
        self.prereq_grade_entry_lbl.configure(takefocus="0")
        self.prereq_grade_entry_lbl.configure(text='''Prerequisite Grade''')
        self.prereq_grade_entry_lbl.configure(width=107)

        self.predictive_model = tk.IntVar()

        self.gbt_radio = tk.Radiobutton(top)
        self.gbt_radio.place(relx=0.65, rely=0.838, relheight=0.034
                             , relwidth=0.176)
        self.gbt_radio.configure(activebackground="#ececec")
        self.gbt_radio.configure(activeforeground="#000000")
        self.gbt_radio.configure(anchor='w')
        self.gbt_radio.configure(background="#d9d9d9")
        self.gbt_radio.configure(disabledforeground="#a3a3a3")
        self.gbt_radio.configure(foreground="#000000")
        self.gbt_radio.configure(highlightbackground="#d9d9d9")
        self.gbt_radio.configure(highlightcolor="black")
        self.gbt_radio.configure(justify='left')
        self.gbt_radio.configure(text='''Gradient Boosted Trees Classifier''')
        self.gbt_radio.configure(width=198)
        self.gbt_radio.configure(variable=self.predictive_model)
        self.gbt_radio.configure(value=0)

        self.lr_radio = tk.Radiobutton(top)
        self.lr_radio.place(relx=0.65, rely=0.879, relheight=0.034
                            , relwidth=0.176)
        self.lr_radio.configure(activebackground="#ececec")
        self.lr_radio.configure(activeforeground="#000000")
        self.lr_radio.configure(anchor='w')
        self.lr_radio.configure(background="#d9d9d9")
        self.lr_radio.configure(disabledforeground="#a3a3a3")
        self.lr_radio.configure(foreground="#000000")
        self.lr_radio.configure(highlightbackground="#d9d9d9")
        self.lr_radio.configure(highlightcolor="black")
        self.lr_radio.configure(justify='left')
        self.lr_radio.configure(text='''Logistic Regression''')
        self.lr_radio.configure(width=198)
        self.lr_radio.configure(variable=self.predictive_model)
        self.lr_radio.configure(value=1)

    def prereq_select_callback(self, evt):
        self.grade_entry_combobox.current(0)

    def select_callback(self, evt):
        if evt == 'root' or evt == 'imme' or evt == 'all':
            self.model_type = evt
            self.course_list_slb.delete(0, tk.END)
            MainUI.fill_course_list(self.course_list_slb, self.predictive_model.get(), evt)
        try:
            self.prereq_slb.delete(0, tk.END)
            self.prereq_grades_listbox.delete(0, tk.END)
            self.prereqs = MainUI.get_prereqs(self.model_type, self.course_list_slb.get(self.course_list_slb.curselection()[0]))
            for course in self.prereqs:
                self.prereq_slb.insert(tk.END, course)
                self.prereq_storage.append('')
                self.prereq_grades_listbox.insert(tk.END, "None")
            self.postreq = self.course_list_slb.get(self.course_list_slb.curselection()[0])
        except IndexError:
            return
        return

    def enter_callback(self):
        try:
            index = self.prereqs.index(self.prereq_slb.get(tk.ACTIVE))
            self.prereq_storage[index] = self.grade_entry_combobox.get()
            self.prereq_grades_listbox.delete(index)
            self.prereq_grades_listbox.insert(index, self.grade_entry_combobox.get())

        except IndexError:
            print('dumb')
            return
        return

    def remove_callback(self):
        try:
            index = self.prereqs.index(self.prereq_slb.get(tk.ACTIVE))
            self.prereq_storage[index] = 'None'
            self.prereq_grades_listbox.delete(index)
            self.prereq_grades_listbox.insert(index, 'None')

        except IndexError:
            print('dumb')
            return
        return

    def predict_callback(self):
            term_gpa = float(self.termgpa_ety.get())
            cumulative_gpa = float(self.cumulativegpa_ety.get())
            if 0 <= term_gpa <= 4 and \
                    0 <= cumulative_gpa <= 4:
                X = pd.DataFrame()
                for course in self.prereqs:
                    X[course] = '$'
                    index = self.prereqs.index(course)
                    X.at[0, course] = self.convert_grade(self.prereq_storage[index])

                X['cumulative_gpa'] = ''
                X.at[0, 'cumulative_gpa'] = float(self.cumulativegpa_ety.get())

                X['prev_term_gpa'] = ''
                X.at[0, 'prev_term_gpa'] = float(self.termgpa_ety.get())

                X['struggle'] = ''
                X.at[0, 'struggle'] = self.determine_struggle(self.struggled_combobox.get())

                if self.predictive_model.get() == 0:
                    model_path = '..\\Data\\models\\GBT_model_' + self.model_type + '\\' + self.course_list_slb.get(tk.ACTIVE) + '.pkl'
                elif self.predictive_model.get() == 1:
                    model_path = '..\\Data\\models\\LR_model_' + self.model_type + '\\' + self.course_list_slb.get(
                        tk.ACTIVE) + '.pkl'

                model = pickle.load(open(model_path, 'rb'))

                #   F,  D,  D+, C-, C,  C+, B-, B,  B+, A-, A
                y_grades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                y = model.predict_proba(X)
                for t in y:
                    count = 0
                    not_filled = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    for f in t:
                        y_grades[model.classes_[count]] = f
                        not_filled.remove(model.classes_[count])
                        count += 1
                    for q in not_filled:
                        y_grades[q] = 0

                Pred.vp_start_gui(self.postreq, y_grades)

    def which_prediction(self):
        if self.prediction.get() == 0:
            return 'root'
        elif self.prediction.get() == 1:
            return 'all'
        elif self.prediction.get() == 2:
            return 'imme'
        else:
            return 'unknown'

    def determine_struggle(self, string_struggle):
        if string_struggle == "Good":
            return 3
        if string_struggle == "Struggled":
            return 2
        return -1

    def convert_grade(self, string_grade):
        if string_grade == 'A':
            return 10
        elif string_grade == 'A-':
            return 9
        elif string_grade == 'B+':
            return 8
        elif string_grade == 'B':
            return 7
        elif string_grade == 'B-':
            return 6
        elif string_grade == 'C+':
            return 5
        elif string_grade == 'C':
            return 4
        elif string_grade == 'C-':
            return 3
        elif string_grade == 'D+':
            return 2
        elif string_grade == 'D':
            return 1
        elif string_grade == 'F':
            return 0
        else:
            return -1

    def validate_gpa(self, action, index, value_if_allowed,
                     prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()
