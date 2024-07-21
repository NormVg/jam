


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

function cleanbuild(){

rm -rf build dist jam.spec venv

}

function check_python() {
  if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 to proceed."
    exit 1
  fi
}

function build(){

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

rm -rf build dist jam.spec

python -m PyInstaller -n jam  --hidden-import=inquirer --hidden-import=shellingham  --hidden-import=readchar  --copy-metadata readchar  --icon assets/icon.ico main.py

mkdir dist/jam/_internal/bindings
mkdir dist/jam/_internal/assets/
cp assets/icon.png ./dist/jam/_internal/assets/
cp bindings/library.h bindings/library.so ./dist/jam/_internal/bindings/
cp install.sh ./dist/jam/


cd dist/jam

./jam

}

function install(){
build

echo "Installing Just AppImage Manager."
cp -r jam  _internal ~/JAM/

cd ../../

cleanbuild

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

echo "Welcome too installer of AppImageManager"
read -p "Do you want to proceed? (y/n): " choice

check_python

case "$choice" in 
  y|Y ) install ;;
  n|N ) echo "JAM installation cancelled.";;
  * ) echo "Invalid choice. Please enter y or n.";;
esac




