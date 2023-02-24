sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python3-lxml python3-pygame
pip3 install PyYAML mavproxy --user

LINE='export PATH="$PATH:$HOME/.local/bin"'
if ! grep -qF "$LINE" ~/.bashrc ; 
    then 
        echo "$LINE" >> ~/.bashrc  ;
fi
source ~/.bashrc