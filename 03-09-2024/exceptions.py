import logging

logging.basicConfig(filename= "logging_errors.log", level = logging.DEBUG)

dividend = 15
divisor = 0

try:
    premedatio_malorum = dividend / divisor
except ZeroDivisionError:
    logging.exception("We tried to divide between 0")
    logging.debug(f"Try to change the divisor ({divisor}) variable", stack_info = True, stacklevel = 0)
    logging.info("Did you know the Mayans created the zero?")

location_of = {"mind" : "brain", "heart" : "chest"}

try:
    where_is_the_soul = location_of["soul"]
except KeyError:
    logging.exception("We haven't found where the soul is located yet")
    logging.critical("Don't succumb into nihilism yet!")