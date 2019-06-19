

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
                   Top Tools, Top Developers, Free,
                   Tool Download Version
                   MADE_BY: ARACADE_RISE,
                   "
 
echo -e "$RED \n--> Choose A Tool <--\n $WHITE"

echo -e "$BLUE \n1. Something $WHITE"
choice=1,2,3
read -p ">> Your Choice >> " choice 

if [ $choice == 1 ]
then
  echo -e "$RED \n-->INSTALLING<--\n $WHITE"
  apt update
  git clone https://github.com/ARACADERISE/_Tool-Console_.git
fi
