from load_file import port_l
import time
from colorama import Fore, Style
from exiting import leave_port
from error import error
from config import _server_, _data_info_, _new_server_, _new_data_info, _con_, _impo_, _s_
from packages import pkg_1, pkg_2, def_pkg
from db import DATABASE

# Helps us alternate between original server and new server
server_is_running = False
new_server_is_running = False

def delete_port():

  # Giving both value of false 
  server_is_running = False
  new_server_is_running = False

  # Giving a dictionory for the above
  exit_ = {'server_running': server_is_running, 'new_server_running': new_server_is_running}

  # Exiting the program
  while exit_['server_running'] == False and exit_['new_server_running'] == False:
    delete_port_ = True

    if delete_port_:
      leave_port()
      break

    
# Loading a port for the project
def _p_load_(_name_, _age_):

  server_is_running = False
  new_server_is_running = True

  # This is where extra information about server port will be stored
  _additional_ = []
  port_info_upd = {}

  # Asking the user to start either a default server or a server of there own
  time.sleep(1)
  server_port = input(Fore.GREEN + '\nPort(default 3000): ' + Fore.GREEN)
  time.sleep(2.4)

  # Setting default port to 3000
  if server_port == '':
    server_port = '3000'

  # Storing server_port into a dictionary
  port = {'Server_Port': server_port}

  _con_()
  _impo_(server_is_running, new_server_is_running)

  # EXPLINATION OF LIVE OR NOT LIVE SERVER
  print(Style.RESET_ALL + Fore.WHITE + '\nLive Port: A live port being live means that there is a 80% chance that someone could link there root to it and use it for any need they want. A Not Live server port is a secured port that NO ONE can get to or use but you at that given time \n\n NOTE: Your user info AND port info is stored in a file after the project is done executing, just heads up in case you might want to see what the program knows about you.')

  # Setting the server to Live or Not Live
  server_port_is_live_ = input(Fore.GREEN + '\nDo You Want Port ' + port['Server_Port'] + ' To Be Live (yes by default)[Y/n]: ')
  time.sleep(2)
      
  # Storing server_port_is_live_ into a dictionary
  is_port_live = {'Server_Port_Is_Live': server_port_is_live_}
      
  # Checking if the server is live
  if server_port_is_live_ == 'y' or server_port_is_live_ == 'Y':
    is_port_live['Server_Port_Is_Live'] = 'Live'
    print('Port ' + port['Server_Port'] + ' is ' + is_port_live['Server_Port_Is_Live'])
    print('\nPort Is Marked As Public, No Worries Though!')
  elif server_port_is_live_ == 'n' or server_port_is_live_ == 'N':
    is_port_live['Server_Port_Is_Live'] = 'Not Live'
    print('Port ' + port['Server_Port'] + ' is ' + is_port_live['Server_Port_Is_Live'])
    time.sleep(3)
    print('\nPort Marked As Secured! All Set')
  elif server_port_is_live_ == '':
    is_port_live['Server_Port_Is_Live'] = 'Live by default'
    print('Port ' + port['Server_Port'] + ' is ' + is_port_live['Server_Port_Is_Live'])
    print('\nPort Is Marked As Public(by default), No Worries Though!')
  else:
    error()
    server_port_is_live = input(Fore.GREEN + '\nDo You Want Port ' + port['Server_Port'] + ' To Be Live (yes by default)[Y/n]: ')
    if server_port_is_live == 'Y' or server_port_is_live == 'n':
      print(Fore.RED + 'Cannot follow through with change..sorry')
    else:
      print(Fore.RED + 'Cannot follow through with change..sorry')
      time.sleep(2)

  port_l(port['Server_Port'], is_port_live['Server_Port_Is_Live'])

  port_data = []
  port_info = {'Is_New': False, 'Dict_Name': 'Port_Data_Info', 'Type': 'basic', 'Port_ID': server_port, 'Is_Live': is_port_live['Server_Port_Is_Live'], 'Port_Security': True} # Set true by default

  # Giving the port more choices
  print(Fore.GREEN + Style.BRIGHT + '\nWe want to know more about what you want for your server port ' + port['Server_Port'] + '\n')
  def _ch_():
    print('1) Keep Port At Default Of Everything')
    print('2) Let Server Port Know Your Name')
    print('3) Let Server Port Know Your Name AND Age')
    
  _ch_()
  port_choice = input(Fore.GREEN + '> ')

  # We Add To The Dictionary port_info_upd On What The User Had Entered For port_choice
  if port_choice == '1':
    print('No Problem, we will keep your port at default!')
    port_info_upd.update({'Type': 'default_generated', 'Name': None, 'Age': None})
    _additional_.append(def_pkg())
  elif port_choice == '2':
    print('We will update your port data shortly!')
    port_info_upd.update({'Type': 'Extra_Port_Information','Name': _name_})
    _additional_.append(port_info_upd)
    _additional_.append(pkg_1())
  elif port_choice == '3':
    print('We will update your port data shortly!')
    port_info_upd.update({'Type': 'Extra_Port_Info', 'Name': _name_, 'Age': _age_})
    _additional_.append(port_info_upd)
    _additional_.append(pkg_2())
  else:
    print(Fore.RED + 'THERE WAS A ERROR' + Fore.GREEN)

  # Checking whether or not Port_Security is true or False
  if port_info['Is_Live'] == 'Live':
    port_info['Port_Security'] = True
    if port_info['Port_Security']:
      port_info['Port_Security'] = 'Your Server Port might be used by others'
  elif port_info['Is_Live'] == 'Not Live':
    port_info['Port_Security'] = False
    if port_info['Port_Security'] == False:
      port_info['Port_Security'] = 'Your Server Port is secured'
  elif port_info['Is_Live'] == 'Live by default':
    port_info['Port_Security'] = True
    if port_info['Port_Security']:
      port_info['Port_Security'] = 'Server Port is being shared with others By Default'
  # If for some reason the code doesn't execute correctly, this else statement will make the Data_Saved value UNKNOWN
  else:
    port_info['Data_Saved'] = 'UNKNOWN'

  # PRINTING PORT INFORMATION  
  port_data.append(port_info) 

  # Here we replace the value None that _additional_ gives us by default and tell the user why there is no additional information about there port
  if _additional_ == [None]:
    _additional_.append(['Information Could Not Be Loaded'])
    _additional_.remove(None)

  # If port_info_upd['Name'] has a value of None we change it to a string
  if port_info_upd['Name'] == [None] or port_info_upd['Name'] == '':
    port_info_upd['Name'] = 'User did not give port a name'

  # This will be stored in a file that the user can access after the project is done running
  _server_(port_data, port_info_upd['Name'], _additional_)
  _data_info_(port['Server_Port'], port_info['Is_New'], port_info_upd['Name'])

  DATABASE(port_info['Port_ID'], port_data)
    
  for item in port_data:
    print(Fore.YELLOW + Style.NORMAL + '\n' + '--' * 10)
    print('Data stored about your server port\n')
    print(item)
    print('--' * 10)
  

