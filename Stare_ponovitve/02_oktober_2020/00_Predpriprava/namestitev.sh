#!/bin/bash
echo "Zagon skripte..."

echo "Priprava git..."

echo "Vnesite vaše ime:"
read user_name
echo Vneseno je ime: $user_name

echo "Vnesite email:"
read email
echo Vnesen email: $email

git config --global user.name $user_name
git config --global user.email $email
git config --global color.ui auto

git --version

echo "Nova mapa analitika2"
cd ~ && mkdir analitika2

echo "Ustvarjanje mape clean_dir in work_dir"
cd ~/analitika2 && mkdir clean_dir && mkdir work_dir

echo "Priprava git v clean dir..."
cd ~/analitika2/clean_dir && git init && git remote add origin https://github.com/leon11s/python-analitika-2-public.git && git remote -v
cd ~/analitika2/clean_dir/ && git pull origin master
echo "clean_dir pripravljen..."

echo "Priprava git v work_dir..."
echo "Prilepite svoj github repoziorji link:"
read link
cd ~/analitika2/work_dir && git init && git remote add origin $link && git remote -v
cd ~/analitika2/work_dir/ && git pull origin master
cp ~/analitika2/clean_dir/

echo "clean_dir pripravljen..."

echo "Kopiranje..."
cp -r ~/analitika2/clean_dir/Del_* ~/analitika2/work_dir/
cd ~/analitika2/work_dir/ && git add . && git commit -m "First commit" && git push origin master


echo "Nastavitve koncane"
echo "Odpiranje Jupyter notebook..."
cd ~/analitika2/ && jupyter notebook