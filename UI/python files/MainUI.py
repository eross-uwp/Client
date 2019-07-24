courses = pd.read_csv('C:\\Users\\yangz\\Documents\\GitHub\\Server\\Data\\unique_courses.csv')
count = 0
for each_course in courses['courses'].values:
    self.Scrolledlistbox1.insert(count, each_course)
    count = + 1