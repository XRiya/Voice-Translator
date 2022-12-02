#26.09.2021 -- Set up Git
#Sources: 
#https://linuxtechlab.com/how-to-install-github-on-ubuntu-step-by-step/

#1. Install
sudo apt-get install git

#Registered data on GitHub
git config --global user.name "rmaier"
git config --global user.email "git@ribeiromaier.de"

#2. Setting up SSH

cd ~/.ssh
ssh-keygen -t rsa -C "git@ribeiromaier.de"
# no passphrase used 29.09.2021

#on GitHub: 
#Account Settings → SSH Keys → Add another public key
#C & P content of the id_xxx_.pub file
ssh-add id_git.ribeiromaier.de

#3. Use git 
#From GitHub doc

echo "# 2021_Shellhacks_Hearandlisten" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:rmaier/2021_Shellhacks_Hearandlisten.git
git push -u origin main



#####

#4. Clone a Git repository
git init
git clone git@github.com:rmaier/2021_Shellhacks_Hearandlisten.git
