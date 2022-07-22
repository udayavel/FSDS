import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


# example 1 - polymorphism
class home:

    def __init__(self, home_title):
        self.home_title = home_title

    def view_home(self):
        '''VIEW HOME DATA'''
        try:
            logging.info(f'{self.home_title}')
        except Exception as e:
            logging.error(e)


class home_view:

    def view_home(self):
        '''VIEW HOME UI'''
        try:
            logging.info('Viewing Home data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_home()
    except Exception as e:
        logging.error(e)


logging.info('******************************************POLYMORPHISM*****************************************')
logging.info('polymorphism example #1')
home_obj = home('Home Dashboard')
create_obj(home_obj)
home_view_obj = home_view()
create_obj(home_view_obj)


# example 2 - polymorphism
class one_neuron:

    def __init__(self, one_neuron_title):
        self.one_neuron_title = one_neuron_title

    def view_one_neuron(self):
        '''VIEW ONE NEURON DATA'''
        try:
            logging.info(f'{self.one_neuron_title}')
        except Exception as e:
            logging.error(e)


class one_neuron_view:

    def view_one_neuron(self):
        '''VIEW ONE NEURON UI'''
        try:
            logging.info('Viewing One Neuron data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_one_neuron()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #2')
one_neuron_obj = one_neuron('One Neuron Dashboard')
create_obj(one_neuron_obj)
one_neuron_view_obj = one_neuron_view()
create_obj(one_neuron_view_obj)


# example 3 - polymorphism
class your_collection:

    def __init__(self, your_collection_title):
        self.your_collection_title = your_collection_title

    def view_your_collection(self):
        '''VIEW COURSE COLLECTION'''
        try:
            logging.info(f'{self.your_collection_title}')
        except Exception as e:
            logging.error(e)


class your_collection_view:

    def view_your_collection(self):
        '''COURSE COLLECTION UI'''
        try:
            logging.info('Viewing Your Collection data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_your_collection()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #3')
your_collection_obj = your_collection('Your Collection Dashboard')
create_obj(your_collection_obj)
your_collection_view_obj = your_collection_view()
create_obj(your_collection_view_obj)


# example 4 - polymorphism
class road_maps:

    def __init__(self, road_maps_title):
        self.road_maps_title = road_maps_title

    def view_road_maps(self):
        '''VIEW ROAD MAP DATA'''
        try:
            logging.info(f'{self.road_maps_title}')
        except Exception as e:
            logging.error(e)


class road_maps_view:

    def view_road_maps(self):
        '''VIEW ROAD MAP UI'''
        try:
            logging.info('Viewing Home data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_road_maps()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #4')
road_maps_obj = road_maps('Raod Maps Dashboard')
create_obj(road_maps_obj)
road_maps_view_obj = road_maps_view()
create_obj(road_maps_view_obj)


# example 5 - polymorphism
class what_next:

    def __init__(self, what_next_title):
        self.what_next_title = what_next_title

    def view_what_next(self):
        '''VIEW WHAT NEXT DATA'''
        try:
            logging.info(f'{self.what_next_title}')
        except Exception as e:
            logging.error(e)


class what_next_view:

    def view_what_next(self):
        '''VIEW WHAT NEXT UI'''
        try:
            logging.info('Viewing What Next data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_what_next()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #5')
what_next_obj = what_next('What Next Dashboard')
create_obj(what_next_obj)
what_next_view_obj = what_next_view()
create_obj(what_next_view_obj)


# example 6 - polymorphism
class challenges:

    def __init__(self, challenges_title):
        self.challenges_title = challenges_title

    def view_challenges(self):
        '''VIEW CHALLENGES DATA'''
        try:
            logging.info(f'{self.challenges_title}')
        except Exception as e:
            logging.error(e)


class challenges_view:

    def view_challenges(self):
        '''VIEW CHALLENGES UI'''
        try:
            logging.info('Viewing Challenges data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_challenges()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #6')
challenges_obj = challenges('Challenges Dashboard')
create_obj(challenges_obj)
challenges_view_obj = challenges_view()
create_obj(challenges_view_obj)


# example 7 - polymorphism
class enroll_one_neuron:

    def __init__(self, enroll_one_neuron_title):
        self.enroll_one_neuron_title = enroll_one_neuron_title

    def view_enroll_one_neuron(self):
        '''VIEW ENROLL ONE NEURON DATA'''
        try:
            logging.info(f'{self.enroll_one_neuron_title}')
        except Exception as e:
            logging.error(e)


class enroll_one_neuron_view:

    def view_enroll_one_neuron(self):
        '''VIEW ENROLL ONE NEURON UI'''
        try:
            logging.info('Viewing Enroll One Neuron data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_enroll_one_neuron()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #7')
enroll_one_neuron_obj = enroll_one_neuron('Enroll One Neuron Dashboard')
create_obj(enroll_one_neuron_obj)
enroll_one_neuron_view_obj = enroll_one_neuron_view()
create_obj(enroll_one_neuron_view_obj)


# example 8 - polymorphism
class course_library:

    def __init__(self, course_library_title):
        self.course_library_title = course_library_title

    def view_course_library(self):
        '''VIEW COURSE LIBRARY DATA'''
        try:
            logging.info(f'{self.course_library_title}')
        except Exception as e:
            logging.error(e)


class course_library_view:

    def view_course_library(self):
        '''VIEW COURSE LIBRARY UI'''
        try:
            logging.info('Viewing Course Library data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_course_library()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #8')
course_library_obj = course_library('Course Library Dashboard')
create_obj(course_library_obj)
course_library_view_obj = course_library_view()
create_obj(course_library_view_obj)


# example 9 - polymorphism
class internship:

    def __init__(self, internship_title):
        self.internship_title = internship_title

    def view_internship(self):
        '''VIEW INTERNSHIP DATA'''
        try:
            logging.info(f'{self.internship_title}')
        except Exception as e:
            logging.error(e)


class internship_view:

    def view_internship(self):
        '''VIEW INTERNSHIP UI'''
        try:
            logging.info('Viewing Internship data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_internship()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #9')
internship_obj = internship('Internship Dashboard')
create_obj(internship_obj)
internship_view_obj = internship_view()
create_obj(internship_view_obj)


# example 10 - polymorphism
class online_ide:

    def __init__(self, online_ide_title):
        self.online_ide_title = online_ide_title

    def view_online_ide(self):
        '''VIEW ONLINE IDE DATA'''
        try:
            logging.info(f'{self.online_ide_title}')
        except Exception as e:
            logging.error(e)


class online_ide_view:

    def view_online_ide(self):
        '''VIEW ONLINE IDE UI'''
        try:
            logging.info('Viewing Online IDE data in the webapge loaded')
        except Exception as e:
            logging.error(e)


def create_obj(obj):
    '''CREATING OBJECT'''
    try:
        return obj.view_online_ide()
    except Exception as e:
        logging.error(e)


logging.info('polymorphism example #10')
online_ide_obj = online_ide('Online IDE Dashboard')
create_obj(online_ide_obj)
online_ide_view_obj = online_ide_view()
create_obj(online_ide_view_obj)
