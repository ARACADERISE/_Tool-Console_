import time, shelve
from colorama import Fore, Style

LINK = {}
_type_ = [['type=', 'project_link']]

def transfer(info):
  ap_info = [].append(info)
  _trans_ = shelve.open('transfered_info.json.txt')
  _trans_['info'] = str(ap_info)

def get_(proj_name, link):

  time.sleep(3)
  print(Fore.RED + 'Fetching Information For ' + proj_name + '...')

  time.sleep(5)
  print('Getting Link For ' + proj_name + '...')

  try:
    LINK.update({'link': link})
    _type_.append(LINK)
    transfer(_type_)
  except:
    print('Error getting..transfering..and storing link')

  time.sleep(6)
  print('Scanning Steps For ' + proj_name + '....')

  time.sleep(8)
  print('One more moment...')
  time.sleep(3.6)
