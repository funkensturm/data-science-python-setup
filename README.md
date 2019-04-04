# Data Science Python Project Setup

## Setup

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
