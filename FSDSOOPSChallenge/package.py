import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

logging.info('******************************************PACKAGE******************************************')
# example 1 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #1')
    ineuron().access_hof()
except Exception as e:
    logging.error(e)

# example 2 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #2')
    ineuron().view_assignment_analytics(10)
except Exception as e:
    logging.error(e)

# example 3 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #3')
    ineuron().view_analytics(7)
except Exception as e:
    logging.error(e)

# example 4 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #4')
    ineuron().view_syllabus(['Python', 'Stats', 'Machine Learning', 'Deep Learning', 'Computer Vision'])
except Exception as e:
    logging.error(e)

# example 5 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #5')
    ineuron().view_achievers(['Microsoft', 'VM Ware', 'Adobe', 'Wipro'])
except Exception as e:
    logging.error(e)

# example 6 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #6')
    ineuron().view_openings({'Business Development Associate': 'Bangalore', 'Senior UI/UX developer': 'Bangalore',
                             'UI/UX developer': 'Bangalore'})
except Exception as e:
    logging.error(e)

# example 7 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #7')
    ineuron().view_affliate('AF23890')
except Exception as e:
    logging.error(e)

# example 8 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #8')
    ineuron().view_internship(['Full Stack Data Science', 'Javascript'])
except Exception as e:
    logging.error(e)

# example 9 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #9')
    ineuron().view_neuron_type(['Tech Neuron', 'Kids Neuron'])
except Exception as e:
    logging.error(e)

# example 10 package

from oops_package.package_ex import ineuron

try:
    logging.info('Package example #10')
    ineuron().view_course('Data Structures and Algorithms')
except Exception as e:
    logging.error(e)
