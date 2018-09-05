#!/usr/bin/python3
import subprocess
import re
import time
import math
import random
import json
import requests
import decimal
from decimal import (Decimal, ROUND_DOWN)
#import apim
#import sqlite3
import urllib
import MySQLdb
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('/root/dismona.conf')

section1 = 'development'
walletpassphrase = config.get(section1, 'mona_walletpassphrase')
db_user = config.get(section1, 'db_user')
db_password = config.get(section1, 'db_password')
db_host = config.get(section1, 'db_host')
db_name = config.get(section1, 'db_name')
electrum_wallet_location = config.get(section1, 'electrum_wallet_location')
