# Data Science Python Project Setup

## Setup

### Linux - Miniconda

```sh
wget -O ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ~/miniconda.sh -b -p ~/miniconda
rm ~/miniconda.sh
```

### Mac OS X - Miniconda

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
conda env create --file environment.yml
conda activate data-science-project
```

## Usage

```sh
conda env update --file environment.yml
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
