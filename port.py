from load_file import port_l
import time
from colorama import Fore, Style
from exiting import leave_port
from error import error

# Just helps know when to exit, or start a new server, no use really, might help in the long run though
server_is_running = True
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
def _p_load_():

  # Asking the user to start either a default server or a server of there own
  time.sleep(1)
  server_port = input(Fore.GREEN + '\nPort(default 3000): ')
  time.sleep(2.4)
  print(Fore.WHITE + '\nLive Port: The port being live means that everything you do can be tracked. If you chose "Y" then the possibility of your usage being tracked is above 80%, but it is for a good use. If you chose "n" then your usage will not be tracked. \n NOTE: After you have declared your port and thereafter decide whether or not it is live you will not be able to pull up any information about it')

  # Setting default port to 3000
  if server_port == '':
    server_port = '3000'

  # Storing server_port into a dictionary
  port = {'Server_Port': server_port}

  # Setting the server to Live or Not Live
  server_port_is_live_ = input(Fore.GREEN + '\nDo You Want Port ' + port['Server_Port'] + ' To Be Live (yes by default)[Y/n]: ')
  time.sleep(2)
    
  # Storing server_port_is_live_ into a dictionary
  is_port_live = {'Server_Port_Is_Live': server_port_is_live_}
    
  # Checking if the server is live
  if server_port_is_live_ == 'y' or server_port_is_live_ == 'Y':
    is_port_live['Server_Port_Is_Live'] = 'Live'
    print('Port ' + port['Server_Port'] + ' is ' + is_port_live['Server_Port_Is_Live'])
    print('\nUsage of project will most likely be saved')
  elif server_port_is_live_ == 'n' or server_port_is_live_ == 'N':
    is_port_live['Server_Port_Is_Live'] = 'Not Live'
    print('Port ' + port['Server_Port'] + ' is ' + is_port_live['Server_Port_Is_Live'])
    time.sleep(3)
    print('\nYou will not have history in this project !')
  elif server_port_is_live_ == '':
    is_port_live['Server_Port_Is_Live'] = 'Live by default'
    print('Port ' + port['Server_Port'] + ' is ' + is_port_live['Server_Port_Is_Live'])
    print('\nUsage of project will most likely be saved')

  port_l(port['Server_Port'])

  port_data = []
  port_info = {'Is_New': False, 'Dict_Name': 'Port_Data_Info', 'Type': 'basic', 'Port_ID': server_port, 'Is_Live': is_port_live['Server_Port_Is_Live'], 'Data_Saved': True} # Set true by default

  # Checking whether or not Data_Saved is true or fals
  if port_info['Is_Live'] == False:
    port_info['Data_Saved'] == False
    if port_info['Data_Saved'] == False:
      port_info['Data_Saved'] = 'Data Not Saved'
  if port_info['Is_Live'] == True:
    port_info['Data_Saved'] = True
    if port_info['Data_Saved']:
      port_info['Data_Saved'] = 'Data will be saved'

  port_data.append(port_info)
  
  for item in port_data:
    print(Fore.YELLOW + '\n' + '--' * 10)
    print('Data stored about your server port')
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
def change_port():

  server_is_running = False
  new_server_is_running = True

  # Running this as a loop for the fact the the server_is_running has been declared as false
  while new_server_is_running and not server_is_running:
    delete_()

    time.sleep(3)
    print('\n' + Fore.GREEN + '---' * 8)
    new_port = input('New Port(default 3000): ')
    time.sleep(4)

    if new_port == '':
      new_port = '3000'
    
    new_port_ = {'New_Port': new_port}

    new_port_live = input('Do you want the new port to be live(yes by default)[Y/n]: ')

    port_live = {'Is_New_Port_Live': new_port_live}

    if new_port_live == 'Y' or new_port_live == 'y':
      port_live['Is_New_Port_Live'] = 'Live'
      time.sleep(1.5)
      print('New port ' + new_port_['New_Port'] + ' is ' + port_live['Is_New_Port_Live'])
      print('\nUsage of project will most likely be saved')
      port_l(new_port_['New_Port'])
      print('---' * 8)
      break

    elif new_port_live == 'N' or new_port_live == 'n':
      port_live['Is_New_Port_Live'] = 'Not Live'
      time.sleep(1.5)
      print('New port ' + new_port_['New_Port'] + ' is ' + port_live['Is_New_Port_Live'])
      print('\nYou will not have history in this project !')
      port_l(new_port_['New_Port'])
      print('---' * 8)
      break

    elif new_port_live == '':
      port_live['Is_New_Port_Live'] = 'Live By Default'
      time.sleep(1.5)
      print('New port ' + new_port_['New_Port'] + ' is ' + port_live['Is_New_Port_Live'])
      print('\nUsage of project will most likely be saved')
      port_l(new_port_['New_Port'])
      print('---' * 8)
      break
