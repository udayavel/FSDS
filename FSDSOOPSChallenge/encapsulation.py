import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


# example 1 - encapsulation

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

logging.info('******************************************ENCAPSULATION******************************************')
logging.info('encapsulation example #1')
hof = hall_of_fame('IN1234', 'Made successfull transition to Data Science domain')
hof.access_hof()


# example 2 - encapsulation

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


logging.info('encapsulation example #2')
cl = course_library('DS1234', 'Data Structures and Algorithms')
cl.view_course()


# example 3 - encapsulation

class one_neuron:

    def __init__(self, neuron_type):
        self.__neuron_type = neuron_type

    def view_neuron_type(self):
        '''ACCESS NEURON TYPE'''
        try:
            logging.info('Viewing Neuron Type')
            logging.info(f'{self.__neuron_type} was listed')
        except Exception as e:
            logging.error(e)


logging.info('encapsulation example #3')
on = one_neuron(['Tech Neuron', 'Kids Neuron'])
on.view_neuron_type()


# example 4 - encapsulation

class internship:

    def __init__(self, domain):
        self.__domain = domain

    def view_internship(self):
        '''VIEW INTERNSHIP DATA'''
        try:
            logging.info(f'{self.__domain} was listed in internship program')
        except Exception as e:
            logging.error(e)


logging.info('encapsulation example #4')
intr = internship(['Full Stack Data Science', 'Javascript'])
intr.view_internship()


# example 5 - encapsulation

class affliate:

    def __init__(self, affliate_id):
        self.__affliate_id = affliate_id

    def view_affliate(self):
        '''VIEW AFFLIATE LINK'''
        try:
            logging.info(f'your affliate id {self.__affliate_id} was registered')
        except Exception as e:
            logging.error(e)


logging.info('encapsulation example #5')
af = affliate('AF23890')
af.view_affliate()


# example 6 - encapsulation

class careers:

    def __init__(self, openings):
        self.__openings = openings

    def view_openings(self):
        '''VIEW OPENINGS'''
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


logging.info('encapsulation example #6')
car = careers({'Business Development Associate': 'Bangalore', 'Senior UI/UX developer': 'Bangalore',
               'UI/UX developer': 'Bangalore'})
car.view_openings()
car.add_openings('Automation Developer', 'Bangalore')
car.view_openings()


# example 7 - encapsulation

class achievers:

    def __init__(self, achiever_list):
        self.__achiever_list = achiever_list

    def view_achievers(self):
        '''VIEW ACHIEVERS'''
        try:
            logging.info(f'{self.__achiever_list}')
        except Exception as e:
            logging.error(e)


logging.info('encapsulation example #7')
ach = achievers(['Microsoft', 'VM Ware', 'Adobe', 'Wipro'])
ach.view_achievers()


# example 8 - encapsulation

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


logging.info('encapsulation example #8')
syl = course_syllabus(['Python', 'Stats', 'Machine Learning', 'Deep Learning', 'Computer Vision'])
syl.view_syllabus()


# example 9 - encapsulation

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


logging.info('encapsulation example #9')
ca = course_analytics(8)
ca.view_analytics()


# example 10 - encapsulation

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


logging.info('encapsulation example #10')
assignment = assignment_status(18)
assignment.view_assignment_analytics()
