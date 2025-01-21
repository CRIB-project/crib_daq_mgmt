# CRIB DAQ management scripts

CRIB currently uses [babirl + MPV](https://ribf.riken.jp/RIBFDAQ/index.php?DAQ/Information) configuration.
Useful scripts have been created using python and shellscript for ease of set-up and management.

As for the python environment, we are using ["uv" package manager](https://docs.astral.sh/uv/).
Please install the uv in advance.

# Usage

It assume the scripts are stored in $HOME/exp directory, that is:

```shell
> cd ~
> tree
.
├── exp
│   ├── expname1
│   │   ├── file of this repository

...

│   │   └── file of this repository
│   ├── expname2

...
```

Also the data files (ridf files) are assumed to be stored ./ridf and /Data directory.
The /Data directory is assumed to be mounted by external storage, and if you want to change the name, please modify the "bin/setup_environment" file.

```shell
> cd ~/exp/expname
> tree -L 1 ridf
ridf
├── ****.ridf

...

└── ****.ridf

> tree -L 1 /Data/expname
/Data/expname
├── ****.ridf

...

└── ****.ridf
```


After checking these requirements, you can start to make the environment by coping the files from previous experiment or `git clone` from GitHub repository.

- Copy from previous experiment
```shell
> cd ~/exp
> cp -r expname_pre expname_new
```

- Clone from GitHub repository

```shell
> cd ~/exp
> git clone https://github.com/okawak/crib_daq_mgmt.git expname
```

# Initial setup

The .bashrc/.zshrc setup

```shell
export EXP_NAME="hoge"
```

Initial setup

```shell
> cd bin
> ./setup_environment
```

## useful scripts

```sh
# initialize the babirl process
sudo ./bin/init_babirl

# kill the babirl process
sudo ./bin/kill_babirl

# restart the MPV process
./bin/mpvrestart

# change the event build size
./bin/set_EBsize [number]

# setup new experiment environment
./bin/setup_environment

# backup the data file to the analysis PC
./bin/do_sync.sh
```
