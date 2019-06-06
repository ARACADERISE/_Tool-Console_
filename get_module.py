import time
from colorama import Fore, Style
# This will print "Getting.." when module targeted
def get_():
  time.sleep(1)
  print(Fore.RED + 'Fetching Information...')
  time.sleep(2)
  print('Got https')
  time.sleep(1)
  print('Found https://github.com/')
  time.sleep(5)
  print('Getting github user...')
  time.sleep(3)
  print('Found github user')
  time.sleep(1)
  print('Fetching file name..')
  time.sleep(4)
  print('Found file name...')
  time.sleep(2)
  print('Please wait.....')
  time.sleep(3)
