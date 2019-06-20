clear

GREEN="\033[92m"
RED="\033[91m"
BLUE="\033[94m"
WHITE="\033[0;37m"
BOLDR="\033[1;31m"

echo -e "$GREEN $RESET\n\n"

title()
{
echo -e "$GREEN
      ___ __   __  __        ___ __  __ _ ____  __  __   ____ 
    (_  _/  \ /  \(  )  ___ / __/  \(  ( / ___)/  \(  ) (  __)
      )((  O (  O / (_/(___( (_(  O /    \___ (  O / (_/\) _) 
     (__)\__/ \__/\___/     \___\__/\_)__(____/\__/\____(____) V.1.0.1
                 Top Tools, Top Developers, Free,
                 Tool Download Version
                 MADE_BY: ARACADE_RISE,
                   "
}
title
info()
{
echo -e "$BOLDR \n==>NOTE: You can only download one at a time<==\n"     
echo -e "$BOLDR \n==> After the tool downloads you can then type run-nameoftoolhere instead of putting in a number, or you can type
open-project to run the python side of things! (NOTE: It is not case sensetive meaning the file name can be in all lowercase even if
it has uppercase letters in it)<==\n"
}
info

tool()
{
# echo -e "$BLUE \n-->TOOLS<--\n "
echo -e "$BOLDR \n==> C H O O S E - O N E - O F - T H E - F O L L O W I N G - T O O L S <==\n"
echo -e "$BLUE\n1.Sniper\n2.JohnTheRipper\n3.Hydra\n4.Metasploit\n5.sploitego\n6.Hunner\n7.sqlmap\n8.shellphish\n9.userrecon\n10.BlackEye
\n11.InstaShell\n12.SayCheese\n13.ClipBoardMe\n14.IP-Tracer\n15.Nmap\n16.RED_HAWK\n17.Crips\n18.OSIF\n19.Leave$WHITE"
read -p "Your Choice >> " choice 
}

install()
{
if [ $choice == 'setup-sniper' ]
then
  mode()
  {
  echo -e "$BOLDR \n==> SETUP <==\n $WHITE"
  read -p "normal-mode[y/n]?>> " setup
  if [ $setup == 'y' ]
  then
    read -p "normal-mode>>target>> " theTarget
    bash sniper -t --$theTarget
    title
    info
    tool
    install
  elif [ $setup == 'n' ]
  then
    echo -e "$BOLDR \n==> REDIRECTING YOU... <==\n"
    title
    info
    tool
    install
  elif [ $setup == 'leave' ]
  then
    echo -e "$BOLDR \n==> Bye bye <==\n"
  fi
  }
  mode
elif [ $choice == 1 ]
then
  echo -e "$RED \n==> INSTALLING SNIPER <==\n $WHITE"
  git clone https://github.com/1N3/Sn1per
  # echo -e "$BLUE \n1.cd Sniper\n2.bash install.sh"
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 2 ]
then
  echo -e "$RED \n==> INSTALLING JohnTheRipper <==\n $WHITE"
  git clone https://github.com/magnumripper/JohnTheRipper.git
  echo -e "$BLUE \n1.cd JohnTheRipper\n2.cd run"
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 3 ]
then
  echo -e "$RED \n==> INSTALLING HYDRA <==\n $WHITE"
  pkg install hydra
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 4 ]
then
  echo -e "$RED \n==> INSTALLING METASPLOIT <==\n $WHITE"
  pkg update && pkg upgrade -y && pkg install wget curl openssh git -y
  pkg install unstable-repo
  wget Auxilus.github.io/metasploit.sh
  pkg install metasploit
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 5 ]
then
  echo -e "$RED \n==> INSTALLING sploitego <==\n $WHITE"
  git clone https://github.com/allfro/sploitego
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 6 ]
then
  echo -e "$RED \n==> INSTALLING Hunner <==\n $WHITE"
  git clone https://github.com/b3-v3r/Hunner
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 7 ]
then
  echo -e "$RED \n==> INSTALLING sqlmap <==\n $WHITE"
  git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D<==\n $WHITE"
  tool
  install
elif [ $choice == 8 ]
then
  echo -e "$RED \n==> INSTALLING shellphish <==\n $WHITE"
  git clone https://github.com/thelinuxchoice/shellphish
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 9 ]
then
  echo -e "$RED \n==> INSTALLING userrecon <==\n $WHITE"
  git clone https://github.com/thelinuxchoice/userrecon.git
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 10 ]
then
  echo -e "$RED \n==> INSTALLING blackeye <==\n $WHITE"
  git clone https://github.com/thelinuxchoice/blackeye
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 11 ]
then
  echo -e "$RED \n==> INSTALLING InstaShell <==\n $WHITE"
  git clone https://github.com/thelinuxchoice/instashell
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 12 ]
then
  echo -e "$RED \n==> INSTALLING SayCheese <==\n $WHITE"
  git clone https://github.com/thelinuxchoice/saycheese
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 13 ]
then
  echo -e "$RED \n==> INSTALLING ClipBoardMe <==\n $WHITE"
  git clone https://github.com/thelinuxchoice/clipboardme.git
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 14 ]
then
  echo -e "$RED \n==> INSTALLING IP-Tracer <==\n $WHITE"
  git clone https://github.com/Rajkumrdusad/IP-Tracer.git
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 15 ]
then
  echo -e "$RED \n==>INSTALLING Nmap<==\n $WHITE"
  pkg install nmap
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D<==\n $WHITE"
  tool
  install
