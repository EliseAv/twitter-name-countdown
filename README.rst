======================
Twitter Name Countdown
======================

Quick renamer that I put together to count down for cons such as BronyCAN. Yay.

I run it in my Raspberry Pi.


Install
-------

::

    sudo apt-get install python3 python3-pip git
    git clone https://github.com/ekevoo/twitter-name-countdown.git
    cd twitter-name-countdown
    sudo pip3 install -r requirements.txt


Configure
---------

1. Copy ``local_settings_example.py`` to a new file called ``local_settings.py``
2. Go to `Twitter Apps`_ and create a new app called **Name Countdown**.

   a. In **Application Settings** click **manage keys and access tokens**.
   b. Copy API Key and API Secret over to your local settings file.
   c. Scroll down to generate a new access token.
   d. Copy Token and Token Secret over to your local settings file.

3. Set the target date, using ISO format (YYYY-MM-DD).
4. Choose the names you wish to have before, during, and after target date.

.. _Twitter Apps: https://apps.twitter.com/


Run
---

Test it once by running: ``./renamer.py``

If it's good, run the following command to schedule it to run every midnight::

    (crontab -l 2>/dev/null; echo "0 0 * * * /usr/bin/python3 /home/pi/twitter-name-countdown/renamer.py") | crontab -

Aaand done!
