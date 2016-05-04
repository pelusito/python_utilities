##############################################################
####     SHELL SCRIPT used to ejecute ScrpitLista.py     #####
##############################################################

clear # clear the terminal window

python ./*/ScriptListas.py # ejecute the python program

cat ./*.csv  # before close python program show in terminal the csv archive created 

rm ./*.csv # delete the csv archive

sleep 5 # wait 5 seconds in order to be able to see the table

clear # clear the window
