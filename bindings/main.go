package main

import (
	"C"
)
import (
	"encoding/json"
	"jam/lib/db"
	manager "jam/lib/manager"
	"log"
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

	file, id := manager.MoveAppImageFile(file, name)
	icon = manager.MoveAppImageIconFile(icon, name)
	myDotPath := manager.CreateDotDesktopFile(name, file, icon, version)

	db.AppendDB(name, icon, file, myDotPath, version, id)
}

//export aplist
func aplist() *C.char {
	SetUpApp()
	mydb := db.AppDbList()

	jsonData, err := json.Marshal(mydb)
	if err != nil {
		log.Fatal(err)
	}

	return C.CString(string(jsonData))

}

//export apremove
func apremove(pyid *C.char) {
	SetUpApp()
	id := C.GoString(pyid)
	db.PopDB(id)
}

//export apupdate
func apupdate(pyname, pyfile, pyicon, pyversion, pyid *C.char) {
	SetUpApp()
	name := C.GoString(pyname)
	file := C.GoString(pyfile)
	icon := C.GoString(pyicon)
	version := C.GoString(pyversion)
	id := C.GoString(pyid)

	fileNew, idNew := manager.MoveAppImageFile(file, name)

	iconNew := manager.MoveAppImageIconFile(icon, name)

	myDotPathNew := manager.CreateDotDesktopFile(name, fileNew, iconNew, version)

	db.PopDB(id)

	db.AppendDB(name, iconNew, fileNew, myDotPathNew, version, idNew)
}

//export ping
func ping() *C.char {
	SetUpApp()
	return C.CString("pong")
}

func main() {

}
