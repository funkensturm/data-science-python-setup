# Data Science Python Project Setup

A minimal setup to let you crunch numbers like a pro.

Read the full article here:

If you like to use the repository as a blueprint for your own projects just follow the steps below.

Replace `data-science-project` with you project/environment name in:
- .travis.yml
- environment.yml
- README.md
- setup.py

Replace the package information in the setup.py with your own.


## Setup

### Miniconda

Skip this step if you have Anaconda or Miniconda installed already!

#### Linux

```sh
wget -O ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ~/miniconda.sh -b -p ~/miniconda
rm ~/miniconda.sh
```

#### Mac OS X

```sh
curl -fSL -o ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash ~/miniconda.sh -b -p ~/miniconda
rm ~/miniconda.sh
```

### Project

```sh
git clone https://github.com/datasciencejob-de/data-science-python-setup.git
```

```sh
conda env create -f environment.yml
conda activate data-science-project
```


## Usage

```sh
conda env update -f environment.yml
conda activate data-science-project
jupyter notebook
```


## Data

See the [Data README](/data#readme) for more infos.


## Tests

```sh
flake8 # Run code style checks
pytest # Run the tests
```
