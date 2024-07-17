package db

import (
	"encoding/json"
	"fmt"
	"io"
	manager "jam/lib/manager"
	"os"
)

type AppImageReg struct {
	ID         string `json:"id"`
	Name       string `json:"name"`
	File       string `json:"file"`
	DotDesktop string `json:"DotDesktop"`
	Icon       string `json:"icon"`
	Version    string `json:"version"`
}

type AppListItem struct {
	Name    string `json:"name"`
	File    string `json:"file"`
	Version string `json:"version"`
}

func GetDbfilePath() string {
	homeDir := manager.GetHomeDir()
	return homeDir + "/Application/jam_db/db.json"
}

func Readjsondb() []AppImageReg {
	dbFilePath := GetDbfilePath()

	jsonFile, err := os.Open(dbFilePath)

	if err != nil {
		fmt.Println(err)
	}

	defer jsonFile.Close()

	byteValue, _ := io.ReadAll(jsonFile)

	var appimageReg []AppImageReg

	json.Unmarshal(byteValue, &appimageReg)

	return appimageReg
}

func WritejsonDb(content []AppImageReg) {
	path := GetDbfilePath()
	result, err := json.Marshal(content)
	if err != nil {
		fmt.Println(err)
	}
	os.WriteFile(path, result, 0644)
}

func AppendDB(name, icon, file, dotDesktop, version, id string) {

	db := Readjsondb()

	db = append(db, AppImageReg{Name: name, Icon: icon, DotDesktop: dotDesktop, Version: version, ID: id, File: file})

	WritejsonDb(db)

}

func PopDB(id string) {

}

func AppDbList() []AppListItem {
	db := Readjsondb()
	var AppList []AppListItem

	for _, i := range db {
		append(AppList, AppListItem{Name: i.Name, File: i.File, Version: i.Version})
	}
	return AppList
}
