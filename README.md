		     ▄▄▄ ▄▄▄▄▄▄ ▄▄   ▄▄
		    █   █      █  █▄█  █
		    █   █  ▄   █       █
		 ▄  █   █ █▄█  █       █
		█ █▄█   █      █       █
		█       █  ▄   █ ██▄██ █
		█▄▄▄▄▄▄▄█▄█ █▄▄█▄█   █▄█

# Just AppImage Manager (J.A.M)

Just AppImage Manager (J.A.M) is a CLI tool for sudo installing AppImage packages on Linux. This tool is developed using Python and Go-lang, combined via a shared-C library. The CLI interface leverages Python libraries such as Rich, Typer, Inquirer, and Yaspin, while Go-lang handles the core functionalities.

## Tested Environments

| Distribution     | Status  |
|------------------|---------|
| Arch Linux       | ✅ Tested |
| Endeavour OS     | ✅ Tested |
| Pop OS           | ✅ Tested |
| Ubuntu           | ✅ Tested |
| Linux Mint       | ✅ Tested |
| More to be tested soon... | ⏳ |

## TODO
- edit run command
- run app from jam


## Installation

To install Just AppImage Manager (J.A.M), follow these steps:

### Pre-requirements 
	- python3
	- python's venv y

```sh
wget https://github.com/NormVg/jam/releases/download/v1.0.3/jam.zip

unzip jam.zip

cd package

chmod +x ./install.sh

./install.sh

```

Follow the instructions provided during the installation process.

## Usage

To get information and help about J.A.M, use the following command:

```sh
jam --help
```

## Contribution and Support

This is a new tool, so kindly report any issues you face. For contributions, join the [Discord server](https://discordapp.com/users/943907992145911818) or just DM me, and we can have a talk.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
