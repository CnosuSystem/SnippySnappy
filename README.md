# Snippy Snappy

A collection of Cnosu's code snippets. Basically a library.

## Installation

If you have Git installed, you can install the latest version directly from this repository using:

```
pip install "git+https://github.com/CnosuSystem/SnippySnappy.git"
```

If you installed the project but want to update it to the latest version, use:

```
pip install --upgrade "git+https://github.com/CnosuSystem/SnippySnappy.git"
```

No PyPi install is planned, as this is a minor/niche project and I prefer to keep it off PyPi.

If you don't have Git, you can build the project from source.

## Building from Source

### 1. Clone the repository

Make sure you have Git installed, then clone the repository:

```
git clone https://github.com/CnosuSystem/SnippySnappy.git
cd SnippySnappy
```

If you don't have Git, simply download the raw source .zip file from GitHub and put it in your preffered directory. Then open it in the terminal.

### 2. Install the project

Install the project and its dependencies with:

```
python -m pip install .
```

The project's package configuration will install its required dependencies (click>=8.0 and colorama>=0.4.6) and register the a-dex command.

## Usage

Functions and their usage:
* get_id(string, len)
  * string - text to get hashed
  * len - how many characters of this hash should get returned (set 0 for the whole one)

## Changelog

For the changelog, please reffer to the [CHANGELOG.md](https://github.com/CnosuSystem/SnippySnappy/blob/main/CHANGELOG.md) file in the root of this project's GitHub repository.

## Authors

* [@Cnosu](https://spacehey.com/cnosu) - The guy that did all the coding

## License

This project is licensed under the [GNU GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text) - see the [LICENSE.md](https://github.com/CnosuSystem/SnippySnappy?tab=GPL-3.0-1-ov-file) file for details.