def greet(name, greeting_template='Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    print(greeting)
    return greeting

# greet('brah','\'Ey <name>!!  Howzit <name>?!  Dakine, <name>?')


def force(mass, body='earth'):
    gravity_solar_system_bodies = {
        'sun': 274.0,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
        }
    gravity = gravity_solar_system_bodies[body]
    gravitational_force = mass * gravity
    return gravitational_force
# 
# 
# solar_system_bodies = ('sun', 'mercury', 'venus', 'earth',
#                        'moon', 'mars', 'jupiter', 'saturn',
#                        'uranus', 'neptune', 'pluto')
# import random
# solar_system_body = solar_system_bodies[random.randint(0, 10)]
# mass_of_object_in_kg = 0.1
# gravitational_force = force(mass_of_object_in_kg,
#                             solar_system_body)
# if solar_system_body in ('sun', 'moon'):
#     solar_system_body_name = F'the {solar_system_body.title()}'
# else:
#     solar_system_body_name = solar_system_body.title() 
#     
# print('The gravitational force on the surface of ' \
#       F'{solar_system_body_name}, exerted on an object ' \
#       F'with a mass of {mass_of_object_in_kg} kg,' \
#       F'is {round(gravitational_force, 2)} N.')


def pull(m1, m2, d):
    G = 6.674e-11   # Gravitational constant [N m^2/kg^2]
    # Gravitational pull as a force expressed in N:
    gravitational_pull = G * ((m1 * m2) / (d ** 2))
    return gravitational_pull


# mass_1_in_kg = 1500
# mass_2_in_kg = 800
# distance_in_m = 3
# 
# gravitational_pull = pull(mass_1_in_kg,
#                           mass_2_in_kg,
#                           distance_in_m)
# 
# if gravitational_pull >= 0.1 and gravitational_pull <= 1000:
#     pull_string = round(gravitational_pull, 2)
# else:
#     pull_string = "{:.2e}".format(gravitational_pull)
# 
# print('The gravitational pull between object 1 ' \
#        F'with a mass of {mass_1_in_kg} kg and ' \
#        F'object 2 with a mass of {mass_2_in_kg} kg, ' \
#        F'and separated by {distance_in_m} m, ' \
#        F'is {pull_string} N.')

