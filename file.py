# IMPORTING PACKAGES NEEDED FOR PROJECT
from error import error
# from exiting import leave_port
# import colorama
from colorama import Fore, Style, Back
import time
import os, subprocess
from load_file import load_
from get_module import get_
from port import _p_load_, change_port, delete_port
from config import _send_, _timing_
import datetime
from term import _terminal_
from exiting import exit_terminal

try:
  print(Fore.RED, Style.BRIGHT)
  cmd='git --version'
  'using',subprocess.call(cmd, shell=True)
  print(Style.NORMAL)
except:
  print("Error")
  print(Style.NORMAL)

# START TIME
_t_ = []
_b_ = datetime.datetime.now()
before_ = _b_.strftime("%Y-%m-%d %H:%M")
_t_.append(before_)

# Setting the program is running to true so the program can..well..run and a terminal to true
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

# Putting limit to length of name
if len(users_name) >= 14:
  print(Fore.RED + 'Name is too long, try again')
  users_name = input(Fore.GREEN + 'Your Name: ')
  if len(users_name) >= 14:
    print('You are now UNKNOWN')
    users_name = 'UNKNOWN'

# Getting the users age
users_age = int(input(Fore.GREEN + 'Your Age: '))  

# Making a limit to how young you can be, or is allowed to be typed in
if users_age < 5 and users_age > 1:
  time.sleep(3)
  print(Back.RED + Fore.WHITE + Style.BRIGHT + 'ERROR: That is way to young, please try again')
  users_age = int(input(Style.RESET_ALL + Fore.GREEN + 'Your Age: '))

# Limiting how old you can be
if users_age < 0:
  time.sleep(3)
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

print(Fore.YELLOW + '\n山乇ㄥ匚ㄖ爪乇 ㄒㄖ 爪ㄚ ㄒ ㄖ ㄖ ㄥ - 匚 ㄖ 几 丂 ㄖ ㄥ 乇 , %s' % name['UserName'].upper())

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
if users_age > 60:
  print(Fore.RED + 'Sorry, you are over the limited age limit according to the data you entered: Age ' + age['Users_Age'])
  server = False;


''' BREAKS ARE NEEDED IN CASE OF REPETITION '''


