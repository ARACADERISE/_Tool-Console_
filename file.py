# IMPORTING PACKAGES NEEDED FOR PROJECT
from error import error
from exiting import exit_server_msg
import colorama
from colorama import Fore, Style
import time
from load_file import load_

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
    
# Storing users_name in a dictionary
names = {'UserName': users_name}

# welcoming user to my Tool-Console    

print(Fore.YELLOW + '\n山乇ㄥ匚ㄖ爪乇 ㄒㄖ 爪ㄚ ㄒ ㄖ ㄖ ㄥ - 匚 ㄖ 几 丂 ㄖ ㄥ 乇 ,', names['UserName'].upper())

# Making some loading time for the server to load
time.sleep(2)


''' SERVER STARTS '''


''' BREAKS ARE NEEDED IN CASE OF REPETITION '''


# Giving the server a value of true
server = True

# Starting the server
while server == True:
    
    # Asking the user to pick one of the following choices
    def choices():
        print(Fore.GREEN + '\nChoose one of these choices')
        print(Fore.BLUE + '1) "The Linux Choice" tools')
        print('2) Tools Choice Two')
        print('3) Tools Choice Three')
        print('4) Exit Tool-Console')
    
    choices()
    
    # This will be when the server ends
    server_ended = False
    
    while not server_ended:
        
        users_choice = input(Fore.GREEN + '> ')
        
        # This simply ask the user to stay
        def stay():
            
            print('Please type 1 to go back to main menu')
            go_back = input('> ')
            time.sleep(1)
            
            # Making any number above 1 invalid
            if go_back == '1':
                choices
            elif go_back > '1':
                error()
                stay()

        # Asks user to go back to main menu
        def error_go_back():
          print(Fore.GREEN + 'Type 1 to go back to main menu..')
          input('> ')
          time.sleep(1)
                
        # Making a function use() so we do not have to retype the code inside
        def use(LINK):
            print(Fore.GREEN + '--' * 9)
            print(LINK)
            print('--' * 9)
            
        # This will print "Getting.." when module targeted
        def get_():
          print(Fore.RED + 'Getting....')
          time.sleep(3)

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
                    use('LINK HERE')
                elif users_module_choice == '4':
                    get_()
                    use('LINK HERE 4')
                elif users_module_choice == '5':
                    get_()
                    use('LINK HERE 5')
            elif users_choice == '2':
                if users_module_choice_two == '1':
                    get_()
                    use('https://google.com3')
                elif users_module_choice_two == '2':
                    get_()
                    use('https://google.com4')
            elif users_choice == '3':
                if users_module_choice_three == '1':
                    get_()
                    use('https://google.com5')
                elif users_module_choice_three == '2':
                    get_()
                    use('https://google.com6')
        
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
            print('1. Choice one')
            print('2. Choice two')
            users_module_choice_two = input('> ')
            
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
            print('1. Choice one')
            print('2. Choice two')
            users_module_choice_three = input('> ')

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
            exit_server_msg()
            
        else:
            error()
            choices()