# Deletes previous port if user decides to make a new port
def delete_():
  time.sleep(2)
  print(Fore.RED + 'Deleting previous port....')
  time.sleep(8.5)
  print('Please wait while we dump the server...')
  time.sleep(5.8)
  print('One more moment...')
  time.sleep(5.5)

# Making a function so the user can change there port anytime
def change_port(__name__, __age__):

  server_is_running = False
  new_server_is_running = True

  _new_additional_ = []
  new_info_upd = {}

  delete_()

  time.sleep(3)
  print('\n' + Fore.GREEN + '---' * 8)
  new_port = input('New Port(default 3000): ')
  time.sleep(4)

  if new_port == '':
    new_port = '3000'
      
  new_port_ = {'New_Port': new_port}

  _s_()

  # _con_()
  # _impo_(server_is_running, new_server_is_running)

  new_port_live = input('Do you want the new port to be live(yes by default)[Y/n]: ')

  port_live = {'Is_New_Port_Live': new_port_live}

  if new_port_live == 'Y' or new_port_live == 'y':
    port_live['Is_New_Port_Live'] = 'Live'
    time.sleep(1.5)
    print('New port ' + new_port_['New_Port'] + ' is ' + port_live['Is_New_Port_Live'])
    print('\nPort Is Markes As Public, No Worries Though')

  elif new_port_live == 'N' or new_port_live == 'n':
    port_live['Is_New_Port_Live'] = 'Not Live'
    time.sleep(1.5)
    print('New port ' + new_port_['New_Port'] + ' is ' + port_live['Is_New_Port_Live'])
    print('\nPort Marked As Secured! All Set')

  elif new_port_live == '':
    port_live['Is_New_Port_Live'] = 'Live By Default'
    time.sleep(1.5)
    print('New port ' + new_port_['New_Port'] + ' is ' + port_live['Is_New_Port_Live'])
    print('\nPort Marked As Public(by default), No Worries Though!')

  _n_port = []
  new_port_data = {'Is_New': True, 'Dict_Name': 'New_Port_Info', 'Type': 'basic', 'Port_ID': new_port_['New_Port'], 'Is_Live': port_live['Is_New_Port_Live'], 'Port_Security': True} # True by default

  # Loads new port
  port_l(new_port_['New_Port'], new_port_data['Is_Live'])
  print('---' * 8)

  # Storing Extra Info About Port
  print(Fore.GREEN + Style.BRIGHT + '\nWe want to know more about what you want for your new server port ' + new_port_data['Port_ID'] + '\n')
  def _c_():
    print('1) Keep Port At Default Of Everything')
    print('2) Let New Server Port Know Your Name')
    print('3) Let New Server Port Know Your Name AND Age')
    
  _c_()
  new_port_choice = input(Fore.GREEN + '> ')

  # Adding to the dictionary new_info_upd,this is the same as the other one for the new server port should have the same concept as the original server, just different values
  if new_port_choice == '1':
    print('No Problem, we will keep your new port at default!')
    new_info_upd.update({'Type': 'New_Extra_Port_Info', 'Name': None, 'Age': None})
    _new_additional_.append(def_pkg())
  elif new_port_choice == '2':
    print('We will update your new port data shortly!')
    new_info_upd.update({'Type': 'New_Extra_Port_Info', 'Name': __name__})
    _new_additional_.append(new_info_upd)
    _new_additional_.append(pkg_1())
  elif new_port_choice == '3':
    print('We will update your new port data shortly!')
    new_info_upd.update({'Type': 'New_Extra_Port_Info', 'Name': __name__, 'Age': __age__})
    _new_additional_.append(new_info_upd)
    _new_additional_.append(pkg_2())
  else:
    print(Fore.RED + 'THERE WAS A ERROR' + Fore.GREEN)
    _c_()



  if new_port_data['Is_Live'] == 'Live':
    new_port_data['Port_Security'] = True
    if new_port_data['Port_Security']:
      new_port_data['Port_Security'] = 'Your Server Port might be used by others'
  elif new_port_data['Is_Live'] == 'Not Live':
    new_port_data['Port_Security'] = False
    if new_port_data['Port_Security'] == False:
      new_port_data['Port_Security'] = 'Your Server Port is secured'
  elif new_port_data['Is_Live'] == 'Live By Default':
    new_port_data['Port_Security'] = True
    if new_port_data['Port_Security']:
      new_port_data['Port_Security'] = 'Server Port is being shared with others By Default'
  
  _n_port.append(new_port_data)

  # If _new_additional_ has a value of None we change it to a string
  if _new_additional_ == [None]:
    _new_additional_.append('User did not give new port a name')
    _new_additional_.remove(None)
  if new_info_upd['Name'] == [None]:
    new_info_upd['Name'] = 'NO NAME GIVEN TO NEW PORT'

  # STORING PORT INFO
  _new_server_(_n_port, new_info_upd['Name'], _new_additional_)
  _new_data_info(new_port_data['Port_ID'], new_port_data['Is_New'], new_info_upd['Name'])

  for item in _n_port:
    print(Fore.YELLOW + '\n' + '--' * 10)
    print('New Data about your server port')
    print(item)
    print('--' * 10)
