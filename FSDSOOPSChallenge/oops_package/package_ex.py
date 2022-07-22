import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


class ineuron:

    def __init__(self):
        pass

    def access_hof(self):
        '''ACCESS HALL OF FAME'''
        try:
            logging.info('Accessing Hall of Fame data')
        except Exception as e:
            logging.error(e)

    def view_assignment_analytics(self, count):
        '''VIEW ASSIGNMENT ANALYTICS'''
        try:
            logging.info('Out of 20')
            logging.info('#' * count)
        except Exception as e:
            logging.error(e)

    def view_analytics(self, count):
        '''VIEW ANALYTICS'''
        try:
            logging.info('Out of 10')
            logging.info('*' * count)
        except Exception as e:
            logging.error(e)

    def view_syllabus(self, syllabus):
        '''VIEW SYLLABUS INFO'''
        try:
            count = 0
            for i in syllabus:
                logging.info(f'{count}.{i}')
                count += 1
        except Exception as e:
            logging.error(e)

    def view_achievers(self, achievers):
        '''VIEW ACHIEVERS'''
        try:
            logging.info(f'{achievers}')
        except Exception as e:
            logging.error(e)

    def view_openings(self, openings):
        '''VIEW OPENINGS'''
        try:
            for i in openings.keys():
                logging.info(f'opening for {i} at {openings[i]} location')
        except Exception as e:
            logging.error(e)

    def view_affliate(self, affliate):
        '''VIEW AFFLIATE ID'''
        try:
            logging.info(f'your affliate id {affliate} was registered')
        except Exception as e:
            logging.error(e)

    def view_internship(self, internship):
        '''VIEW INTERNSHIP'''
        try:
            logging.info(f'{internship} was listed in internship program')
        except Exception as e:
            logging.error(e)

    def view_neuron_type(self, neuron_type):
        '''VIEW NEURON TYPE INFO'''
        try:
            logging.info('Viewing Neuron Type')
            logging.info(f'{neuron_type} was listed')
        except Exception as e:
            logging.error(e)

    def view_course(self, course):
        '''VIEW COURSE DATA'''
        try:
            logging.info('Viewing Course library')
            logging.info(f'{course}')
        except Exception as e:
            logging.error(e)
