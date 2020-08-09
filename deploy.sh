sudo pacman -S python
python -m pip install discord.py youtube-dl beautifulsoup4
echo "Gice the discord api key"
read varname
touch apikey.file
echo $varname >> apikey.file

