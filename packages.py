import shelve
import json
from load import load


# THIS FILE IS A PART OF THE DATABASE


def pkg_1():
  pkg = {'Stored': 'As_Default', 'File_Author': None, 'Type': 'Extra'}
  return pkg
def pkg_2():
  pkg = {'Stored': 'As_Default', 'File_Author': None, 'Type': 'Extra'}
  return pkg
def def_pkg():
  pkg = {'Stored': 'As_Default', 'File_Author': 'None', 'Type': 'Default_Extra'}
  return pkg

# This will be executed when load_file.py is executed
def _get_():

  # This will return None due to the fact that we have not executed through the files
  _py_file = []
  url = 'https://github.com/ARACADERISE/_Tool-Console_.git'
  
  # So we help the above out by setting its fetching information by default!
  _g_ = {'Type': 'project_git', 'Project_Get': url, 'DEFAULT': []}
  # Changing it to json for the file
  json.dumps(_g_)

  _p_ = {'Type': 'Project_Details', 'DEFAULT': []}
  # Changing it to json for the file
  json.dumps(_p_)

  _f_ = {'Type': 'File_Fetch', 'DEFAULT': ['main.py', 'config.py', 'error.py', 'exiting.py', 'get_module.py', 'load_file.py', 'packages.py', 'port.py', {'not_needed': 'program.json'}]}
  # Changing it to json for the file
  json.dumps(_f_)

  _ = []
  _s_ = []

  _ap_ = str([
    'get_url', [str(_.append(_g_))],
    'get_details', [str(_.append(_p_))],
    'get_file', [str(_.append(_f_))],
  ])

  # Storing data about the project being loaded
  _load_ = {'load': [load(_g_['Type'], _g_), load(_p_['Type'], _p_), load(_f_['Type'], _f_)]}

  # Just storing _ap_ into a list
  _s_.append(_ap_)
  _s_.append(_load_)

  # Appending _
  str(_py_file.append(_))

  _open_ = shelve.open('project.json.txt')
  # This is the raw _py_file. We want to store the raw version for the fact that that is actually how the data would be stored
  _open_['[raw]'] = _py_file

  # This is the json formatted info
  _open_['[data]'] = str(_py_file)

  _open_.close()
  return 0

def _leave_(arg1):
  _l_ = []
  _leave_information = {'Type': 'exit_storage', 'Leaving_Info': [arg1]}
  json.dumps(_leave_information)

  _ = []
  _pend_ = []
  
  _i_ = str([
    'gather_', [_.append(_leave_information)],
    'gather_', [],
  ])

  _.append(_i_)

  __load__ = {'load_data': [load(_leave_information['Type'], _l_)]}

  _pend_.append(_)
  _pend_.append(_i_)
  _pend_.append(__load__)
  # print(_pend_)

  _l_.append(_leave_information)

  _s_ = shelve.open('exit_info.json.txt')
  _s_['[e_info_raw]'] = _l_
  _s_['e_info'] = str(_l_)
  _s_.close()
  return 0

# This is for the terminal
def _t_(arg):

  gen = {'generated_for': 'user_entering_terminal', 'DEFAULT': ['terminal', 'terminal_root']}

  get = []
  str(get.append(gen))
  str(get.append(arg))
  get.append(['DATABASE_GENERATED'])
  # _ = [].append(get)

  _term_ = shelve.open('terminal.json.txt')
  _term_['[raw]'] = get
  _term_['[term_data]'] = str(get)
  _term_.close()

# This will store steps of booting the terminal
def load_term(terminal):

  # Appending _t_ to terminal, where terminal will get data within the load_file.py that loads terminal
  _t_ = []
  str(_t_.append(terminal))

  # making file
  _boot_ = shelve.open('boot.json.txt')
  _boot_['store_this_data'] = str({'data_type': ['terminal']})
  _boot_['store_boot_data'] = str(_t_)
  _boot_.close()

def leave_term(terminal):
  _l_ = []
  str(_l_.append(terminal))

  _leave_ = shelve.open('leave.json.txt')
  _leave_['main'] = str({'leaving':'terminal'})
  _leave_['info'] = str(_l_)
