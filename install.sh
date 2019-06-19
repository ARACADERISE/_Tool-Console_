
INSTALL_DIR=/_Tool-Console_
LOOT_DIR=/usr/share/sniper/loot
PLUGINS_DIR=/usr/share/sniper/plugins
GO_DIR=~/go/bin

echo -e "$OKGREEN Type 'YES' to continue$RESET"
read answer

echo -e "$OKORANGE Installing Requirement$RESET"
apt update && apt upgrade
pkg install python

echo -e " -->Stored in $INSTALL_DIR<--$RESET"

echo -e "$OKORANGE Setting up...$RESET"
git clone https://github.com/ARACADERISE/_Tool-Console_.git
echo -e "$OKORANGE + -- --=[Setting up Ubuntu$RESET"
apt-get update && apt-get upgrade -y
apt-get install wget -y
apt-get install proot -y
apt-get install git -y
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
echo -e "OKORANGE To use ubuntu \ncd ubuntu-in-termux \nchmod +x ubuntu.sh \n./ubuntu.sh \ncp ~/ubuntu-in-termux/resolv.conf ~/ubuntu-in-termux/ubuntu-fs/etc/
./start.sh"
echo -e "$OKORANGE Setting Up Kali...$RESET"
pkg install wget
wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter
chmod +x kalinethunter
bash kalinethunter

echo -e "$OKORANGE + -- --=[Done!$RESET"
echo -e "$OKORANGE + -- --=[To run, type python file.py! $RESET"