elif [ $choice == 16 ]
then
  echo -e "$RED \n==> INSTALLING RED_HAWK <==\n $WHITE"
  git clone https://github.com/Tuhinshubhra/RED_HAWK
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 17 ]
then
  echo -e "$RED \n==> INSTALLING Crips <==\n $WHITE"
  git clone https://github.com/Manisso/Crips.git
  echo -e "$BOLDR \n==> I  N  S  T  A  L  L  E  D <==\n $WHITE"
  tool
  install
elif [ $choice == 18 ]
then
  echo -e "$RED \n==> INSTALLING OSIF <==\n $WHITE"
  echo -e "$BOLDR \n==>INSTALLING python2 <==\n $WHITE"
  pkg install git python2
  echo -e "$BOLDR \n==> NOW INSTALLING OSIF <==\n $WHITE"
  git clone https://github.com/ciku370/OSIF
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D <--\n $WHITE"
  tool
  install
elif [ $choice == 19 ]
then
  echo -e "$BOLDR \n==> Hope you enjoyed. Hey while you're at it, type in python file.py and checkout the actual project! <==\n $WHITE"
elif [ $choice == 'open-project' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO file.py <==\n $WHITE"
  python file.py
  title
  info
  tool
  install
elif [ $choice == 'run-sniper' ]
then
  echo -e "$BOLDR \n==> BOOTING UP SNIPER <==\n $WHITE"
  cd Sn1per
  bash install.sh
  echo -e "$BOLDR \n==> LIST OF COMMANDS <==\n $WHITE"
  bash sniper --help
  title
  info
  tool
  install
elif [ $choice == 'run-johntheripper' ]
then
  echo -e "$BOLDR \n==> Independent Terminal App that requires arguments, or a user format, to run. Sorry <==\n $WHITE"
  tool
  install
elif [ $choice == 'run-hydra' ]
then
  echo -e "$BOLDR \n==> Independent Terminal App that requires arguments, or a user format, to run. Sorry <==\n $WHITE"
  tool
  install
elif [ $choice == 'run-metasploit' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO METASPLOIT <==\n $WHITE"
  bash metasploit.sh
  tool
  install
elif [ $choice == 'run-sploitego' ]
then
  echo -e "$BOLDR \n==> Independent Terminal App that requires arguments, or a user format, to run. Sorry <==\n $WHITE"
  tool
  install
elif [ $choice == 'run-hunner' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO Hunner <==\n $WHITE"
  cd hunner
  python hunner.py
  title
  info
  tool
  install
elif [ $choice == 'run-sqlmap' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO Sqlmap <==\n $WHITE"
  cd sqlmap-dev
  python sqlmap.py --wizard
  title
  info
  tool
  install
elif [ $choice == 'run-shellphish' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO SHELLPHISH <==\n $WHITE"
  cd shellphish
  bash shellphish.sh
  title
  info
  tool
  install
elif [ $choice == 'run-userrecon' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO userrecon <==\n $WHITE"
  cd userrecon
  bash userrecon.sh
  title
  info
  tool
  install
elif [ $choice == 'run-blackeye' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO BlackEye <==\n $WHITE"
  cd blackeye
  bash blackeye.sh
  title
  info
  tool
  install
elif [ $choice == 'run-instashell' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO InstalShell <==\n $WHITE"
  cd instashell
  bash install.sh
  bash instashell.sh
  title
  info
  tool
  install
elif [ $choice == 'run-saycheese' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO SayCheese <==\n $WHITE"
  cd saycheese
  bash saycheese.sh
  title
  info
  tool
  install
elif [ $choice == 'run-clipboardme' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO ClipboardMe <==\n $WHITE"
  cd clipboardme
  bash clipboardme.sh
  title
  info
  tool
  install
elif [ $choice == 'run-ip-tracer' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO IP-Tracer <==\n $WHITE"
  cd IP-Tracer
  chmod +x install
  sh install
  title
  info
  tool
  install
elif [ $choice == 'run-nmap' ]
then
  echo -e "$BOLDR \n==> Independent Terminal App that requires arguments, or a user format, to run. Sorry <==\n $WHITE"
  title
  info
  tool
  install
elif [ $choice == 'run-red_hawk' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO RED_HAWK <==\n $WHITE"
  cd RED_HAWK
  php rhawk.php
  title
  info
  tool
  install
elif [ $choice == 'run-crips' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO Crips <==\n $WHITE"
  cd Crips
  python2 crips.py
  title
  info
  tool
  install
elif [ $choice == 'run-osif' ]
then
  echo -e "$BOLDR \n==> BOOTING INTO OSIF <==\n $WHITE"
  cd OSIF
  python2 osif.py
  title
  info
  tool
  install
else
  echo -e "$BOLDR \n==> Hmm.. oops seems like we couldn't execute..please re-type bash tools.sh or go to python file.py!<==\n $WHITE"
fi
}

# CALLING THEM
tool
install
