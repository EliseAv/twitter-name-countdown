"""
Local Settings for a twitter key.
"""

from sys import stdout

# Credentials
MY_CONSUMER_KEY = 'Your Twitter API Consumer Key'
MY_CONSUMER_SECRET = 'Your Consumer Secret Key'
MY_ACCESS_TOKEN_KEY = 'Your Twitter API Access Token Key'
MY_ACCESS_TOKEN_SECRET = 'Your Access Token Secret'

# Target date (use YYYY-MM-DD notation), this is day 0.
TARGET_DATE = '2017-08-25'

# Formats! Use {} to represent the count.
# Max length: 20 chrs'aoeuidhtnspyfgcrlqjk'
BEFORE_TARGET_DATE = 'My name ({} to go)'
DURING_TARGET_DATE = 'My name'
AFTER__TARGET_DATE = 'My name'

# Log settings. Documentation:
# https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'fmt': {'datefmt': '%Y-%m-%d %H:%M:%S',
                           'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'}},
    'handlers': {
        'console': {'class': 'logging.StreamHandler', 'formatter': 'fmt', 'stream': stdout},
        # 'file': {'class': 'logging.handlers.RotatingFileHandler',
        #          'formatter': 'fmt',
        #          'filename': '/tmp/renamer.log',
        #          'maxBytes': 4 * 1024 * 1024,  # 4 MB
        #          'backupCount': 5},
    },
    'loggers': {'renamer': {'handlers': ['console'], 'level': 'INFO'}},
}
