import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


# example 1 - method overriding
class home:

    def __init__(self, home_title):
        self.home_title = home_title

    def view_home(self):
        '''VIEW HOME'''
        try:
            logging.info(f'{self.home_title}')
        except Exception as e:
            logging.error(e)


class home_view(home):

    def view_home(self):
        '''VIEW HOME DASHBOARD UI'''
        try:
            logging.info('Viewing Home data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('******************************************METHOD OVERRIDING******************************************')
logging.info('method overriding example #1')
home_obj = home('Home Dashboard')
home_view_obj = home_view('Home Dashboard')
home_obj.view_home()
home_view_obj.view_home()


# example 2 - method overriding
class one_neuron:

    def __init__(self, one_neuron_title):
        self.one_neuron_title = one_neuron_title

    def view_one_neuron(self):
        '''VIEW ONE NEURON DATA'''
        try:
            logging.info(f'{self.one_neuron_title}')
        except Exception as e:
            logging.error(e)


class one_neuron_view(one_neuron):

    def view_one_neuron(self):
        '''VIEW ONE NEURON UI'''
        try:
            logging.info('Viewing One Neuron data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #2')
one_neuron_obj = one_neuron('One Neuron Dashboard')
one_neuron_obj.view_one_neuron()
one_neuron_view_obj = one_neuron_view('One Neuron Dashboard')
one_neuron_view_obj.view_one_neuron()


# example 3 - method overriding
class your_collection:

    def __init__(self, your_collection_title):
        self.your_collection_title = your_collection_title

    def view_your_collection(self):
        '''VIEW COURSE COLLECTION DATA'''
        try:
            logging.info(f'{self.your_collection_title}')
        except Exception as e:
            logging.error(e)


class your_collection_view(your_collection):

    def view_your_collection(self):
        '''VIEW COURSE COLLECTION UI'''
        try:
            logging.info('Viewing Your Collection data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #3')
your_collection_obj = your_collection('Your Collection Dashboard')
your_collection_obj.view_your_collection()
your_collection_view_obj = your_collection_view('Your Collection Dashboard')
your_collection_view_obj.view_your_collection()


# example 4 - method overriding
class road_maps:

    def __init__(self, road_maps_title):
        self.road_maps_title = road_maps_title

    def view_road_maps(self):
        '''VIEW ROADMAPS DATA'''
        try:
            logging.info(f'{self.road_maps_title}')
        except Exception as e:
            logging.error(e)


class road_maps_view(road_maps):

    def view_road_maps(self):
        '''VIEW ROAD MAPS UI'''
        try:
            logging.info('Viewing Home data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #4')
road_maps_obj = road_maps('Raod Maps Dashboard')
road_maps_obj.view_road_maps()
road_maps_view_obj = road_maps_view('Raod Maps Dashboard')
road_maps_view_obj.view_road_maps()


# example 5 - method overriding
class what_next:

    def __init__(self, what_next_title):
        self.what_next_title = what_next_title

    def view_what_next(self):
        '''VIEW WHAT NEXT DATA'''
        try:
            logging.info(f'{self.what_next_title}')
        except Exception as e:
            logging.error(e)


class what_next_view(what_next):

    def view_what_next(self):
        '''WHAT NEXT UI'''
        try:
            logging.info('Viewing What Next data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #5')
what_next_obj = what_next('What Next Dashboard')
what_next_obj.view_what_next()
what_next_view_obj = what_next_view('What Next Dashboard')
what_next_view_obj.view_what_next()


# example 6 - method overriding
class challenges:

    def __init__(self, challenges_title):
        self.challenges_title = challenges_title

    def view_challenges(self):
        '''VIEW CHALLENGES DATA'''
        try:
            logging.info(f'{self.challenges_title}')
        except Exception as e:
            logging.error(e)


class challenges_view(challenges):

    def view_challenges(self):
        '''VIEW CHALLENGES UI'''
        try:
            logging.info('Viewing Challenges data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #6')
challenges_obj = challenges('Challenges Dashboard')
challenges_obj.view_challenges()
challenges_view_obj = challenges_view('Challenges Dashboard')
challenges_view_obj.view_challenges()


# example 7 - method overriding
class enroll_one_neuron:

    def __init__(self, enroll_one_neuron_title):
        self.enroll_one_neuron_title = enroll_one_neuron_title

    def view_enroll_one_neuron(self):
        '''VIEW ENROLL ONE NEURON DATA'''
        try:
            logging.info(f'{self.enroll_one_neuron_title}')
        except Exception as e:
            logging.error(e)


class enroll_one_neuron_view(enroll_one_neuron):

    def view_enroll_one_neuron(self):
        '''VIEW ENROLL ONE NEURON UI'''
        try:
            logging.info('Viewing Enroll One Neuron data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #7')
enroll_one_neuron_obj = enroll_one_neuron('Enroll One Neuron Dashboard')
enroll_one_neuron_obj.view_enroll_one_neuron()
enroll_one_neuron_view_obj = enroll_one_neuron_view('Enroll One Neuron Dashboard')
enroll_one_neuron_view_obj.view_enroll_one_neuron()


# example 8 - method overriding
class course_library:

    def __init__(self, course_library_title):
        self.course_library_title = course_library_title

    def view_course_library(self):
        '''VIEW COURSE LIBRARY DATA'''
        try:
            logging.info(f'{self.course_library_title}')
        except Exception as e:
            logging.error(e)


class course_library_view(course_library):

    def view_course_library(self):
        '''VIEW COURSE LIBRARY UI'''
        try:
            logging.info('Viewing Course Library data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #8')
course_library_obj = course_library('Course Library Dashboard')
course_library_obj.view_course_library()
course_library_view_obj = course_library_view('Course Library Dashboard')
course_library_view_obj.view_course_library()


# example 9 - method overriding
class internship:

    def __init__(self, internship_title):
        self.internship_title = internship_title

    def view_internship(self):
        '''VIEW INTERNSHIP DATA'''
        try:
            logging.info(f'{self.internship_title}')
        except Exception as e:
            logging.error(e)


class internship_view(internship):

    def view_internship(self):
        '''VIEW INTERNSHIP UI'''
        try:
            logging.info('Viewing Internship data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #9')
internship_obj = internship('Internship Dashboard')
internship_obj.view_internship()
internship_view_obj = internship_view('Internship Dashboard')
internship_view_obj.view_internship()


# example 10 - method overriding
class online_ide:

    def __init__(self, online_ide_title):
        self.online_ide_title = online_ide_title

    def view_online_ide(self):
        '''VIEW ONLINE IDE DATA'''
        try:
            logging.info(f'{self.online_ide_title}')
        except Exception as e:
            logging.error(e)


class online_ide_view(online_ide):

    def view_online_ide(self):
        '''VIEW ONLINE IDE UI'''
        try:
            logging.info('Viewing Online IDE data in the webapge loaded')
        except Exception as e:
            logging.error(e)


logging.info('method overriding example #10')
online_ide_obj = online_ide('Online IDE Dashboard')
online_ide_obj.view_online_ide()
online_ide_view_obj = online_ide_view('Online IDE Dashboard')
online_ide_view_obj.view_online_ide()
