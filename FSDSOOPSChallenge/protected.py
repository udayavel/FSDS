import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')


# Example 1 - public

class courses:

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self._course_name = course_name

    def view_course(self):
        '''VIEW COURSE REGISTRATION'''
        try:
            logging.info(f'{self._course_name} was registered successfully')
        except Exception as e:
            logging.error(e)


logging.info('******************************************PROTECTED******************************************')
logging.info('protected Example # 1')
cou = courses('ML1234', 'Data Science')
cou.view_course()


# Example 2 - public

class course_library:

    def __init__(self, course_names):
        self._course_names = course_names

    def view_course(self):
        '''VIEW COURSE LIST'''
        try:
            logging.info('Course list')
            for i in self._course_names:
                logging.info(i)
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 2')
cou = course_library(['Data Science', 'Data Structures', 'Programming'])
cou.view_course()


# Example 3 - public

class categories:

    def __init__(self, category_list):
        self._category_list = category_list

    def view_category(self):
        '''VIEW CATEGORY LIST'''
        try:
            logging.info('Category list')
            for i in self._category_list:
                logging.info(i)
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 3')
cat = categories(['Data Science', 'Programming', 'Development', 'Cloud', 'Marketing'])
cat.view_category()


# Example 4 - public

class sub_topic:

    def __init__(self, topic_id, topic_name):
        self.topic_id = topic_id
        self._topic_name = topic_name

    def view_course(self):
        '''VIEW COURSE TOPIC INFO'''
        try:
            logging.info(f'{self._topic_name} topic was confirmed with ID {self.topic_id}')
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 4')
st = sub_topic('TP1234', 'FULL STACK DEVELOPMENT')
st.view_course()


# Example 5 - public

class instructor:

    def __init__(self, instructor_list):
        self._instructor_list = instructor_list

    def view_instructor(self):
        '''VIEW INSTRUCTOR DATA'''
        try:
            for i in self._instructor_list:
                logging.info(f'{i}')
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 5')
ins = instructor(['Ankur Khanna', 'Sourangshu Paul', 'Sunny Bhaveen Chandra'])
ins.view_instructor()


# Example 6 - public

class language:

    def __init__(self, language_list):
        self._language_list = language_list

    def view_language(self):
        '''VIEW COURSE LANGUAGES'''
        try:
            for i in self._language_list:
                logging.info(f'{i}')
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 6')
lan = language(['English', 'Hindi', 'German'])
lan.view_language()


# Example 7 - public

class job_guaranteed_program:

    def __init__(self, program_names):
        self._program_names = program_names

    def view_program(self):
        '''VIEW PROGRAM INFO'''
        try:
            for i in self._program_names:
                logging.info(f'{i}')
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 7')
job = job_guaranteed_program(['FULL STACK DATA SCIENCE', 'JAVASCRIPT'])
job.view_program()


# Example 8 - public

class course_filter:

    def __init__(self, course_list):
        self._course_list = course_list

    def filter_course(self, course_name):
        '''FILTER COURSE'''
        try:
            for i in self._course_list:
                if i == course_name:
                    logging.info(f'{course_name} searching done')
                    break
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 8')
cf = course_filter(['Data Science', 'Data Structures', 'Javascript', 'Web Automation'])
cf.filter_course('Data Structures')


# Example 9 - public

class ineuron_vision:

    def __init__(self, products):
        self._products = products

    def view_products(self):
        '''VIEW INEURON PRODUCTS'''
        try:
            logging.info(f'{self._products}')
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 9')
iv = ineuron_vision(['Apparael Detection', 'Consumption Prediction', 'Bible Author Prediction'])
iv.view_products()


# Example 10 - public

class stories:

    def __init__(self, story_list):
        self._story_list = story_list

    def view_stories(self):
        '''VIEW STORIES'''
        try:
            for i in self._story_list:
                logging.info(f'{i}')
        except Exception as e:
            logging.error(e)


logging.info('protected Example # 10')
story = stories(['story 1', 'story 2', 'story 3'])
story.view_stories()
