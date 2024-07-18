
rm -rf build dist main.spec

python -m PyInstaller -n jam  --hidden-import=inquirer --hidden-import=readchar --copy-metadata readchar --icon assets/icon.ico main.py

mkdir dist/jam/_internal/bindings

cp bindings/library.h bindings/library.so ./dist/jam/_internal/bindings/


cd dist/jam

./jam
