#!/usr/bin/python3

from datetime import date
from logging import getLogger
from logging.config import dictConfig

from dateutil.parser import parse
from twitter import Api, User

import local_settings as config

log = getLogger('renamer')


def main():
    dictConfig(config.LOGGING)
    new_name = choose_name()
    log.info('About to set name: {}'.format(new_name))
    result_user = set_name(new_name)
    log.info('New user name: {}'.format(result_user.name))


def set_name(new_name) -> User:
    api = Api(config.MY_CONSUMER_KEY, config.MY_CONSUMER_SECRET,
              config.MY_ACCESS_TOKEN_KEY, config.MY_ACCESS_TOKEN_SECRET)
    return api.UpdateProfile(name=new_name)


def choose_name():
    then = parse(config.TARGET_DATE).date()
    now = date.today()
    days_in_future = (then - now).days
    if days_in_future == 0:
        name = config.DURING_TARGET_DATE
    elif days_in_future > 0:
        name = config.BEFORE_TARGET_DATE
    else:
        name = config.AFTER__TARGET_DATE
        days_in_future = -days_in_future
    # We have a name, let's format it!
    return name.format(days_in_future)


if __name__ == '__main__':
    main()