# Starting the server
while server == True and program_is_running:
    
    # Asking the user to pick one of the following choices
    def choices():
        print(Fore.GREEN + '\nChoose one of these choices')
        print(Fore.BLUE + '1) Web Hacking')
        print('2) Media Hacking')
        print('3) "The Linux Choice" top tools')
        print('4) Information Gathering')
        print('5) Leave _Tool-Console_')
        print('6) Next Update Info')
        print('7) About _Tool-Console_')
        print('8) Change port')
        print('9) Project Info')
        # print('10) See project files')
    
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
          print(Fore.GREEN + '\nPlease type 1 to go back to main menu')
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
                    get_('Sn1per', 'https://github.com/1N3/Sn1per')
                    use('https://github.com/1N3/Sn1per')
                    print('Type: Vulnerability Scanner')
                    print('Github Username: 1N3')
                    print('\nDownload: \nKali: \n1. git clone https://github.com/1N3/Sn1per \n2. bash install.sh \n\nUbuntu: \n1. git clone https://github.com/1N3/Sn1per \n2. bash install_debian_ubuntu.sh ')
                elif users_module_choice == '2':
                    get_('JohnTheRipper', 'https://github.com/magnumripper/JohnTheRipper.git')
                    use('https://github.com/magnumripper/JohnTheRipper.git')
                    print('Type: Password Cracking Tool')
                    print('Github Username: magnumripper')
                    print('\nDownload:\n Kali/Ubuntu: \n1. git clone https://github.com/magnumripper/JohnTheRipper.git \n2. cd JohnTheRipper \n3. cd run')
                elif users_module_choice == '3':
                    get_('Hydra', 'https://wiki.termux.com/wiki/Hydra')
                    use('https://wiki.termux.com/wiki/Hydra')
                    print('Type: Password Cracking Tool')
                    print('Github Username: <--Wiki Site-->')
                    print('\nDownload: \nKali/Ubuntu: \n1. pkg install hydra')
                elif users_module_choice == '4':
                    get_('Metasploit', 'https://wiki.termux.com/wiki/Metasploit_Framework')
                    use('https://wiki.termux.com/wiki/Metasploit_Framework')
                    print('Type: Execution of exploit code towards target')
                    print('Github Username: <--Wiki Site-->')
                    print('\nDownload: \nKali/Ubuntu: \n1. pkg install unstable-repo \n2. pkg install metasploit')
                elif users_module_choice == '5':
                    get_('sploitego', 'https://github.com/allfro/sploitego')
                    use('https://github.com/allfro/sploitego')
                    print('Type: "Cyber"(look it up for yourself)')
                    print('Github Username: allfro')
                    print('\nDownload: \nPlease visit there Github page for there are steps only you can uniquely take.')
            elif users_choice == '2':
                if users_module_choice_two == '1':
                    get_('Hunner','https://github.com/b3-v3r/Hunner')
                    use('https://github.com/b3-v3r/Hunner')
                    print('Type: Scan Vulnerability/Bruteforce')
                    print('Github Username: b3-v3r')
                    print('Download: \nKali/Ubuntu: \n1. git clone https://github.com/b3-v3r/Hunner \n2. cd hunner \n3. python hunner.py')
                    
                elif users_module_choice_two == '2':
                    get_('sqlmap')
                    use('https://github.com/sqlmapproject/sqlmap')
                    print('Type: Exploit code ejections')
                    print('Github Username: sqlmapproject')
                    print('\nDownload: \nKali/Ubuntu: \n1. git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev \n2. python sqlmap.py -hh')
                elif users_module_choice_two == '3':
                  get_('shellphish', 'https://github.com/thelinuxchoice/shellphish')
                  use('https://github.com/thelinuxchoice/shellphish')
                  print('Type: SSH, Social media phishinh')
                  print('Github Username: TheLinuxChoice')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/thelinuxchoice/shellphish \n2. cd shellphish \n3. bash shellphish.sh')
                elif users_module_choice_two == '4':
                  get_('userrecon', 'https://github.com/thelinuxchoice/userrecon')
                  use('https://github.com/thelinuxchoice/userrecon')
                  print('Type: Username finder')
                  print('Github Username: TheLinuxChoice')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/thelinuxchoice/userrecon.git \n2. cd userrecon \n3. bash userrecon.sh')
            elif users_choice == '3':
                if users_module_choice_three == '1':
                  get_('blackeye', 'https://github.com/thelinuxchoice/blackeye')
                  use('https://github.com/thelinuxchoice/blackeye')
                  print('Type: Ultamite phishing tool')
                  print('Github Username: TheLinuxChoice')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/thelinuxchoice/blackeye \n2. cd blackeye \n3. bash blackeye.sh')
                elif users_module_choice_three == '2':
                  get_('instashell', 'https://github.com/thelinuxchoice/instashell')
                  use('https://github.com/thelinuxchoice/instashell')
                  print('Type: Instagram Username Password Finder')
                  print('Github Username: TheLinuxChoice')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/thelinuxchoice/instashell \n2. cd instashell \n3. chmod +x instashell.sh \n4. service tor start \n5. sudo ./instashell.sh')
                elif users_module_choice_three == '3':
                  get_('saycheese', 'https://github.com/thelinuxchoice/saycheese')
                  use('https://github.com/thelinuxchoice/saycheese')
                  print('Type: Take pics of targets')
                  print('Github Username: TheLinuxChoice')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/thelinuxchoice/saycheese \n2. cd saycheese \n3. bash saycheese.sh')
            elif users_choice == '4':
                if users_module_choice_four == '1':
                  get_('clipboardme', 'https://github.com/thelinuxchoice/clipboardme')
                  use('https://github.com/thelinuxchoice/clipboardme')
                  print('Type: Writer/copier from target clipboard')
                  print('Github Username: TheLinuxChoice')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/thelinuxchoice/clipboardme.git \n2. cd clipboardme \n3. bash clipboardme.sh')
                elif users_module_choice_four == '2':
                  get_('D-tect', 'https://github.com/ihamquentin/D-tect')
                  use('https://github.com/ihamquentin/D-tect')
                  print('Type: Target Information Gatherer')
                  print('Github Username: ihamquentin')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/ihamquentin/D-tect.git \n2. cd D-tect && ls \n3. python2 d-tect.py')
                elif users_module_choice_four == '3':
                  get_('Nmap', 'https://wiki.termux.com/wiki/Nmap')
                  use('https://wiki.termux.com/wiki/Nmap')
                  print('Type: Network Discovery')
                  print('Github Username: <--Wiki Site-->')
                  print('\nDownload: \nKali/Ubuntu: \n1. pkg install nmap')
                elif users_module_choice_four == '4':
                  get_('RED_HAWK', 'https://github.com/Tuhinshubhra/RED_HAWK')
                  use('https://github.com/Tuhinshubhra/RED_HAWK')
                  print('Type: Site Info Gathering Tool')
                  print('Github Username: Tuhinshubhra')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/Tuhinshubhra/RED_HAWK \n2. cd RED_HAWK \n3. ' + Style.BRIGHT + Fore.RED + '[ ! ]' + Fore.YELLOW + '<---(HAVE PHP INSTALLED)--->' + Style.NORMAL + 'php rhawk.php')
                elif users_module_choice_four == '5':
                  get_('Crips', 'https://github.com/Manisso/Crips')
                  use('https://github.com/Manisso/Crips')
                  print('Type: Ip info gatherer, webpage info gatherer, dns record gathering tool')
                  print('Github Username: Manisso')
                  print('\nDownload: \nKali/Ubuntu: \n1. git clone https://github.com/Manisso/Crips.git \n2. cd Crips && python Crips.py \n3. python2 crips.py')
                elif users_module_choice_four == '6':
                  get_('OSIF', 'https://github.com/CiKu370/OSIF')
                  use('https://github.com/CiKu370/OSIF')
                  print('Type: Gathering tool for Facebook')
                  print('Github Username: CiKu370')
                  print('\nDownload: \nKali/Ubuntu: \n1. pkg update upgrade \n2. pkg install git python2 \n3. git clone https://github.com/ciku370/OSIF \n4. cd OSIF \n5. pip2 install -r requirements.txt \n5. python2 osif.py')

        # Assigning an if statement to whatever the user has chosen
        time.sleep(1)

        if users_choice == 'help kali':
          print('Step 1: pkg install wget')
          print('Step 2: wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter')
          print('Step 3: chmod +x kalinethunter')
          print('Step 4: bash kalinethunter')
          print(Fore.GREEN + Style.BRIGHT + "You're All Set!" + Style.NORMAL)
          time.sleep(3)
          break
            
        elif users_choice == 'help ubuntu':
          print('Step 1: apt-get update && apt-get upgrade -y')
          print('Step 2: apt-get install wget -y')
          print('Step 3: apt-get install proot -y')
          print('Step 4: apt-get install git -y')
          print('Step 5: cd ~')
          print('Step 6: git clone https://github.com/MFDGaming/ubuntu-in-termux.git')
          print('Step 7: cd ubuntu-in-termux')
          print('Step 8: chmod +x ubuntu.sh')
          print('Step 9: ./ubuntu.sh')
          print('Step 10 & 11: 10: cp ~/ubuntu-in-termux/resolv.conf ~/ubuntu-in-termux/ubuntu-fs/etc/ 11: ./start.sh')
          time.sleep(3)
          break

        if users_choice == '1':

            # Making a function called call_ to call the modules for the users choice
            def call_():
                print(Fore.BLUE + Style.BRIGHT + '\nWEB HACKING IN KALI/UBUNTU\n' + Style.RESET_ALL + Fore.GREEN + 'Now choose one of the following 5 modules(type help then the number you want help with or help kali/ubuntu to see how to download): ')
                print(Fore.BLUE + '1. Sniper')
                print('2. John The Ripper')
                print('3. THC HYDRA')
                print('4. METASPLOIT')
                print('5. MALTEGO')
            call_()
            users_module_choice = input(Fore.GREEN + '> ')
            # Checking which one the user chose within a if else statement
            if users_module_choice == 'help 1':
              print('\nType: Vulnerability Scanner')
              print('Explination: scans for sensitive data. Finds data not well protected\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice == '1':
                link()
                stay()
                break

            elif users_module_choice == 'help 2':
              print('\nType: Password cracker')
              print('Explination: Tries thousands of passwords till one is the correct one\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice == '2':
                link()
                stay()
                break

            elif users_module_choice == 'help3':
              print('\nType: Password Cracking Tool')
              print('Explination: Tries thousands of passwords until it fumbles upon one that is correct\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice == '3':
                link()
                stay()
                break

            elif users_module_choice == 'help 4':
              print('\nType: Exuction of exploit code towards target')
              print('Explination: Tool used for executing exploit code towards a target(framework)\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice == '4':
                link()
                stay()
                break

            elif users_module_choice == 'help 5':
              print('\nType: "Cyber"(look it up for yourself)')
              print('Explination: Sends cyber threat pictures to a organization\n')
              time.sleep(3)
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
            def c():
              print(Fore.BLUE + Style.BRIGHT + '\nMedia Hacking In Kali/Ubuntu\n'.upper() + Style.NORMAL + Fore.GREEN + 'Now choose one of the following within this module(type help then the number you need help on)')
              print(Fore.BLUE + '1. Hunner framework')
              print('2. SQLMAP')
              print('3. Shellphish')
              print('4. userrecon')
            c()
            users_module_choice_two = input(Fore.GREEN + '> ')

            if users_module_choice_two == 'help 1':
              print('\nType: Vulnerability Scans/Bruteforce')
              print('Explination: Hacking framework with ssh and uses bruteforce. Framework hacking.\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice_two == '1':
              link()
              stay()
              break

            elif users_module_choice_two == 'help 2':
              print('\nType: Exploiting exploit code into databases. can be used for web as well')
              print('Explination: Exploits a database at any given Vulnerability that is provided within the database.\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice_two == '2':
              link()
              stay()
              break
            
            elif users_module_choice_two == 'help 3':
              print('\nType: Phishing tool for social media')
              print('Explination: Creates a ssh website similar to what the logins of these social media platforms are and once user has entered user+pass it will send you the data\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice_two == '3':
              link()
              stay()
              break
            
            elif users_module_choice_two == 'help 4':
              print('\nType: Username finder')
              print('Explination: This tool goes over 75 other social media networks and finds a certain username. Helpful for if you want to attack there password!\n')
              time.sleep(3)
              stay()
              break
            
            elif users_module_choice_two == '4':
              link()
              stay()
              break

            else:
              error()
              error_go_back()
              break
            
        elif users_choice == '3':
            def _c_():
              print(Fore.BLUE + Style.BRIGHT + '\nThe Linux Choice Top Tools In Kali/Ubuntu\n'.upper() + Style.NORMAL + Fore.GREEN + 'Now choose one of the following within this module(type help and then the number you need help with)')
              print(Fore.BLUE + '1. Blackeye')
              print('2. Instashell')
              print('3. saycheese')
              print('4. clipboardme')
            _c_()
            users_module_choice_three = input(Fore.GREEN + '> ')

            if users_module_choice_three == 'help 1':
              print('\nType: Ultamite phishing tool')
              print('Explination: Gather user info from any social media they have!\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice_three == '1':
              link()
              stay()
              break

            elif users_module_choice_three == 'help 2':
              print('\nType: Instagram password finder')
              print('Expination: This tool runs a non-stop list of passwords on a Instagram username till the password is found\n')
              time.sleep(3)
              stay()
              break

            elif users_module_choice_three == '2':
              link()
              stay()
              break
            
            elif users_module_choice_three == 'help 3':
              print('\nType: Picture taker for targets camera')
              print('Explination: This tool uses Serveo or Ngrok to create a malicious website using JavaScript to take pictues of the target\n')
              time.sleep(3)
              stay()
              break
            
            elif users_module_choice_three == '3':
              link()
              stay()
              break
            
            elif users_module_choice_three == 'help 4':
              print('\nType: This tool can write/copy anything from user clipboard')
              print('Explination: This tool uses JavaScript to either write or sync data from your Targets clipboard\n')
              time.sleep(3)
              stay()
              break
            
            elif users_module_choice_three == '4':
              link()
              stay()
              break

            else:
              error()
              error_go_back()
              break
        
        elif users_choice == '4':
          def __c__():
            print(Fore.BLUE + Style.BRIGHT + '\nInformation Gathering In Kali/Ubuntu\n'.upper() + Style.NORMAL + Fore.GREEN + 'Now choose one of the following within this module(type help and then the number you need help with)')
            print(Fore.BLUE + '1. M-Dork')
            print('2. D-Tect')
            print('3. Nmap')
            print('4. Red Hawk')
            print('5. Crips')
            print('6. OSIF')
          __c__()
          users_module_choice_four = input(Fore.GREEN + '> ')

          if users_module_choice_four == 'help 1':
            print('\nType: Gathers info from domain')
            print('Explination: this tool requires user(you) to input a domain then the magic starts!\n')
            time.sleep(3)
            stay()
            break

          elif users_module_choice_four == '1':
            link()
            stay()
            break

          elif users_module_choice_four == 'help 2':
            print('\nType: Penetration Testing')
            print('Explination: This is a easy to use tool that uses multiple features to gather information about your targets. Can be used for both Security or you know ;)\n')
            time.sleep(3)
            stay()
            break
          
          elif users_module_choice_four == '2':
            link()
            stay()
            break
          
          elif users_module_choice_four == 'help 3':
            print('\nType: Network discovery')
            print('Explination: Gathers information from networks\n')
            time.sleep(3)
            stay()
            break
          
          elif users_module_choice_four == '3':
            link()
            stay()
            break;
          
          elif users_module_choice_four == 'help 4':
            print('\nType: Information Gathering from site titles, to site information to scanning')
            print('Explination: Scans sites from basic information to some pretty interesting things\n')
            time.sleep(3)
            stay()
            break
          
          elif users_module_choice_four == '4':
            link()
            stay()
            break
          
          elif users_module_choice_four == 'help 5':
            print('\nType: IP Information Gatherer')
            print('Explination: Gathers information from ip addresses, web pages and DNS records\n')
            time.sleep(3)
            stay()
            break
          
          elif users_module_choice_four == '5':
            link()
            stay()
            break
          
          elif users_module_choice_four == 'help 6':
            print('\nType: Facebook Information Gatherer')
            print('Explination: What can I epxlain? It says it all above!\n')
            time.sleep(3)
            stay()
            break
          
          elif users_module_choice_four == '6':
            link()
            stay()
            break
          
        elif users_choice == '5':
          server = False
          server_ended = True
          program_is_running = False
          delete_port()
          break
        
        elif users_choice == '6':
          print('\n' + Fore.BLUE + 'Topic: Modes' + Fore.GREEN)
          print('Explination: Tool-Console has been out for around a month to 2 months now and is ready to face the future of Tool-Console-Modes. The modes will vary as each update comes out. An avg of 2 modes will be available within this upcoming update! Enjoy!')
          stay()
          break
        
        elif users_choice == '7':
          print(Fore.BLUE + Style.BRIGHT + '\nAbout _Tool-Console_')
          print(Fore.WHITE + Style.BRIGHT + '\n_Tool-Console_ was thought of when I saw how much struggle and time it took to use those other tools to find the right tool for you. Yes, there was a good one out there of the name Tool-X for it organized tools. So why did I make this? \nTruth be told, I wanted to make it VERY easy to have access to top tools from top developers that are the most used! This tool is new, but trust me the udpates are coming and it will become a very powerful way to get top tools!\n' + Style.NORMAL)
          stay()
          break

        elif users_choice == '8':
          time.sleep(2)
          print(Fore.RED + 'NOTE: Once this transaction is done, previous information will be uploaded to there files')
          time.sleep(1.5)
          _send_(user_data)
          change_port(name['UserName'], age['Users_Age'])
          print(Style.NORMAL)
          stay()
          break
        
        elif users_choice == '9':
          print('Developer Name                Aidan White/ARACADE_RISE')
          print('Date Started                  June 4th, 2019, 7pm')
          print('Date Released                 June 19th, 2019, 4pm')
          print('Developer Email               t.targetyt@gmail.com')
          print('Project Type                  Terminal/Terminal App.')
          print('Version                       1.0.1')
          print(Fore.RED + Style.BRIGHT + '\n\n[ ! ]' + Style.NORMAL + Fore.BLUE + 'Please send me an email, or contact me via SnapChat @aidan_5554, if you come across any error within the project. Thank You!')
          time.sleep(12)
          stay()
          break
        
        elif users_choice == '10':
          print('Files:\n')
          'show',subprocess.call(["ls"])
          time.sleep(4)
          stay()
          break

        elif users_choice == '11':
          time.sleep(6.5)
          print(Fore.RED + 'Gathering information...')
          time.sleep(10)
          print('Getting File...')
          time.sleep(5)
          print('Executing Information..')
          time.sleep(7.8)
          print('Sorry, execution failed')

          stay()
          break

        def _tr_():
          __ = input('#t: ')
          if __ == 'run_t':
            ter = input('#run_t: ')
            if ter == 'tc-r-t':
              _terminal_(ter, name['UserName'])
            else:
              print(Fore.RED + 'Unable to get to the terminal..closing project')
              exit_terminal()
          else:
            print(Fore.RED + 'Not able to find that type of directory root' + Fore.GREEN)
            _tr_()
              
        
        if users_choice == 'open-t':
          print('To Continue, [Y], To Leave [n]')
          t_ = input('#: ')
          if t_ == 'y' or t_ == 'Y':
            _tr_()

            # ENDING THE SERVER
            server = False
            server_ended = True
            program_is_running = False
            break              
        else:
          error()
          choices()

# END TIME
__t__ = []
_a_ = datetime.datetime.now()
_after_ = _a_.strftime("%Y-%m-%d %H:%M")
__t__.append(_after_)
_timing_(_t_, __t__)
