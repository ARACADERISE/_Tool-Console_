import time
from colorama import Fore, Style

# No use, but may help us later...better to declare each as false then declare them as true when we print that we've found the data
https_found = False
github_found = False
user_found = False
filename_found = False

def get_():
  time.sleep(1)
  print(Fore.RED + 'Fetching Information...')
  time.sleep(2)
  print('Got https')
  https_found = True
  time.sleep(1)
  print('Found https://github.com/')
  github_found = True
  time.sleep(5)
  print('Getting github user...')
  time.sleep(3)
  print('Found github user')
  user_found = True
  time.sleep(1)
  print('Fetching file name..')
  time.sleep(4)
  print('Found file name...')
  filename_found = True
  time.sleep(2)
  print('Please wait.....')
  time.sleep(3)
