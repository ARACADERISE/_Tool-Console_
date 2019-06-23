clear

GREEN="\033[92m"
RED="\033[91m"
BLUE="\033[94m"
WHITE="\033[0;37m"
BOLDY="\033[1;33m"

echo -e "$GREEN $RESET\n\n"

echo -e "
      ___ __   __  __        ___ __  __ _ ____  __  __   ____ 
    (_ T_/  \ /  \(l )  ___ /c__/  \( n( /s___)/  \(l ) ( E__)
      )((  O (  O / (_/(___( (_(  O /    \___ (  O / (_/\) _) 
     (__)\__/ \__/\___/     \___\__/\_)__(____/\__/\____(____) V.1.0.1
                   Top Tools, Top Developers, Free
                   MADE_BY: ARACADE_RISE,
                   
                   THANK YOU for running this part of the project, not only will this help you install Ubuntu/Kali but it also sets
                   up the project itself again!
"

bootDown()
{
  echo -e "$BOLDY"
  read -p "SAFE_MODE_ON# " shell
  if [ $shell == 'help' ]
  then
    echo -e "$BOLDY > SAFE_MODE_ON turns on by default everytime user exits project. CASE SENSETIVE!"
    echo -e "$BOLDY > Type Turn_Off to return back to normal terminal! OR Turn_Off&&tools.sh"
    echo -e "$BOLDY > Type Turn_Off&&python.file.py to run the main project"
    echo -e "$BOLDY > Type 'cat' to load file information"
    echo -e "$BOLDY > Type see_d_f to see list of files!"
    echo -e "$BOLDY > clear to clear terminal"
    bootDown
  elif [ $shell == 'cat' ]
  then
    read -p "name_of_file# " nof
    if [ $nof == 'exit' ]
    then
      bootDown
    fi
    echo -e "$WHITE"
    cat $nof
    bootDown
  elif [ $shell == 'see_d_f' ]
  then
    cd && cd _Tool-Console_
    ls
    bootDown
  elif [ $shell == 'Turn_Off' ]
  then
    echo -e "SAVE_MODE_ON# term.exit.withStatus(1)"
    echo -e "Exited with" exit "status" 1 "$WHITE"
    clear 
    echo -e "$WHITE \n==> HERE IS YOUR DIRECTORY <==\n"
    cd ~ && ls
  elif [ $shell == 'Turn_Off&&tools.sh' ]
  then
    echo -e "SAFE_MODE_ON# bash tools.sh"
    # echo -e exit "status" 1
    cd && cd _Tool-Console_
    bash tools.sh
  elif [ $shell == 'Turn_Off&&python.file.py' ]
  then
    echo -e "SAFE_MODE_ON# python file.py $WHITE"
    # echo -e exit "status" 1
    cd && cd _Tool-Console_
    python file.py
  elif [ $shell == 'clear' ]
  then
    clear
    bootDown
  else
    bootDown
  fi
}
 
ask()
{
echo -e "$RED \n==>TYPE 'Y' TO INSTALL<=="
#echo -e "$RED \n==>OR, TYPE ctrl-c TO EXIT<==\n"
read -p "#> " ch
}

route()
{
echo -e "$BLUE ==> CHOOSE <==\n \n==> 1. python file.py 2. bash tools.sh 3. exit <== $WHITE"
}

load()
{
if [ $ch == 'y' ]
then
echo -e "$RED \n==>SETTING UP<==\n $WHITE"
apt update && apt updgrade
pkg install python

ehco -e "$GREEN \n==>INSTALLING PROJECT DETAILS<==\n $WHITE"
git clone https://github.com/ARACADERISE/_Tool-Console_.git
https://github.com/ARACADERISE/_Tool-Console_/blob/master/tools.sh
https://github.com/ARACADERISE/_Tool-Console_/blob/master/rights.txt
https://github.com/termux/termux-packages
apt install git

echo -e "$RED \n==>INSTALLING UBUNTU<==\n $WHITE"
apt-get update && apt-get upgrade -y
apt-get install wget -y
apt-get install proot -y
apt-get install git -y
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
echo -e "$BLUE \n==>If you want to use Ubuntu: \n1.cd ubuntu-in-termux\n2.chmod +x ubuntu.sh\n3. ./ubuntu.sh\n4.cp ~/ubuntu-in-termux/resolv.conf ~/ubuntu-in-termux/ubuntu-fs/etc/
./start.sh\n<==\n"

echo -e "$RED \n==>INSTALLING KALI<==\n $WHITE"
pkg install wget
wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter
echo -e "$BLUE To run: \n
1.chmod +x kalinethunter\n
2.bash kalinethunter"

echo -e "$RED \n==>INSTALLING PHP<==\n $WHITE"
apt install php

echo -e "$RED \n==>At no point is it alright to edit the script source and claim it as your own work, even at fault of deleting all code and creating your
own version of it<==\n $WHITE"

echo -e "$RED \n ==>INSTALLED SUCESSFULLY<== $WHITE"
# echo -e "$BLUE ==>To run, type python file.py<== $WHITE"
echo -e "$BLUE ==>Want to read Tool-Consoles rights document? Type $RED cat rights.txt$BLUE<==\n $WHITE"
echo -e "E   N   J   O   Y!"
else
echo -e "$RED \n==> Redirecting... <==\n"
ask
load
fi
}

after()
{
read -p ">> " ro

if [ $ro == 1 ]
then
  echo -e "$RED \n==> BOOTING PROJECT <==\n $WHITE"
  python file.py
  echo -e "$RED \n==> Redirecting you to bash.sh to install the tools! <==\n $WHITE"
  cd && cd _Tool-Console_
  bash tools.sh
  bootDown
elif [ $ro == 2 ]
then
  echo -e "$RED \n==> BOOTING tools.sh <==\n $WHITE"
  cd && cd _Tool-Console_
  bash tools.sh
  bootDown
elif [ $ro == 3 ]
then
  bootDown
fi
}

# CALLING THEM
ask
load
route
after
