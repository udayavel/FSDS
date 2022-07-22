import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


# example 1 - abstraction

class hall_of_fame:

    def __init__(self, candidate_id, comments):
        self.__candidate_id = candidate_id
        self.comments = comments

    def access_hof(self):
        '''ACCESS HALL OF FAME'''
        try:
            logging.info('Accessing Hall of Fame data')
            logging.info(f'{self.__candidate_id} --> {self.comments}')
        except Exception as e:
            logging.error(e)

logging.info('******************************************ABSTRACTION******************************************')
logging.info('abstraction example #1')
hof = hall_of_fame('IN1234', 'Made successfull transition to Data Science domain')
logging.info('Accesing private variable with class name')
logging.info(hof._hall_of_fame__candidate_id)
hof.access_hof()


# example 2 - abstraction

class course_library:

    def __init__(self, course_id, course):
        self.__course_id = course_id
        self.course = course

    def view_course(self):
        '''VIEW COURSE INFO'''
        try:
            logging.info('Viewing Course library')
            logging.info(f'{self.__course_id} --> {self.course}')
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #2')
cl = course_library('DS1234', 'Data Structures and Algorithms')
logging.info('Accesing private variable with class name')
logging.info(cl._course_library__course_id)
cl.view_course()


# example 3 - abstraction

class one_neuron:

    def __init__(self, neuron_type):
        self.__neuron_type = neuron_type

    def view_neuron_type(self):
        '''VIEW NEURON TYPE'''
        try:
            logging.info('Viewing Neuron Type')
            logging.info(f'{self.__neuron_type} was listed')
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #3')
on = one_neuron(['Tech Neuron', 'Kids Neuron'])
logging.info('Accesing private variable with class name')
logging.info(on._one_neuron__neuron_type)
on.view_neuron_type()


# example 4 - abstraction

class internship:

    def __init__(self, domain):
        self.__domain = domain

    def view_internship(self):
        '''VIEW INTERNSHIP INFO'''
        try:
            logging.info(f'{self.__domain} was listed in internship program')
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #4')
intr = internship(['Full Stack Data Science', 'Javascript'])
logging.info('Accesing private variable with class name')
logging.info(intr._internship__domain)
intr.view_internship()


# example 5 - abstraction

class affliate:

    def __init__(self, affliate_id):
        self.__affliate_id = affliate_id

    def view_affliate(self):
        '''VIEW AFFLIATE LINK'''
        try:
            logging.info(f'your affliate id {self.__affliate_id} was registered')
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #5')
af = affliate('AF23890')
logging.info('Accesing private variable with class name')
logging.info(af._affliate__affliate_id)
af.view_affliate()


# example 6 - abstraction

class careers:

    def __init__(self, openings):
        self.__openings = openings

    def view_openings(self):
        '''VIEW OPENING INFO'''
        try:
            for i in self.__openings.keys():
                logging.info(f'opening for {i} at {self.__openings[i]} location')
        except Exception as e:
            logging.error(e)

    def add_openings(self, role, location):
        '''ADD OPENINGS'''
        try:
            self.__openings[role] = location
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #6')
car = careers({'Business Development Associate': 'Bangalore', 'Senior UI/UX developer': 'Bangalore',
               'UI/UX developer': 'Bangalore'})
logging.info('Accesing private variable with class name')
logging.info(car._careers__openings)
car.view_openings()
car.add_openings('Automation Developer', 'Bangalore')
car.view_openings()


# example 7 - abstraction

class achievers:

    def __init__(self, achiever_list):
        self.__achiever_list = achiever_list

    def view_achievers(self):
        '''VIEW ACHIEVERS INFO'''
        try:
            logging.info(f'{self.__achiever_list}')
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #7')
ach = achievers(['Microsoft', 'VM Ware', 'Adobe', 'Wipro'])
logging.info('Accesing private variable with class name')
logging.info(ach._achievers__achiever_list)
ach.view_achievers()


# example 8 - abstraction

class course_syllabus:

    def __init__(self, syllabus_list):
        self.__syllabus_list = syllabus_list

    def view_syllabus(self):
        '''VIEW SYLLABUS INFO'''
        try:
            count = 0
            for i in self.__syllabus_list:
                logging.info(f'{count}.{i}')
                count += 1
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #8')
syl = course_syllabus(['Python', 'Stats', 'Machine Learning', 'Deep Learning', 'Computer Vision'])
logging.info('Accesing private variable with class name')
logging.info(syl._course_syllabus__syllabus_list)
syl.view_syllabus()


# example 9 - abstraction

class course_analytics:

    def __init__(self, video_progress):
        self.__video_progress = video_progress

    def view_analytics(self):
        '''VIEW ANALYTICS DATA'''
        try:
            logging.info('Out of 10')
            logging.info('*' * self.__video_progress)
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #9')
ca = course_analytics(8)
logging.info('Accesing private variable with class name')
logging.info(ca._course_analytics__video_progress)
ca.view_analytics()


# example 10 - abstraction

class assignment_status:

    def __init__(self, assignment):
        self.__assignment = assignment

    def view_assignment_analytics(self):
        '''VIEW ASSIGNMENT ANALYTICS DATA'''
        try:
            logging.info('Out of 20')
            logging.info('#' * self.__assignment)
        except Exception as e:
            logging.error(e)


logging.info('abstraction example #10')
assignment = assignment_status(18)
logging.info('Accesing private variable with class name')
logging.info(assignment._assignment_status__assignment)
assignment.view_assignment_analytics()
