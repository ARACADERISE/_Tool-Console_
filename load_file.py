import time
# import colorama
from colorama import Fore, Style

def load_():

  loading_file = True

  while loading_file:
    time.sleep(1.5)
    print(Fore.MAGENTA + 'Loading...')
    time.sleep(0.5)
    print('  Getting...')
    time.sleep(3)
    print('    Fetching...')
    time.sleep(1)
    print('File Loaded...\n\n')
    time.sleep(1)

    # GIVING THE VALUE OF LOADING_FILE FALSE DUE TO THE FACT THE ABOVE CODE HAS ALREADY EXECUTED
    loading_file = False

  # NOW THAT THE FILE IS LOADED WE WILL CARRY ON WITH EXECUTING THE MADE BY LOOP ALONG WITH Your Name: 
  while not loading_file:
    # ALERTING WHO PROJECT IS MADE BY
    time.sleep(0.3)
    print(Fore.GREEN + 'ＭＡＤＥ　ＢＹ：　ＡＲＡＣＡＤＥ_ＲＩＳＥ\n')
    time.sleep(0.5)
    break

def port_l(p):
  time.sleep(1)
  print('\nLoading Port ' + p + '...')
  time.sleep(3)
  print('Adapting port ' + p + '...')
  time.sleep(5)
  print('Port ' + p + ' loaded, you are now server port ' + p)
  time.sleep(3)

# CORRUPT, NOT USED
def _port_used_(p):
  print(Fore.YELLOW + '\nYour port is ' + p + '\n')
