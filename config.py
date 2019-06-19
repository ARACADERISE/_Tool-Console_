import shelve
# import json
import datetime
import socket
from colorama import Fore, Style, Back
# import platform
import random
import string
import time

connected = False
est_connection = 'Not_Established'

status = {}

status.update({'Connected': connected, 'Est_Connection': est_connection})


def _not_establish_(connection):

  # This is set to None by default for the fact the database has not connected
  connection_status = {'saved_data': None, 'established_database': False}

  if not connected:
    not_con = []
    str(not_con.append(connection))
    str(not_con.append(connection_status))

    _not_ = shelve.open('not_connected.json.txt')
    _not_['[not_connected]'] = str(not_con)
    _not_.close()

print('\n' + '----' * 13)
print('\nThis project is based off of a database to help it navigate through the code and the users information and what the port info holds. \n\nAs of right now the user MUST accept the fact that we are using a database to store user data. \n\nNOTE: This may change as the project advances but as of right now we are stuck with having the user(you) accept the database connecting to the project. Thanks for understanding!\n')
print('----' * 13)

# The user is forced to connect

def _con_():

  while not connected:

    _not_establish_(status)

    #_r_(status['Est_Connection'])
    print('\nConnection: ' + str(status))
  
    print(Fore.GREEN + '--' * 10)
    c = input('Connect To Database[Y]: ')
    if c == 'Y' or c == 'y':
      time.sleep(6)
      print('\nConnecting..')
      time.sleep(6.5)
      print('  Establishing Connection...')
      time.sleep(8)
      status['Connected'] = True
      status['Est_Connection'] = 'Established'
      print('    Connected!\n')

    else:
      print(Fore.RED + '\nERROR: ' + c + ' is not a choice' + '\n' +  Fore.GREEN)
      _n_c = input('Connect To Database[Y]: ')
      if _n_c == 'Y' or _n_c == 'y':
        print('May take longer due to problems connecting before 😔 ')
        time.sleep(8)
        print('\nConnecting..')
        time.sleep(8.5)
        print('  Establishing Connection...')
        time.sleep(9.5)
        status['Connected'] = True
        status['Est_Connection'] = 'Established'
        print('    Connected\n')

      else:
        time.sleep(4)
        print('\nConnecting By Default..')
        time.sleep(12)
        print('  Establishing Connection...')
        time.sleep(12.5)
        status['Connected'] = [True, 'default_connect']
        status['Est_Connection'] = ['Established', 'forced_establishment']
        print('    Connected\n')

    #if status['Est_Connection'] == 'Established' or status['Connected'] == True:
     # break

    print(Fore.GREEN)
    break

def _s_():
  print('\n' + '~~' * 10)
  print(status)
  print('~~' * 10)

def _impo_(arg, n_arg):
  print('--' * 10)
  print(Fore.GREEN + str(status))
  #status.update({'Server_Is_Live': arg, 'New_Server_Is_Live': n_arg})

  #if status['Server_Is_Live'] == True:
    #status['Server_Is_Live'] = 'Yes'
    #status['New_Server_Is_Live'] = 'No'

  #if status['New_Server_Is_Live'] == True:
    #status['Server_Is_Live'] = 'No'
    #status['New_Server_Is_Live'] = 'Yes'

  print('--' * 10)
  print(Fore.GREEN)
    

  # This file is the database, or the file that stores all the data that is happening within the project
def _buffer_(arg1):
  buf = []
  buf_info = [str(arg1)]
  str(buf.append(buf_info))

  _buf_file = shelve.open('BUFFER.json.txt')
  _buf_file['_data_'] = buf
  _buf_file.close()


def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

# This stores the information about the user
def _send_(user_info):
  data_ap = []
  data = [str(user_info)]
  str(data_ap.append(data))

  file_ = shelve.open('mydata.json.txt')
  file_['data'] = data_ap
  file_.close() 

# This stores information about the users port
def _server_(server_info, extra_, _more_):
  serv_data = []
  data_ = [str(server_info), str(_more_)]
  str(serv_data.append(data_))

  _file_ = shelve.open('serverdata.json.txt')
  _file_['server_data'] = serv_data
  _file_['[other]'] = str({'db_connected': True, 'type': 'force_connection'})
  _file_.close()

# STORES INFO OF NEW SERVER  
def _new_server_(new_server, _extra_, more_):

  # Have more_ has a value of None we give it a string
  if more_ == [None]:
    more_ = 'User did not assign new port a name'
    more_.remove(None)

  new_server_data = []
  n_s_d = [str(new_server), str(more_)]
  str(new_server_data.append(n_s_d))

  __file__ = shelve.open('new_server.json.txt')
  __file__['new_data'] = new_server_data
  __file__.close()
      
# INFO NEEDED FOR THE _data_info_ DICTIONARY
def _time_():
  now_ = datetime.datetime.now()
  return now_.strftime("%Y-%m-%d %H:%M")
def _host_():
  get_ = socket.gethostname()
  return get_
# ip_ = socket.gethostbyname(get_)
def _ip_():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  sok_ = s.getsockname()[0]
  return sok_

def _data_info_(p, new_, _ex_):

  # Changes value of _ex_ being an empty string to None
  if _ex_ == '':
    _ex_ = 'User Did Not Assign Port There Name'

  _basic_info = []
  info = [str({'Name': _ex_, 'Stored_Under_Port': p ,'Stored_For': 'Advancement Of Project', 'Date_Updated': _time_(), 'Device': _host_(), 'User_ID': id_generator(), 'User_Given_IP': _ip_(), 'Is_Port_New': new_})]
  str(_basic_info.append(info))

  _file__ = shelve.open('about.json.txt')
  _file__['about'] = _basic_info
  _file__.close()

def _new_data_info(_p, _new_, __ex__):

  # Changes value of __ex__ being an empty string to None
  if __ex__ == None:
    __ex__ = 'User Did Not Assign Port There Name'

  _b_info = []
  _info_ = [str({'Name': __ex__, 'Stored_Under_Port': _p ,'Stored_For': 'Advancement Of Project', 'Date_Updated': _time_(), 'Device': _host_(), 'User_ID': id_generator(), 'User_Given_IP': _ip_(), 'Is_Port_New': _new_})]
  str(_b_info.append(_info_))

  __file__ = shelve.open('new_data.json.txt')
  __file__['new_data_'] = _b_info
  __file__.close()

# This will make a file of the start / end time
def _timing_(t_1, t_2):
  ap_t = []
  t_info = [str({'Start Time': t_1, 'End_Time': t_2})]
  str(ap_t.append(t_info))

  _t_file = shelve.open('time_info.json.txt')
  _t_file['time_info'] = ap_t
  _t_file.close()
