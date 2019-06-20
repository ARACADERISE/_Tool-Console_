
GREEN="\033[92m"
RED="\033[91m"
BLUE="\033[94m"
WHITE="\033[0;37m"

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
 
echo -e "$RED \n==>TYPE 'Y' TO INSTALL<=="
#echo -e "$RED \n==>OR, TYPE ctrl-c TO EXIT<==\n"
read -p "#> "

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
echo -e "$BLUE ==>You can type $RED bash tools.sh $BLUE to install the tools offered<== $WHITE"
echo -e "$BLUE ==>Want to read Tool-Consoles rights document? Type $RED cat rights.txt$BLUE<==\n $WHITE"
echo -e "E   N   J   O   Y!"

python file.py
