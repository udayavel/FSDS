import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


# example 1 - Single Inheritance

class ineuron_dashboard:

    def __init__(self, menu, title):
        self.title = title
        self.menu = menu

    def get_Meta(self):
        '''LOADING MENU AND TITLE FOR DASHBOARD'''
        try:
            logging.info(f'menu {self.menu} invoked')
            logging.info(f'title {self.title} was invoked')
        except Exception as e:
            logging.error(e)


class one_neuron(ineuron_dashboard):

    def enrollment_status(self, enrolled_courses):
        '''CHECKING ENROLLMENT STATUS OF INEURON'''
        try:
            if 'One Neuron' in enrolled_courses:
                logging.info('one neuron already enrolled')
                return True
            else:
                logging.info('one neuron is not enrolled')
                return False
        except Exception as e:
            logging.error(e)

    def buy_one_neuron(self):
        '''METHOD FOR ONE NEURON PAYMENT'''
        try:
            logging.info('payment is processing...')
            logging.info('one neuron enrolled successfully')
        except Exception as e:
            logging.error(e)


################################################################################################################################################

# example 2 - Multilevel Inheritance

class ineuron_home(one_neuron):

    def play_course(self, playing_course, recent_courses):
        '''PLAYING COURSE'''
        try:
            logging.info(f'{playing_course} course is playing...')
            recent_courses.append(playing_course)
            return recent_courses
        except Exception as e:
            logging.error(e)

    def erolled_course(self, enroll_course, enrolled_courses):
        '''ENROLLING COURSE'''
        try:
            logging.info(f'{enroll_course} course is enrolled')
            enrolled_courses.append(enroll_course)
            return enrolled_courses
        except Exception as e:
            logging.error(e)

    def list_recent_courses(self, recent_courses):
        '''LIST RECENT COURSES'''
        try:
            count = 1
            for course in recent_courses:
                logging.info(f'{count}. {course}')
                count += 1
        except Exception as e:
            logging.error(e)

    def list_enrolled_courses(self, enrolled_courses):
        '''LIST ENROLLED COURSES'''
        try:
            count = 1
            for course in enrolled_courses:
                logging.info(f'{count}. {course}')
                count += 1
        except Exception as e:
            logging.error(e)


################################################################################################################################################

# example 3 - Multilevel Inheritance

class your_collection(ineuron_home):

    def add_to_collection(self, course, collection):
        '''ADD COURSES TO COLLECTION'''
        try:
            logging.info('adding course to the collection')
            collection.append(course)
            return collection
        except Exception as e:
            logging.error(e)

    def view_collection(self, collection):
        '''VIEW COLLECTION OF COURSES'''
        try:
            logging.info('courses in collection')
            count = 1
            for course in collection:
                logging.info(f'{count}. {course}')
                count += 1
        except Exception as e:
            logging.error(e)


################################################################################################################################################
# example 4 - Multiple Inheritance

class roadmap_category:

    def add_road_map_category(self, road_category, category):
        '''ROADMAP CATEGORY UPDATE'''
        try:
            logging.info('adding road map category')
            road_category.append(category)
            return road_category
        except Exception as e:
            logging.error(e)


class sub_road_map:

    def add_sub_roadmap(self, road_sub_category, sub_category):
        '''ROADMAP SUBCATEGORY UPDATE'''
        try:
            logging.info('adding sub road map')
            road_sub_category.append(sub_category)
            return road_sub_category
        except Exception as e:
            logging.error(e)


class road_maps(roadmap_category, sub_road_map):

    def view_road_map_type(self, road_category, road_sub_category):
        '''VIEW ROADMAP TYPES'''
        try:
            logging.info('roadmaps loading....')
            for l, m in zip(road_category, road_sub_category):
                logging.info(f'{l}  :  {m}')
        except Exception as e:
            logging.error(e)


################################################################################################################################################
# example 5 - Multiple Inheritance

class upcoming_courses:

    def __init__(self, course_list, course_month, course_calendar):
        self.course_list = course_list
        self.course_month = course_month
        self.course_calendar = course_calendar

    def add_course(self, course):
        '''ADD COURSE INTO UPCOMING SCHEDULE'''
        try:
            logging.info('adding course into What Next')
            self.course_list.append(course)
        except Exception as e:
            logging.error(e)

    def list_course(self):
        '''LIST SCHEDULED COURSES'''
        try:
            count = 1
            for course in self.course_list:
                logging.info(f'{count}.{course}')
                count += 1
        except Exception as e:
            logging.error(e)


class course_calendar_map(upcoming_courses):

    def add_course_calendar(self):
        '''ADD COURSE INTO CALENDAR'''
        try:
            logging.info('Adding course to the calendar')
            self.course_calendar[self.course_month] = self.course_list
        except Exception as e:
            logging.error(e)

    def list_course_calendar(self):
        '''LIST COURSES WITH MONTH SCHEDULED'''
        try:
            for i in self.course_calendar.keys():
                logging.info(f'Month {i} having Courses {self.course_calendar[i]} scheduled in calendar')
        except Exception as e:
            logging.error(e)


