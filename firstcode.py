import re
import os
import openai
import textwrap
from time import time,sleep
from pprint import pprint

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
      return infile.read()

openai.api_key = open_file("C:/Work/GPT3/openaiapikey.txt") 
#openai.api_key = "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"


print(openai.api_key)

# Just to see the changes in Git