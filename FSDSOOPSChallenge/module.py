import logging

logging.basicConfig(filename='oops.log', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

logging.info('******************************************MODULE******************************************')
# example 1 package

import oops_package.package_ex as md

logging.info('Module example #1')
try:
    md.ineuron().access_hof()
except Exception as e:
    logging.error(e)

# example 2 package

import oops_package.package_ex as md

logging.info('Module example #2')
try:
    md.ineuron().view_assignment_analytics(10)
except Exception as e:
    logging.error(e)

# example 3 package

import oops_package.package_ex as md

logging.info('Module example #3')
try:
    md.ineuron().view_analytics(7)
except Exception as e:
    logging.error(e)

# example 4 package

import oops_package.package_ex as md

logging.info('Module example #4')
try:
    md.ineuron().view_syllabus(['Python', 'Stats', 'Machine Learning', 'Deep Learning', 'Computer Vision'])
except Exception as e:
    logging.error(e)

# example 5 package

import oops_package.package_ex as md

logging.info('Module example #5')
try:
    md.ineuron().view_achievers(['Microsoft', 'VM Ware', 'Adobe', 'Wipro'])
except Exception as e:
    logging.error(e)

# example 6 package

import oops_package.package_ex as md

logging.info('Module example #6')
try:
    md.ineuron().view_openings({'Business Development Associate': 'Bangalore', 'Senior UI/UX developer': 'Bangalore',
                                'UI/UX developer': 'Bangalore'})
except Exception as e:
    logging.error(e)

# example 7 package

import oops_package.package_ex as md

logging.info('Module example #7')
try:
    md.ineuron().view_affliate('AF23890')
except Exception as e:
    logging.error(e)

# example 8 package

import oops_package.package_ex as md

logging.info('Module example #8')
try:
    md.ineuron().view_internship(['Full Stack Data Science', 'Javascript'])
except Exception as e:
    logging.error(e)

# example 9 package

import oops_package.package_ex as md

logging.info('Module example #9')
try:
    md.ineuron().view_neuron_type(['Tech Neuron', 'Kids Neuron'])
except Exception as e:
    logging.error(e)

# example 10 package

import oops_package.package_ex as md

logging.info('Module example #10')
try:
    md.ineuron().view_course('Data Structures and Algorithms')
except Exception as e:
    logging.error(e)
