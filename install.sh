
GREEN="\033[92m"
RED="\033[91m"
BLUE="\033[94m"
WHITE="\033[0;37m"

echo -e "$GREEN $RESET\n\n"

echo -e "
      ___ __   __  __        ___ __  __ _ ____  __  __   ____ 
    (_  _/  \ /  \(  )  ___ / __/  \(  ( / ___)/  \(  ) (  __)
      )((  O (  O / (_/(___( (_(  O /    \___ (  O / (_/\) _) 
     (__)\__/ \__/\___/     \___\__/\_)__(____/\__/\____(____) V.1.0.1
                   Top Tools, Top Developers, Free
                   MADE_BY: ARACADE_RISE,
                   
                   THANK YOU for running this part of the project, not only will this help you install Ubuntu/Kali but it also sets
                   up the project itself again!
"
 
echo -e "$RED \n-->TYPE 'Y' TO INSTALL<--\n"
echo -e "$RED \n-->OR, TYPE ctrl-c TO EXIT<--\nType Below:"
read anser

echo -e "$RED \n-->Installing Requirements For Tool-Console<--\n$RESET"
apt update && apt upgrade
https://github.com/ARACADERISE/_Tool-Console_/blob/master/install.sh
pkg install python

echo -e "$RED \n-->Setting up...<--\n$RESET $WHITE"
git clone https://github.com/ARACADERISE/_Tool-Console_.git
https://github.com/termux/termux-packages.git
echo -e "$RED \n-->Setting up Ubuntu<--\n$RESET $WHITE"
apt-get update && apt-get upgrade -y
apt-get install wget -y
apt-get install proot -y
apt-get install git -y
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
echo -e "\n$OKORANGE To use ubuntu \ncd ubuntu-in-termux \nchmod +x ubuntu.sh \n./ubuntu.sh \ncp ~/ubuntu-in-termux/resolv.conf ~/ubuntu-in-termux/ubuntu-fs/etc/
./start.sh\n"
echo -e "$RED \n-->Setting Up Kali<--\n$RESET"
pkg install wget
wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter
chmod +x kalinethunter
bash kalinethunter

echo -e "$BLUE \n-->Done!<--\n$RESET"
echo -e "$BLUE \n-->To run, type python file.py!<--\n $RESET"

echo -e "$BLUE \nE  N  J  O  Y\n $RESET $WHITE"
