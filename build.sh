
rm -rf build dist main.spec

cd bindings 
go build -buildmode=c-shared -o library.so main.go 
cd ..


python -m PyInstaller -n jam  --hidden-import=inquirer --hidden-import=shellingham  --hidden-import=readchar  --copy-metadata readchar  --icon assets/icon.ico main.py

mkdir dist/jam/_internal/bindings
mkdir dist/jam/_internal/assets/
cp assets/icon.png ./dist/jam/_internal/assets/
cp bindings/library.h bindings/library.so ./dist/jam/_internal/bindings/
cp install.sh ./dist/jam/


cd dist/jam
chmod +x install.sh

./jam
