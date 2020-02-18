""" Analytics Toolkit """
import os
import re
import hashlib
import hmac
from datetime import datetime, timedelta
import logging
import nltk
import pandas as pd
import yaml

def read_sql_file(path_to_file):
    """ Loads SQL file as a string.
	Arguments:
	- path_to_file (string): path to sql file from PYTHONPATH
	"""
    full_path = os.path.join(os.environ.get("PYTHONPATH"), path_to_file)
    query = open(full_path, 'r').read()
    return query

def read_yaml_file(path_to_file):
    """ Loads YAML file as a dictionary.
    Arguments:
    - path_to_file (string): path to yaml file from PYTHONPATH
    """
    full_path = os.path.join(os.getenv("PYTHONPATH"), path_to_file)
    with open(full_path, 'r') as file:
        config = yaml.safe_load(file)
    file.close()
    return config

def customer_hash(email):
    """ Hash Email address using sha256 algorithm with salt.
    Parameters:
    email (string): Email address of the customer
    Returns:
    UID (string)
   """
    if "EMAIL_HASH_SALT" in os.environ:
        pass
    else:
        raise KeyError("EMAIL_HASH_SALT does not exist")
    if isinstance(email, str):
        if email != '':
            email = bytes(email.lower(), 'utf-8')
            salt = bytes(os.environ.get("EMAIL_HASH_SALT"), 'utf-8')
            hash_ = hmac.new(key=salt,
                             digestmod=hashlib.sha256)
            hash_.update(email)
            uid = str(hash_.hexdigest())[0:16]
        else:
            uid = '0000000000000000'
        return uid
    elif email is None:
        uid = '0000000000000000'
        return uid
    else:
        raise KeyError("Email argument should be a string")

def stringify(value):
    """
    Returns the string representation of the value.
    """
    if value is None:
        return 'null'
    elif value is True:
        return 'True'
    elif value is False:
        return 'False'
    return str(value)

def is_email_address(text):
    """
    Return true if it is a valid email address
    """
    return re.search(r'[\w\.-]+@[\w\.-]+', text)

def anonymizer(text):
    """
    A part-of-speech tagger, or POS-tagger, processes a sequence
    of words, and attaches a part of speech tag to each word. See
    https://www.nltk.org/index.html for more information.
    """
    if text is None or text == "":
        new_text = text
    else:
        new_text = []
        # Splits text into sentences
        sentence_list = text.replace('\n', ' ').split(". ")
        for sentence in sentence_list:
            # Splits sentence into list of words and filters empty elts.
            # Not using nltk.word_tokenize as it splits an email address
            # in several entities.
            word_list = list(filter(None, sentence.split(" ")))
            # process word_list
            pos = nltk.pos_tag(word_list)
            new_word_list = []
            for word in pos:
                if is_email_address(word[0]):
                    # tags word as EMAIL
                    new_word_list.append("{EMAIL}")
                elif word[1] == 'NNP':
                    # tags word as NAME (proper noun)
                    new_word_list.append("{NAME}")
                elif word[1] == 'CD':
                    # tags word as NUMBER
                    new_word_list.append("{NUMBER}")
                else:
                    # no tranformation
                    new_word_list.append(word[0])
            new_sentence = " ".join(new_word_list)
            new_text.append(new_sentence)
        new_text = ". ".join(new_text)
    return new_text

def get_yesterday_date():
    """
    Returns yesterday date in string format ('%Y-%m-%d')
    """
    return (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

def date_lister(start_date, end_date):
    """
     Returns list of dates between start_date and end_date in string format ('%Y-%m-%d')
     Arguments:
     - start_date (string)
     - end_date (string)
     """
    if end_date < start_date:
        date_list = []
        logging.error("End date must be equal or after start_date")
    else:
        date_list = pd.date_range(start_date, end_date)
        date_list = date_list.format()
        logging.info(date_list)
    return date_list

def validate_date(date_text, format='%Y-%m-%d', error_msg=None):
    try:
        datetime.strptime(date_text, format)
    except ValueError:
        if error_msg is None:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        else:
            raise ValueError(error_msg)
