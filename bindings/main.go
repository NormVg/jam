package main

import (
	"C"
	"fmt"
)
import (
	"jam/lib/db"
	manager "jam/lib/manager"
)

func SetUpApp() {

	manager.CreateApplicationFolder()

}

//export apinstall
func apinstall(pyname *C.char, pyfile *C.char, pyicon *C.char, pyversion *C.char) {
	SetUpApp()

	name := C.GoString(pyname)
	file := C.GoString(pyfile)
	icon := C.GoString(pyicon)
	version := C.GoString(pyversion)

	fmt.Println(version, name, file, icon)

	file, id := manager.MoveAppImageFile(file, name)
	icon = manager.MoveAppImageIconFile(icon, name)
	myDotPath := manager.CreateDotDesktopFile(name, file, icon, version)

	db.AppendDB(name, icon, file, myDotPath, version, id)
}

//export aplist
func aplist() {
	SetUpApp()

	fmt.Println("list command in go")
}

//export apremove
func apremove() {
	SetUpApp()
	fmt.Println("remove command in go")
}

//export apupdate
func apupdate() {
	SetUpApp()
	fmt.Println("update command in go")
}

//export ping
func ping() *C.char {
	SetUpApp()
	return C.CString("pong")
}

func main() {

}