################################################################################################################################################
# example 6 - Single Inheritance

class tech_neuron(ineuron_dashboard):

    def add_challenge(self, challenge_name, challenges_neuron):
        '''ADD NEW CHALLENGES TO CHALLENGE PAGE'''
        try:
            logging.info('adding new challenges')
            challenges_neuron.append(challenge_name)
            return challenges_neuron
        except Exception as e:
            logging.error(e)

    def view_challenge(self, challenges_neuron):
        '''VIEW AVAILABLE CHALLENGES'''
        try:
            logging.info('Challenges added in Challenge section')
            count = 1
            for chal in challenges_neuron:
                logging.info(f'{count}.{chal}')
                count += 1
        except Exception as e:
            logging.error(e)


################################################################################################################################################
# example 7 - Single Inheritance

class tech_neuron_dashboard:

    def __init__(self, menu, tech_course):
        self.menu = menu
        self.tech_course = tech_course

    def load_status(self):
        '''LOADING DASHBOARD STATUS'''
        try:
            logging.info('Tech neuron Page is loading.......')
        except Exception as e:
            logging.error(e)

    def courses_available(self):
        '''AVAILABLE COURSE IN TECH NEURON'''
        try:
            logging.info('Available courses in Tech neuron page')
            for course in self.tech_course:
                logging.info(f'{course}')
        except Exception as e:
            logging.error(e)


class course_search(tech_neuron_dashboard):

    def tech_course_search(self, course):
        'COURSE SEARCH FROM DASHBOARD'
        try:
            for i in self.tech_course:
                if (i == course):
                    logging.info('course found :)')
                    break
        except Exception as e:
            logging.error(e)


################################################################################################################################################

# example 8 - Single Inheritance
class home_data:

    def __init__(self, home_title):
        self.home_title = home_title

    def view_home(self):
        '''VIEW HOME DASHBOARD'''
        try:
            logging.info(f'{self.home_title}')
        except Exception as e:
            logging.error(e)


class home_view(home_data):

    def view_home(self):
        '''VIEW HOME UI'''
        try:
            logging.info('Viewing Home data in the webapge loaded')
        except Exception as e:
            logging.error(e)


################################################################################################################################################

# example 9 - Single Inheritance
class one_neuron_data:

    def __init__(self, one_neuron_title):
        self.one_neuron_title = one_neuron_title

    def view_one_neuron(self):
        '''VIEW ONE NEURON'''
        try:
            logging.info(f'{self.one_neuron_title}')
        except Exception as e:
            logging.error(e)


class one_neuron_view(one_neuron_data):

    def view_one_neuron(self):
        '''VIEW ONE NEURON UI'''
        try:
            logging.info('Viewing One Neuron data in the webapge loaded')
        except Exception as e:
            logging.error(e)


################################################################################################################################################


# example 10 - Single Inheritance
class your_collection_data:

    def __init__(self, your_collection_title):
        self.your_collection_title = your_collection_title

    def view_your_collection(self):
        '''VIEW COURSE COLLECTION'''
        try:
            logging.info(f'{self.your_collection_title}')
        except Exception as e:
            logging.error(e)


class your_collection_view(your_collection_data):

    def view_your_collection(self):
        '''VIEW SPECIFIC COLLECTION'''
        try:
            logging.info('Viewing Your Collection data in the webapge loaded')
        except Exception as e:
            logging.error(e)


################################################################################################################################################

