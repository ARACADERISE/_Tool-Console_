
INSTALL_DIR=/_Tool-Console_

echo -e "$OKGREEN \n-->Type 'yes' to continue<--\n$RESET"
read answer

echo -e "$OKORANGE \n-->Installing Requirement<--\n$RESET"
apt update && apt upgrade
https://github.com/ARACADERISE/_Tool-Console_/blob/master/install.sh
pkg install python

echo -e " \n-->Stored in $INSTALL_DIR<--\n$RESET"

echo -e "$OKORANGE \n-->Setting up...<--\n$RESET"
git clone https://github.com/ARACADERISE/_Tool-Console_.git
echo -e "$OKORANGE \n-->Setting up Ubuntu<--\n$RESET"
apt-get update && apt-get upgrade -y
apt-get install wget -y
apt-get install proot -y
apt-get install git -y
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
echo -e "\n$OKORANGE To use ubuntu \ncd ubuntu-in-termux \nchmod +x ubuntu.sh \n./ubuntu.sh \ncp ~/ubuntu-in-termux/resolv.conf ~/ubuntu-in-termux/ubuntu-fs/etc/
./start.sh\n"
echo -e "$OKORANGE Setting Up Kali...$RESET"
pkg install wget
wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter
chmod +x kalinethunter
bash kalinethunter

echo -e "$OKORANGE \n-->Done!<--\n$RESET"
echo -e "$OKORANGE \n-->To run, type python file.py!<--\n $RESET"

echo -e "\nE  N  J  O  Y\n $RESET"
