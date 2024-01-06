import argparse
import collections
import configparser
import hashlib
from datetime import datetime
import grp, pwd
import os
from math import ceil
import re
import sys
import zlib
from fnmatch import fnmatch

argparser = argparse.ArgumentParser(description="The stupid content tracker")



