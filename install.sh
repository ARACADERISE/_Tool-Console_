
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

echo -e "$OKORANGE + -- --=[Setting up...$RESET"
git clone https://github.com/ARACADE_RISE/_Tool-Console.git
echo -e "$OKORANGE + -- --=[Setting up Ruby...$RESET"
dpkg-reconfigure ruby

echo -e "$OKORANGE + -- --=[Cleaning up old extensions...$RESET"
rm -Rf $PLUGINS_DIR 2> /dev/null
mkdir $PLUGINS_DIR 2> /dev/null
cd $PLUGINS_DIR
mkdir -p $PLUGINS_DIR/nmap_scripts/ 2> /dev/null
mkdir -p $GO_DIR 2> /dev/null

echo -e "$OKORANGE + -- --=[Downloading extensions...$RESET"
echo -e "$OKORANGE + -- --=[Done!$RESET"
echo -e "$OKORANGE + -- --=[To run, type 'sniper'! $RESET"
