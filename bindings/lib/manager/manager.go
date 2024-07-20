package manager

import (
	"errors"
	"fmt"
	"math/rand"
	"os"
	"path/filepath"
)

func RandSting() string {
	str := "67bcdwxysav345tu890z12qrefghijklmnop"

	shuff := []rune(str)

	// Shuffling the string
	rand.Shuffle(len(shuff), func(i, j int) {
		shuff[i], shuff[j] = shuff[j], shuff[i]
	})

	// Displaying the random string
	randID := string(shuff)

	return randID
}

func WriteMyFile(path, content string) {
	os.WriteFile(path, []byte(content), 0644)
}

func GetHomeDir() string {
	dirname, err := os.UserHomeDir()
	if err != nil {
		fmt.Println(err)
	}

	return dirname
}

func CreateFolderAndFile(name string, file bool) {
	if file {
		if _, err := os.Stat(name); errors.Is(err, os.ErrNotExist) {

			f, err := os.OpenFile(name, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
			if err != nil {
				fmt.Println(err)
			}

			f.Close()

		}

	} else {
		if _, err := os.Stat(name); errors.Is(err, os.ErrNotExist) {

			err := os.Mkdir(name, os.ModePerm)

			if err != nil {
				fmt.Println(err)
			}

		}

	}
}

func CreateApplicationFolder() {
	homeDir := GetHomeDir()

	CreateFolderAndFile(homeDir+"/Application", false)
	CreateFolderAndFile(homeDir+"/Application/jam_db", false)
	CreateFolderAndFile(homeDir+"/Application/jam_db/icons", false)
	CreateFolderAndFile(homeDir+"/.local/share/applications/jam/", false)
	CreateFolderAndFile(homeDir+"/Application/jam_db/db.json", true)

}

func WriteDotDesktop(name, Config string) string {

	randID := RandSting()

	homeDir := GetHomeDir()
	myDotPath := homeDir + "/.local/share/applications/jam/" + name + "-" + randID + ".desktop"
	WriteMyFile(myDotPath, Config)

	return myDotPath
}

func CreateDotDesktopFile(name, path, icon, version string) string {
	const file_data = `[Desktop Entry]
Name= %s
Comment=shortcut Video Editor software
Exec= %s
Icon= %s
Version= %s
Terminal=false
Type=Application
`
	FileConfig := fmt.Sprintf(file_data, name, path, icon, version)
	myDotPath := WriteDotDesktop(name, FileConfig)
	return myDotPath
}

func MoveAppImageFile(path, name string) (string, string) {
	randID := RandSting()
	homeDir := GetHomeDir()
	newName := randID + "-" + name
	movePath := homeDir + "/Application/" + newName + ".AppImage"

	r, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer r.Close()
	w, err := os.Create(movePath)
	if err != nil {
		panic(err)
	}
	defer w.Close()
	w.ReadFrom(r)

	os.Chmod(movePath, 0755)

	return movePath, newName
}

func MoveAppImageIconFile(path, name string) string {
	randID := RandSting()
	homeDir := GetHomeDir()
	extension := filepath.Ext(path)

	movePath := homeDir + "/Application/jam_db/icons/" + randID + "-" + name + extension

	r, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer r.Close()
	w, err := os.Create(movePath)
	if err != nil {
		panic(err)
	}
	defer w.Close()
	w.ReadFrom(r)

	os.Chmod(movePath, 0755)

	return movePath
}
