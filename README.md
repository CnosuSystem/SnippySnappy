# Snippy Snappy

A collection of Cnosu's code snippets. Basically a library.


## Installation

If you have Git installed, you can install the latest version directly from this repository using:

```bash
pip install "git+https://github.com/CnosuSystem/SnippySnappy.git"
```

If you installed the project but want to update it to the latest version, use:

```bash
pip install --upgrade "git+https://github.com/CnosuSystem/SnippySnappy.git"
```

No PyPi install is planned, as this is a minor/niche project and I prefer to keep it off PyPi.

If you don't have Git, you can build the project from source.


## Building from Source

### 1. Clone the repository

Make sure you have Git installed, then clone the repository:

```bash
git clone https://github.com/CnosuSystem/SnippySnappy.git
cd SnippySnappy
```

If you don't have Git, simply download the raw source .zip file from GitHub and put it in your preffered directory. Then open it in the terminal.

### 2. Install the project

Install the project with:

```bash
python -m pip install .
```

You can also use this command to install it as an editable developer build (will allow you to use ruff and pytest).

```bash
pip install -e ".[dev]"
```


## Usage

See [USAGE.md](https://github.com/CnosuSystem/SnippySnappy/blob/main/USAGE.md) for information on how to use specific functions.


## Changelog

For the changelog, please reffer to the [CHANGELOG.md](https://github.com/CnosuSystem/SnippySnappy/blob/main/CHANGELOG.md) file in the root of this project's GitHub repository.


## Authors

* [@Cnosu](https://spacehey.com/cnosu) - The guy that did all the coding


## License

This project is licensed under the [GNU GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text) - see the [LICENSE.md](https://github.com/CnosuSystem/SnippySnappy?tab=GPL-3.0-1-ov-file) file for details.


## Acknowledgements

* ANSI colors inspired by and based on the [tartley/colorama](https://github.com/tartley/colorama) GitHub repo