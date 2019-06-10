import shelve
# import json
import datetime
import socket
# import platform
import random
import string

'''
  THIS IS THE FILE THAT WILL STORE USER DATA INTO FILES, THIS ID THE BACK END DEVELOPMENT OF THE PROJECT
'''

def _buffer_(arg1):
  buf = []
  buf_info = [str(arg1)]
  str(buf.append(buf_info))
  _buf_file = shelve.open('BUFFER.json.txt')
  _buf_file['_data_'] = buf
  _buf_file.close()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
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
  info = [str({'Name': _ex_, 'Stored_Under_Port': p ,'Stored_For': 'Advancement Of Project', 'Date_Updated': _time_(), 'Device': _host_(), 'User_ID': id_generator(), 'User_IP': _ip_(), 'Is_Port_New': new_})]

  str(_basic_info.append(info))
  _file__ = shelve.open('about.json.txt')
  _file__['about'] = _basic_info
  _file__.close()

def _new_data_info(_p, _new_, __ex__):

  # Changes value of __ex__ being an empty string to None
  if __ex__ == None:
    __ex__ = 'User Did Not Assign Port There Name'

  _b_info = []
  _info_ = [str({'Name': __ex__, 'Stored_Under_Port': _p ,'Stored_For': 'Advancement Of Project', 'Date_Updated': _time_(), 'Device': _host_(), 'User_ID': id_generator(), 'User_IP': _ip_(), 'Is_Port_New': _new_})]

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
