

GREEN="\033[92m"
RED="\033[91m"
BLUE="\033[94m"
WHITE="\033[0;37m"
BOLDR="\033[1;31m"

echo -e "$GREEN $RESET\n\n"

echo -e "
      ___ __   __  __        ___ __  __ _ ____  __  __   ____ 
    (_  _/  \ /  \(  )  ___ / __/  \(  ( / ___)/  \(  ) (  __)
      )((  O (  O / (_/(___( (_(  O /    \___ (  O / (_/\) _) 
     (__)\__/ \__/\___/     \___\__/\_)__(____/\__/\____(____) V.1.0.1
                   Top Tools, Top Developers, Free,
                   Tool Download Version
                   MADE_BY: ARACADE_RISE,
                   "
echo -e "$BOLDR \n-->NOTE: You can only download one at a time<--\n"                   

echo -e "$RED \n--> Choose A Tool <--\n $WHITE"
tool()
{
echo -e "$BLUE \n-->TOOLS<--\n "
echo -e "$BLUE\n1.Sniper\n2.JohnTheRipper\n3.Hydra\n4.Metasploit\n5.sploitego\n6.Hunner\n7.sqlmap\n8.shellphish $WHITE"
read -p "Your Choice >> " choice 
}

install()
{
if [ $choice == 1 ]
then
  echo -e "$RED \n-->INSTALLING SNIPER<--\n $WHITE"
  git clone https://github.com/1N3/Sn1per
  echo -e "$BLUE \n1.cd Sniper\n2.bash install.sh"
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D<--\n $WHITE"
  tool
  install
elif [ $choice == 2 ]
then
  echo -e "$RED \n-->INSTALLING JohnTheRipper<--\n $WHITE"
  git clone https://github.com/magnumripper/JohnTheRipper.git
  echo -e "$BLUE \n1.cd JohnTheRipper\n2.cd run"
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D<--\n $WHITE"
  tool
  install
elif [ $choice == 3 ]
then
  echo -e "$RED \n-->INSTALLING HYDRA<--\n $WHITE"
  pkg install hydra
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D<--\n $WHITE"
  tool
  install
elif [ $choice == 4 ]
then
  echo -e "$RED \n-->INSTALLING METASPLOIT<--\n $WHITE"
  pkg install unstable-repo
  pkg install metasploit
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D<--\n $WHITE"
  tool
  install
elif [ $choice == 5 ]
then
  echo -e "$RED \n-->INSTALLING sploitego<--\n $WHITE"
  echo -e "$WHITE trying to find package..."
  echo -e "$RED \n-->COULD NOT FIND<--\n"
  echo -e "try visiting $BLUEhttps://github.com/allfro/sploitego"
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D<--\n $WHITE"
  tool
  install
elif [ $choice == 6 ]
then
  echo -e "$RED \n-->INSTALLING Hunner<--\n $WHITE"
  git clone https://github.com/b3-v3r/Hunner
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D<--\n $WHITE"
  tool
  install
elif [ $choice == 7 ]
then
  echo -e "$RED \n-->INSTALLING sqlmap<--\n $WHITE"
  git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D<--\n $WHITE"
  tool
  install
elif [ $choice == 8 ]
then
  echo -e "$RED \n-->INSTALLING shellphish<--\n $WHITE"
  git clone https://github.com/thelinuxchoice/shellphish
  echo -e "$BOLDR \n--> I  N  S  T  A  L  L  E  D<--\n $WHITE"
  tool
  install
else
  echo -e "$BOLDR \n--> ALREADY INSTALLED<--\n"
fi
}

# CALLING THEM
tool
install
