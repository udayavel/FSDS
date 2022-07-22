import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


# Example 1 - private

class course_library:

    def __init__(self, course_id, course_name):
        self.__course_id = course_id  # private class variable
        self.course_name = course_name

    def view_course(self):
        '''VIEW COURSE DATA'''
        try:
            logging.info(f'Course ID {self.__course_id} and Course Name {self.course_name}')
        except Exception as e:
            logging.error(e)


logging.info('******************************************PRIVATE******************************************')
logging.info('private Example # 1')
cl = course_library('ML1345', 'Data Science')
cl.view_course()


# Example 2 - private

class course_library:

    def __init__(self, course_id, course_name):
        self.__course_id = course_id  # private class variable
        self.course_name = course_name

    def view_course(self):
        '''VIEW COURSE DATA'''
        try:
            logging.info(f'Course ID {self.__course_id} and Course Name {self.course_name}')
        except Exception as e:
            logging.error(e)

    def change_id(self, cid):
        '''CAHNGE COURSE ID'''
        try:
            self.__course_id = cid
            logging.info(f'Course Id was changed to {cid}')
        except Exception as e:
            logging.error(e)


logging.info('private Example # 2')
cl = course_library('ML1345', 'Data Science')
cl.change_id('ML1234')
cl.view_course()


# Example 3 - private

class one_neuron:

    def __init__(self, class_id, class_name):
        self.__class_id = class_id  # private class variable
        self.class_name = class_name

    def view_one_course(self):
        '''VIEW COURSE SPECIFIC'''
        try:
            logging.info(f'Class ID {self.__class_id} and Class Name {self.class_name}')
        except Exception as e:
            logging.error(e)


logging.info('private Example # 3')
on = one_neuron('ONE12345', 'Kids Neuron')
on.view_one_course()


# Example 4 - private

class one_neuron:

    def __init__(self, class_id, class_name):
        self.__class_id = class_id  # private class variable
        self.class_name = class_name

    def view_one_course(self):
        '''VIEW COURSE SPECIFIC'''
        try:
            logging.info(f'Class ID {self.__class_id} and Class Name {self.class_name}')
        except Exception as e:
            logging.error(e)

    def change_one_neuron(self, cid):
        '''CHANGE ONE NEURON CLASS ID'''
        try:
            self.__course_id = cid
            logging.info(f'Class Id was changed to {cid}')
        except Exception as e:
            logging.error(e)


logging.info('private Example # 4')
on = one_neuron('ONE12345', 'Kids Neuron')
on.change_one_neuron('ONE23145')
on.view_one_course()


# Example 5 - private

class affliate:
    __affliate_link = 'https://affiliate.ineuron.ai/'

    def view_affliate(self):
        '''VIEW AFFLIATE LINK'''
        try:
            logging.info(f'Affliate Link {self.__affliate_link}')
        except Exception as e:
            logging.error(e)


logging.info('private Example # 5')
af = affliate()
af.view_affliate()
af._affliate__affliate_link = 'www.google.com'  # changing private variable value using class name
af.view_affliate()


# Example 6 - private

class affliate:
    __affliate_link = 'https://affiliate.ineuron.ai/'

    def view_affliate(self):
        '''VIEW AFFLIATE LINK'''
        try:
            logging.info(f'Affliate Link {self.__affliate_link}')
        except Exception as e:
            logging.error(e)

    def change_affliate(self, link):
        '''CHANGE AFFLIATE LINK'''
        try:
            self.__affliate_link = link
        except Exception as e:
            logging.error(e)


logging.info('private Example # 6')
af = affliate()
af.view_affliate()
af.change_affliate('www.google.com')  # changing private variable value through function
af.view_affliate()


# Example 7 - private

class careers:

    def __init__(self, job_type, location):
        self.__job_type = job_type
        self.location = location

    def view_opening(self):
        '''VIEW OPENING INFORMATION'''
        try:
            logging.info(f'Job opening with type {self.__job_type} at location {self.location}')
        except Exception as e:
            logging.error(e)


logging.info('private Example # 7')
career = careers('Full Time', 'Bangalore')
career.view_opening()


# Example 8 - private

class careers:

    def __init__(self, job_type, location):
        self.__job_type = job_type
        self.location = location

    def view_opening(self):
        '''VIEW OPENING INFORMATION'''
        try:
            logging.info(f'Job opening with type {self.__job_type} at location {self.location}')
        except Exception as e:
            logging.error(e)

    def change_opening(self, location):
        '''CHANGING OPENING LOCATION'''
        try:
            logging.info('changing opening location')
            self.location = location
        except Exception as e:
            logging.error(e)


logging.info('private Example # 8')
career = careers('Full Time', 'Bangalore')
career.view_opening()
career.change_opening('Chennai')
career.view_opening()


# Example 9 - private

class internship:

    def __init__(self, candidate_name, domain):
        self.__candidate_name = candidate_name
        self.domain = domain

    def view_domain(self):
        '''VIEW DOMAIN INFORMATION'''
        try:
            logging.info(
                f'Hi {self.__candidate_name}, your domain {self.domain} internship was registered successfully')
        except Exception as e:
            logging.error(e)


logging.info('private Example # 9')
intr = internship('Udayavel', 'Data Science')
intr.view_domain()


# Example 10 - private

class internship:

    def __init__(self, candidate_name, domain):
        self.__candidate_name = candidate_name
        self.domain = domain

    def view_domain(self):
        '''VIEW DOMAIN INFORMATION'''
        try:
            logging.info(
                f'Hi {self.__candidate_name}, your domain {self.domain} internship was registered successfully')
        except Exception as e:
            logging.error(e)

    def change_domain(self, domain):
        '''CHANGE DOMAIN INFORMATION'''
        try:
            self.domain = domain
            logging.info(f'Hi {self.__candidate_name}, your domain {self.domain} was changed')
        except Exception as e:
            logging.error(e)


logging.info('private Example # 10')
intr = internship('Udayavel', 'Data Science')
intr.view_domain()
intr.change_domain('Javascript')
