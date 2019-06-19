# import colorama
from colorama import Fore, Style
import time
from packages import _leave_, _t_, leave_term

# ENDS THE SERVER PORT
def leave_port():

  _i_ = []
  _ap_ = []

  time.sleep(3)
  print(Fore.RED + '   Ending Server Port...')

  _ap_ = ['server port ending']
  _i_.append(_ap_)

  time.sleep(2)
  print('     Server port ended..')

  _ap_ = ['port has ended']
  _i_.append(_ap_)

  time.sleep(3)
  print('       Dumping Server Port Info...')

  _ap_ = ['getting server port info']
  _i_.append(_ap_)

  time.sleep(9)
  print('         Collecting Time Info...')

  _ap_ = ['getting time info']
  _i_.append(_ap_)

  time.sleep(7)
  print('           Creating User Data Files...')

  _ap_ = ['creating user data files']
  _i_.append(_ap_)

  time.sleep(11)
  print('           Exiting..')

  _ap_ = ['leaving project']
  _i_.append(_ap_)
  _leave_(_i_)
  
  time.sleep(2.5)
  print(Fore.WHITE + '         ᑢ ᓍ ᘻ ᘿ  ᗷᗩᑢᖽᐸ  ᗩ ᘜ ᗩ ᓰ ᘉ  !')

def exit_terminal():

  info = {}

  time.sleep(5)
  print(Fore.RED + '\nEnding Terminal....')
  info.update({'_1_': 'ending_terminal'})
  time.sleep(8)
  print('  Re-Locating Server...')
  info.update({'_2_': 'connecting_back_with_server'})
  time.sleep(12)
  print('    Please wait while the terminal shuts down')
  info.update({'_3_': 'shutting_down_terminal'})
  time.sleep(15)
  leave_term(info)
