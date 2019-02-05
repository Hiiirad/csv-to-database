# Importing CSV File to SQL Database!
[![License](http://img.shields.io/:license-mit-blue.svg)](LICENSE)
![PyPI - Status](https://img.shields.io/pypi/status/Django.svg)

Hi everybody :)

## Getting Started

This program will only works on **Linux** systems and I believe it would be work perfectly on Macbooks. My OS is Ubuntu 18.04 and I design this program to run on all debian-based linux systems. The installation process will be different if you use other linux distributions.

This program import all data of a _CSV_ file to database. (When I say database, I mean _SQL_ database)

### Features

- Using **pyodbc** to connect to your database and read every row using **csv** library and insert them one by one to database.

- You can see [ODBC Documentation](https://docs.microsoft.com/en-us/sql/odbc/reference/introduction-to-sql-and-odbc?view=sql-server-2017)

### Prerequisites
```
sudo apt update && sudo apt upgrade -y
```
```
sudo apt install git
```

### Installing
I prefer using [Anaconda](https://www.anaconda.com/) instead of using [Pip or PyPI](https://pypi.org/), but you decide which is good for you.
 - Using Pip:
    - ```sudo apt install python3-pip```
    - ```pip install pip```
    - ```pip install -r requirements.txt```
 - Using Anaconda: Installation process is completely documented [here](https://docs.anaconda.com/anaconda/install/linux/).

### Upgrading
* Pip:
    ```
    pip install -U pip
    ```
* Anaconda:
    ```
    conda update --all
    ```

### Version check to verify installation
* Pip:
    ```
    pip --version
    ```
* Anaconda:
    ```
    conda --version
    ```

## Usage
```
https://github.com/Hiiirad/csv-to-database.git
```
```
cd csv-to-database/
```
```
python csv-to-database.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
