# IMPORTING PACKAGES NEEDED FOR PROJECT
from error import error
# from exiting import leave_port
# import colorama
from colorama import Fore, Style, Back
import time
from load_file import load_
from get_module import get_
from port import _p_load_, change_port, delete_port
from config import _send_, _timing_
import datetime

# START TIME
_t_ = []
_b_ = datetime.datetime.now()
before_ = _b_.strftime("%Y-%m-%d %H:%M")
_t_.append(before_)

# Setting the program is running to true so the program can..well..run
program_is_running = True

# LOADING THE FILE AT DEFAULT
load_()

'''

    Create the following:
    
    A python server that gives a user choices. Each choice leading a user to a new topic. Whatever the user chooses will then
    be led to a list of tools within that topic. Whatever tool they use it will output a link then ask for them  to go back to the beggining
    The loop shall restart on returning to the main menu
    
    Developer Tips:
    ---------------
    Each module will and should have familiar code, but different type of outcome/function used
    
    There should be functions being used all over the code below
    
    Developer should use if / elif statements

    This project should be well over 200 lines of code

    The majority of this project should be if/elif, unless you want to advance further and use classes or all function!

    Tip: You should assign a server to true and output all of the users input/data output within a while loop that states server_ended is false
    ---------------

    ###
    NOTE: I as a Python Developer do know that using multiple if / elif statements is not as "professional", but as somewhat begginners are trying to advance more and more into coding Python I find this project to be complex enough to use mutliple if / elif statements but not only that, but find out where you want them, what use they have inside each function and how exactly they'll affect your code. Not only will this project help advance young developers to really "see" what they're doing and need to do, but it will help further advance them to problem solve and see a solution to whatever problem they run into.

    ----------
    Try making this for yourself and see how much time it takes to really see what you're doing and need-to-do to just make your project make sense and flow correctly
    ----------
    ###
    
    ###
    NOTE ONCE AGAIN:
    If this project is to become an actual project to use within Termux,then simply use chmod +x FILE NAME HERE then use python FILE NAME HERE.py, no installation except for git clone LINK OF PROJECT
    ###
    
'''

# Getting the users name
users_name = input(Fore.GREEN + 'Your Name: ')
users_age = int(input(Fore.GREEN + 'Your Age: '))  

# Making a limit to how young you can be, or is allowed to be typed in
if users_age < 5 and users_age > 1:
  print(Back.RED + Fore.WHITE + Style.BRIGHT + 'ERROR: That is way to young, please try again')
  users_age = int(input(Style.RESET_ALL + Fore.GREEN + 'Your Age: '))
elif users_age < 0:
  print(Fore.WHITE + Back.RED + 'Error: That is not even an age, try agin')
  users_age = int(input(Style.RESET_ALL + Fore.GREEN + 'Your Age: '))

# Knowing that the user won't be able to get in unless they are older then 12 we will just let it go
if users_age < 5:
  print('Fine..we will accept the age of', users_age, '..why not!')

    
# Storing users_name and users_age in a dictionary
name = {'UserName': users_name}

age = {'Users_Age': str(users_age), 'Is_Of_Age':  True} # Assigned true as default

# Checking if user is under 12, if so stor Is_Of_Age as false
if users_age < 12:
  age['Is_Of_Age'] = False
  # Re-assigning the value of false to Is under age
  if age['Is_Of_Age'] == False:
    age['Is_Of_Age'] = 'Under Age'
else:
  age['Is_Of_Age'] = True
  # Re-assigns the value of false to true then true is re-assigned to Is of age
  if age['Is_Of_Age']:
    age['Is_Of_Age'] = 'Is of age'

# welcoming user to my Tool-Console    

print(Fore.YELLOW + '\n山乇ㄥ匚ㄖ爪乇 ㄒㄖ 爪ㄚ ㄒ ㄖ ㄖ ㄥ - 匚 ㄖ 几 丂 ㄖ ㄥ 乇 ,', name['UserName'].upper())

# Making some loading time for the server to load
time.sleep(2)


''' SERVER STARTS '''

# Giving the server a value of true
server = True

# Will load a server port AND tell the user what the program knows/has stored
_p_load_(name['UserName'], age['Users_Age'])

# Storing user data
user_data = []
user_info = {'Dict_name': 'User_Info_Data', 'User_Name': name['UserName'], 'Users_Age': age['Users_Age'], 'Of_Age': age['Is_Of_Age']}

user_data.append(user_info)

_send_(user_data)

for item in user_data:
  print(Style.NORMAL + '\n' + '--' * 10)
  print('Data stored about ' + user_info['User_Name'] + '\n')
  print(Fore.YELLOW + str(item))
  print('--' * 10 + '\n')

if users_age < 12:
  print(Fore.RED + 'Sorry, but according to your User_Info_Data you are ' + user_info['Of_Age'])
  server = False

''' BREAKS ARE NEEDED IN CASE OF REPETITION '''