# MENU ITEM
option = 0
recent_courses = []
enrolled_courses = []
collection = []
road_map_category = []
course_library = ['DATA SCIENCE', 'PROGRAMMING', 'DEVELOPMENT', 'CLOUD', 'MARKETING']
course_number = 0
road_category = []
road_sub_category = []
course_calendar = {}
challenges_neuron = []
try:
    logging.info('******************************************INHERITANCE******************************************')
    while option != 9:
        logging.info('******************************************MENU******************************************')
        logging.info('1. HOME')
        logging.info('2. ONE NEURON')
        logging.info('3. YOUR COLLECTION')
        logging.info('4. ROAD MAPS')
        logging.info("5. WHAT'S NEXT")
        logging.info('6. CHALLENGES')
        logging.info('7. TECH NEURON')
        logging.info('8. OTHERS')
        logging.info('9. EXIT')
        option = int(input('Enter your choice'))
        if option == 1:
            logging.info('Inheritance example #1')
            logging.info('HOME is choosed from the menu')
            home = ineuron_home('HOME', 'Course Details')
            home.get_Meta()
            logging.info('choose course order number to enroll')
            course_number = int(input('choose course order number to enroll'))
            logging.info(f'course order number choosed {course_number} from {course_library}')
            if course_library[course_number - 1] in enrolled_courses:
                logging.info(f'{course_library[course_number - 1]} course already enrolled')
            else:
                enrolled_courses = home.erolled_course(course_library[course_number - 1], enrolled_courses)
                logging.info('enrolled courses')
                home.list_enrolled_courses(enrolled_courses)
            if len(enrolled_courses) > 0:
                logging.info(f'enrolled course count {len(enrolled_courses)}')
                logging.info('choose course order number within enrolled length to play / enter 0 if play not required')
                course_number = int(input(f'choose course order number to play within {len(enrolled_courses)}'))
                logging.info(f'course order number choosed {course_number} from {enrolled_courses}')
                if course_number == 0:
                    pass
                else:
                    recent_courses = home.play_course(enrolled_courses[course_number - 1], recent_courses)
                    logging.info('recent courses')
                    home.list_recent_courses(recent_courses)
        elif option == 2:
            logging.info('Inheritance example #2')
            logging.info('ONE NEURON is choosed from the menu')
            one = one_neuron('ONE NEURON', 'One Neuron Enrollemnt')
            one.get_Meta()
            logging.info('Checking One Neuron enrollment status....')
            if (one.enrollment_status(enrolled_courses)):
                pass
            else:
                logging.info('press e to enroll the course')
                if (input('press E to enroll the course') == 'e'):
                    one.buy_one_neuron()
                    enrolled_courses.append('One Neuron')
                else:
                    logging.info('one neuron is not enrolled')
        elif option == 3:
            logging.info('Inheritance example #3')
            logging.info('YOUR COLLECTION is choosed from the menu')
            collect = your_collection('YOUR COLLECTION', 'Collections')
            collect.get_Meta()
            collect.list_enrolled_courses(enrolled_courses)
            logging.info(f'choose course number from the enrolled course to add into collection')
            course_number = int(input(f'choose course number from {enrolled_courses} to add into collection'))
            collection = collect.add_to_collection(enrolled_courses[course_number - 1], collection)
            logging.info(f'choose course number from {enrolled_courses} to add into collection')
            collect.view_collection(collection)
        elif option == 4:
            logging.info('Inheritance example #4')
            logging.info('ROADMAP is choosed from the menu')
            roadmap = road_maps()
            category = input('Enter Roadmap category')
            road_category = roadmap.add_road_map_category(road_category, category)
            subcategory = input('Enter Roadmap Sub category')
            road_sub_category = roadmap.add_sub_roadmap(road_sub_category, subcategory)
            roadmap.view_road_map_type(road_category, road_sub_category)
        elif option == 5:
            logging.info('Inheritance example #5')
            logging.info('WHAT NEXT is choosed from the menu')
            course = input('Enter month Name')
            wn = course_calendar_map(['DATA SCIENCE', 'DATA STRUCTURES', 'BI'], course, course_calendar)
            wn.add_course('PROGRAMMING')
            wn.list_course()
            wn.add_course_calendar()
            wn.list_course_calendar()
        elif option == 6:
            logging.info('Inheritance example #6')
            logging.info('CHALLENGES is choosed from the menu')
            challenge = tech_neuron('CHALLENGES', 'Course-A-Thon')
            challenge.get_Meta()
            challenge_name = input('Enter the challenge name ')
            challenges_neuron = challenge.add_challenge(challenge_name, challenges_neuron)
            challenge.view_challenge(challenges_neuron)
        elif option == 7:
            logging.info('Inheritance example #7')
            logging.info('TECH NEURON is choosed from the menu')
            tech_neu = course_search('CHALLENGES', ['DATA SCIENCE', 'JAVASCRIPT', 'AUTOMATION', 'TESTING'])
            tech_neu.load_status()
            tech_neu.courses_available()
            course_neu = input('Enter course to search from ')
            tech_neu.tech_course_search(course_neu)
        elif option == 8:
            logging.info('OTHERS is choosed from the menu')
            logging.info('Inheritance example #8')
            home_obj = home_data('Home Dashboard')
            home_view_obj = home_view('Home Dashboard')
            home_obj.view_home()
            home_view_obj.view_home()
            logging.info('Inheritance example #9')
            one_neuron_obj = one_neuron_data('One Neuron Dashboard')
            one_neuron_obj.view_one_neuron()
            one_neuron_view_obj = one_neuron_view('One Neuron Dashboard')
            one_neuron_view_obj.view_one_neuron()
            logging.info('Inheritance example #10')
            your_collection_obj = your_collection_data('Your Collection Dashboard')
            your_collection_obj.view_your_collection()
            your_collection_view_obj = your_collection_view('Your Collection Dashboard')
            your_collection_view_obj.view_your_collection()
except Exception as e:
    logging.error(e)
