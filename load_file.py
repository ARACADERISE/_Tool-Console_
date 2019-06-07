import time
# import colorama
from colorama import Fore, Style, Back
from random import randint

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
    print(Fore.BLUE + Style.BRIGHT + '''
         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         
         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         
         ¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶___¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶         
         ¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶         
         ¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶______¶¶¶_¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶         
         ¶¶¶¶¶___¶¶¶¶¶¶¶¶¶_______________________¶¶¶¶¶         
         ¶¶¶¶__¶¶¶¶¶¶¶¶¶_________¶¶________¶¶¶¶¶__¶¶¶¶         
         ¶¶¶__¶¶¶¶¶¶¶¶¶¶_________________¶¶¶¶¶¶¶¶__¶¶¶         
         ¶¶__¶¶¶¶¶¶¶¶¶¶¶_____________¶¶¶__¶¶¶¶¶¶¶¶__¶¶         
         ¶¶_¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶_¶¶         
         ¶__¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶         
         ¶_¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶         
         ¶_¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶         
         ¶_¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶         
         ¶_¶¶¶¶¶¶¶¶¶¶¶_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶         
         ¶_¶¶¶¶¶¶¶¶¶¶¶_____¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶         
         ¶__¶¶¶¶¶¶¶¶¶______¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶         
         ¶¶_¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶         
         ¶¶__¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶         
         ¶¶¶__¶¶¶¶_______¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶__¶¶¶         
         ¶¶¶¶__¶¶_______¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶__¶¶¶¶         
         ¶¶¶¶¶__¶______¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶__¶¶¶¶¶         
         ¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶__¶¶¶¶¶¶¶         
         ¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶___¶¶¶¶¶¶¶¶         
         ¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶         
         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         
         ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         \n\n''')
    time.sleep(1)
    print(Style.RESET_ALL + Fore.GREEN + '_ㄒ  ㄖ  ㄖ  ㄥ  -  匚  ㄖ  几  丂  ㄖ  ㄥ  乇_')
    time.sleep(1.5)
    print('ＭＡＤＥ　ＢＹ：　ＡＲＡＣＡＤＥ_ＲＩＳＥ\n')
    time.sleep(0.5)
    break

def port_l(p):
  time.sleep(4)
  print('\nLoading Port ' + p + '...')
  time.sleep(3.8)
  print('Adapting port ' + p + '...')
  time.sleep(6.5)
  print('Port ' + p + ' loaded, you are now server port ' + p)
  time.sleep(4.8)

# CORRUPT, NOT USED
def _port_used_(p):
  print(Fore.YELLOW + '\nYour port is ' + p + '\n')