# Starting the server
while server == True and program_is_running:
    
    # Asking the user to pick one of the following choices
    def choices():
        print(Fore.GREEN + '\nChoose one of these choices')
        print(Fore.BLUE + '1) "The Linux Choice" tools')
        print('2) Tools Choice Two')
        print('3) Tools Choice Three')
        print('4) Exit Tool-Console')
        print('8) Change My Server Port')
    
    choices()
    
    # This will be when the server ends
    server_ended = False
    
    while not server_ended:
        
        users_choice = input(Fore.GREEN + '> ')

        # Asks user to go back to main menu
        def error_go_back():
          print(Fore.GREEN + 'Type 1 to go back to main menu..')
          input('> ')
          time.sleep(1)
                
        # Making a function use() so we do not have to retype the code inside
        def use(LINK):
            print(Fore.YELLOW + '--' * 9)
            print(LINK)
            print('--' * 9)
        
        # This simply ask the user to stay
        def stay():
          print(Fore.GREEN + 'Please type 1 to go back to main menu')
          go_back = input('> ')
          time.sleep(1)

          # Making any number above 1 invalid
          if go_back == '1':
            choices
          elif go_back > '1':
            error()
            stay()

        # Making a function link() so we do not have to repeat the code inside the function both below and above  
        def link():
            
            # Based on the users_choice, each will print differently
            if users_choice == '1':
                if users_module_choice == '1':
                    get_()
                    use('https://github.com/thelinuxchoice/shellphish')
                elif users_module_choice == '2':
                    get_()
                    use('https://github.com/thelinuxchoice/blackeye')
                elif users_module_choice == '3':
                    get_()
                    use('')
                elif users_module_choice == '4':
                    get_()
                    use('')
                elif users_module_choice == '5':
                    get_()
                    use('')
            elif users_choice == '2':
                if users_module_choice_two == '1':
                    get_()
                    use('')
                elif users_module_choice_two == '2':
                    get_()
                    use('')
            elif users_choice == '3':
                if users_module_choice_three == '1':
                    get_()
                    use('')
                elif users_module_choice_three == '2':
                    get_()
                    use('')

        # Assigning an if statement to whatever the user has chosen
        time.sleep(1)
        if users_choice == '1':

            # Making a function called call_ to call the modules for the users choice
            def call_():
                print(Fore.GREEN + '\nNow choose one of the following 5 modules: ')
                print(Fore.BLUE + '1. The Linux Choice: Shellphish')
                print('2. The Linux Choice: Blackeye')
                print('3. The Linux Choice: Option 3')
                print('4. The Linux Choice: Option 4')
                print('5. The Linux Choice: Option 5')
            call_()
            users_module_choice = input(Fore.GREEN + '> ')
            
            # Checking which one the user chose within a if else statement
            if users_module_choice == '1':
                link()
                stay()
                break
            elif users_module_choice == '2':
                link()
                stay()
                break
            elif users_module_choice == '3':
                link()
                stay()
                break
            elif users_module_choice == '4':
                link()
                stay()
                break
            elif users_module_choice == '5':
                link()
                stay()
                break
            else:
                error()
                error_go_back()
                break
            
        elif users_choice == '2':
            print('\nNow choose one of the following within this module')
            print(Fore.BLUE + '1. Choice one')
            print('2. Choice two')
            users_module_choice_two = input(Fore.GREEN + '> ')
            
            if users_module_choice_two == '1':
                link()
                stay()
                break
            elif users_module_choice_two == '2':
                link()
                stay()
                break
            else:
              error()
              error_go_back()
              break
            
        elif users_choice == '3':

            print('\nNow choose one of the following within this module')
            print(Fore.BLUE + '1. Choice one')
            print('2. Choice two')
            users_module_choice_three = input(Fore.GREEN + '> ')

            if users_module_choice_three == '1':
              link()
              stay()
              break
            elif users_module_choice_three == '2':
              link()
              stay()
              break
            else:
              error()
              error_go_back()
              break

        elif users_choice == '4':
            server = False
            server_ended = True
            delete_port()
        
        elif users_choice == '5':
          time.sleep(6.5)
          print(Fore.RED + 'Gathering information...')
          time.sleep(10)
          print('Getting File...')
          time.sleep(5)
          print('Executing Information..')
          time.sleep(7.8)
          print('Sorry, execution failed')

          stay()
          choices()

        elif users_choice == '8':
          time.sleep(2)
          print(Fore.RED + 'NOTE: Once this transaction is done, previous information will be uploaded to there files')
          time.sleep(1.5)
          _send_(user_data)
          change_port(name['UserName'], age['Users_Age'])
          print(Style.NORMAL)
          stay()
          choices()

        else:
          error()
          choices()

# END TIME
__t__ = []
_a_ = datetime.datetime.now()
_after_ = _a_.strftime("%Y-%m-%d %H:%M")
__t__.append(_after_)
_timing_(_t_, __t__)
