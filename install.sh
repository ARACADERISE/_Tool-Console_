
INSTALL_DIR=/_Tool-Console_
LOOT_DIR=/usr/share/sniper/loot
PLUGINS_DIR=/usr/share/sniper/plugins
GO_DIR=~/go/bin

echo -e "$OKGREEN + -- --=[Type 'YES' to continue$RESET"
read answer

mkdir -p $INSTALL_DIR 2> /dev/null
mkdir -p $LOOT_DIR 2> /dev/null
mkdir $LOOT_DIR/domains 2> /dev/null
mkdir $LOOT_DIR/screenshots 2> /dev/null
mkdir $LOOT_DIR/nmap 2> /dev/null
mkdir $LOOT_DIR/reports 2> /dev/null
mkdir $LOOT_DIR/output 2> /dev/null
mkdir $LOOT_DIR/osint 2> /dev/null
cp -Rf * $INSTALL_DIR 2> /dev/null
cd $INSTALL_DIR

echo -e "$OKORANGE + -- --=[Installing Tool-Console$RESET"
apt update && apt upgrade
pkg install python3

echo -e "$OKORANGE + -- --=[Setting up...$RESET"
git clone https://github.com/ARACADE_RISE/_Tool-Console_.git
echo -e "$OKORANGE + -- --=[Setting up Ubuntu$RESET"
apt-get update && apt-get upgrade -y
apt-get install wget -y
apt-get install proot -y
apt-get install git -y
cd ~
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
cd ubuntu-in-termux
chmod +x ubuntu.sh
./ubuntu.sh
cp ~/ubuntu-in-termux/resolv.conf ~/ubuntu-in-termux/ubuntu-fs/etc/
./start.sh

echo -e "$OKORANGE + -- --=[Done!$RESET"
echo -e "$OKORANGE + -- --=[To run, type python file.py! $RESET"
