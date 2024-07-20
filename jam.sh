cd bindings 
go build -buildmode=c-shared -o library.so main.go 
cd ..

python main.py $@