#!/bin/bash



sudo apt-get -y install -f;
sudo apt-get -y upgrade;
sudo apt-get -y update;
sudo apt-get -y install zlib1g-dev python-setuptools  build-essential  libssl-dev libxml2-dev libxslt1-dev  python-dev libzmq-dev  libpq-dev;
sudo apt-get -y upgrade;

cd ~/
curl -L http://www.python.org/ftp/python/2.7.2/Python-2.7.2.tgz > Python-2.7.2.tgz
tar xzf Python-2.7.2.tgz
cd Python-2.7.2
./configure
make altinstall prefix=~/usr/local exec-prefix=~/usr/local
alias python='~/usr/local/bin/python2.7'


curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
python get-pip.py
alias pip=~/usr/local/bin/pip

sudo apt-get install openjdk-7-jdk


mongo_ppa=/etc/apt/sources.list.d/mongodb-org-3.0.list
##installs mongodb if it is not already installed

if [ ! -f "$mongo_ppa" ]; then echo "The Repository does Not Exist";
    # commands to add the ppa ...
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
    echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb.list
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install mongodb-org
fi;


mkdir -p ~/Develop/Workspaces/mgi;
mkdir -p ~/Develop/Workspaces/Envs;
git clone https://github.com/usnistgov/MDCS.git ~/Develop/Workspaces/mgi/mdcs;
sudo apt-get install virtualenvwrapper;
pip install virtualenvwrapper;

# export WORKON_HOME={$HOME}/Develop/Envs;
# mkdir -p $WORKON_HOME;
# echo "here";
# . {$HOME}/usr/local/bin/virtualenvwrapper.sh;

#mkvirtualenv mgi;



cat > ${HOME}/Develop/Workspaces/mgi/mdcs/conf/mongodb.conf  <<EOL
dbpath=${HOME}/Develop/Workspaces/mgi/mdcs/data/db 
bind_ip = 127.0.0.1 
journal=true 
EOL





