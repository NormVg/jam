


mkdir ~/JAM


baner="
		     ▄▄▄ ▄▄▄▄▄▄ ▄▄   ▄▄
		    █   █      █  █▄█  █
		    █   █  ▄   █       █
		 ▄  █   █ █▄█  █       █
		█ █▄█   █      █       █
		█       █  ▄   █ ██▄██ █
		█▄▄▄▄▄▄▄█▄█ █▄▄█▄█   █▄█

 ╦┬ ┬┌─┐┌┬┐  ╔═╗┌─┐┌─┐╦┌┬┐┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┌─┐┌─┐┬─┐
 ║│ │└─┐ │   ╠═╣├─┘├─┘║│││├─┤│ ┬├┤   ║║║├─┤│││├─┤│ ┬├┤ ├┬┘
╚╝└─┘└─┘ ┴   ╩ ╩┴  ┴  ╩┴ ┴┴ ┴└─┘└─┘  ╩ ╩┴ ┴┘└┘┴ ┴└─┘└─┘┴└─

"

echo "$baner"


function install(){

echo "Installing Just AppImage Manager."
cp -r jam  _internal ~/JAM/

cd ~/JAM/

mypath=$(pwd)

export PATH=$PATH:$mypath

echo ""
  echo "Add the following line to your shell configuration file (e.g., ~/.bashrc, ~/.zshrc): "
  echo ""
  echo "export PATH=\$PATH:$mypath"
  echo ""
  echo "Then run 'source ~/.bashrc' (or 'source ~/.zshrc') to apply the changes."

}


read -p "Do you want to proceed? (y/n): " choice

case "$choice" in 
  y|Y ) install ;;
  n|N ) echo "JAM installation cancelled.";;
  * ) echo "Invalid choice. Please enter y or n.";;
esac




