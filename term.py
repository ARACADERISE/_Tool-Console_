import time
from colorama import Fore, Style, Back
import socket
from packages import _t_
from exiting import leave_port, exit_terminal
from load_file import _load_terminal
# import stat

# This will put the user into the projects "terminal"

def _terminal_(u_c, name):

  commands = [['root_get_rd'], ['root_lh'], ['root_get_t'], ['root_set_st'], ['root_ap_device'], ['root_ex']];

  _load_terminal(commands)


  term_info = []
  t_i = {'terminal_name': 'tc_root$ ','name_of_user_using_terminal': name}
  term_info.append(t_i)
  host = {'device': None}


  if u_c == 'tc-r-t':
    def _term_():
      terminal = True

      while terminal:

        r_c = []

        root = input(Fore.GREEN + 'tc_root$ ')

        if root == 'help' or root == 'Help':
          print('Here is what you can do:\n\n')
          print('~ Find your rooted device (root_get_rd)')
          print('~ Localhost (root_lh)')
          print('~ Print Terminal Info (root_get_t)')
          print('~ Store Your Own limited Terminal Info (root_set_st)')
          print('~ Append a key to your device (root_activate_device_secure_key)')
          print('~ Append Root To Device (root_ap_device)')
          print('~ Exit Root (root_ex)\n\n')

        elif root == 'root_get_rd':
          host.update({'device': socket.gethostname()})
          r_c.append(host)
          print(r_c)

        elif root == 'root_lh':
          print(str(socket._LOCALHOST) + '\n')

        elif root == 'root_get_t':
          print(str(term_info) + '\n')

        elif root == 'root_set_st':
          port = socket.gethostname()
          data_info_ = {'local_data': [], '_info': []}
          local_data = [input('What type of data: ')]
          rand_fact = [input('\nTell the terminal one, or multiple things using commas(,), about yourself: ')]

          user_ = {}

          # Appending to each '' within data_info_
          data_info_['local_data'].append(local_data)
          data_info_['_info'].append(rand_fact)

          user_.update({'port':port, 'data': data_info_})

          term_info.append(user_)
          _t_(term_info)

          print(Style.BRIGHT + 'We will update your data shortly\n' + Style.RESET_ALL)

        elif root == 'root_ex':
          terminal = False
          exit_terminal()
          leave_port()
          break
        
        elif root == 'root_activate_device_secure_key':
          key = input('#key(any, default a01): ')

          if key == '':
            key = 'a01'

          _device_ = str(socket.gethostname()) + '/' + key
          host.update({'device_appended_key': _device_})

          r_c.append(host)

          print('Updated: ' + str(r_c) + '\n')
        
        elif root == 'root_ap_device':

          device = str(socket.gethostname)
          device = str(socket.gethostname()) + '/tc_root'
          host.update({'pended_device': device})

          r_c.append(host)
          
          print('Updated: ' + str(r_c) + '\n')

        
        else:
          print(Fore.RED + 'ERROR: That is not a choice' + Fore.GREEN)

    time.sleep(3.6)
    print('''
                             _________
                           /         /.
    .-------------.       /_________/ |
   /             / |      |         | |
  /+============+\ |      | |====|  | |
  ||C:\> _      || |      |         | |
  ||            || |      | |====|  | |
  ||            || |      |   ___   | |
  ||            || |      |  |166|  | |
  ||            ||/@@@    |   ---   | |
  \+============+/    @   |_________|./.
                     @          ..  ....'
  ..................@     __.'.'  ''
 /oooooooooooooooo//     ///
/................//     /_/
------------------
    ''')
  time.sleep(2)
  print(Fore.WHITE + 'Welcome to _Tool-Console_s terminal. Type "Help" to see what you can do!\n\nBe Aware: You will not be able to transition back to the main project. So when you exit the terminal you will have to retype ' + Fore.RED + ' python file.py ' + Fore.GREEN)
  _term_()
