

GREEN="\033[92m"
RED="\033[91m"
BLUE="\033[94m"
WHITE="\033[0;37m"
RUN=$true

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
while [ $RUN == $true ]
do
echo -e "$RED \n--> Choose A Tool <--\n $WHITE"
echo -e "$BLUE \n-->TOOLS<--\n "
echo -e "$BLUE\n1.Sniper\n2.JohnTheRipper\n3.Hydra\n4.Metasploit\n5.sploitego\n6.Hunner\n7.sqlmap\n8.shellphish $WHITE"
read -p "Your Choice >> " choice 
choice=1,2,3,4,5,6,7,8,9,10
$RUN=$false
end
done

$RUN=$false

if [ $choice == 1 ]
then
  echo -e "$RED \n-->INSTALLING SNIPER<--\n $WHITE"
  git clone https://github.com/1N3/Sn1per
  echo -e "$BLUE \n1.cd Sniper\n
  2.bash install.sh"
elif [ $choice == 2 ]
then
  echo -e "$RED \n-->INSTALLING JohnTheRipper<--\n $WHITE"
  git clone https://github.com/magnumripper/JohnTheRipper.git
  echo -e "$BLUE \n1.cd JohnTheRipper\n2.cd run"
elif [ $choice == 3 ]
then
  echo -e "$RED \n-->INSTALLING HYDRA<--\n $WHITE"
  pkg install hydra
elif [ $choice == 4 ]
then
  echo -e "$RED \n-->INSTALLING METASPLOIT<--\n $WHITE"
  pkg install unstable-repo
  pkg install metasploit
elif [ $choice == 5 ]
then
  echo -e "$RED \n-->INSTALLING sploitego<--\n $WHITE"
  echo -e "$WHITE trying to find package..."
  echo -e "$RED \n-->COULD NOT FIND<--\n"
  echo -e "try visiting $BLUEhttps://github.com/allfro/sploitego"
elif [ $choice == 6 ]
then
  echo -e "$RED \n-->INSTALLING Hunner<--\n $WHITE"
  git clone https://github.com/b3-v3r/Hunner
elif [ $choice == 7 ]
then
  ehco -e "$RED \n-->INSTALLING sqlmap<--\n $WHITE"
  git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
elif [ $choice == 8 ]
then
  ehco -e "$RED \n-->INSTALLING shellphish<--\n $WHITE"
  git clone https://github.com/thelinuxchoice/shellphish
fi
