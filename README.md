# CRIB DAQ management scripts

CRIB currently uses [babirl + MPV](https://ribf.riken.jp/RIBFDAQ/index.php?DAQ/Information) configuration.
Useful scripts have been developed using `Python` and `Shellscript` for ease of set-up and management.

As for the python environment, we are using ["uv" package manager](https://docs.astral.sh/uv/).
Please install the `uv` in advance.

# Usage

It assume the scripts are stored in `$HOME/exp` directory, that is:

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

Also the data files (ridf files) are assumed to be stored `(workdir)/ridf` (internal storage) and `/Data` (external storage) directory.

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

- Clone from GitHub repository

```shell
> cd ~/exp
> git clone https://github.com/CRIB-project/crib_daq_mgmt.git expname
```

- **NOT RECOMMENDED** Copy from previous experiment (please exclude `ridf` files)

```shell
> cd ~/exp
> cp -r expname_pre expname_new
```

# Initial setup

Initial setup

```shell
> cd bin
> ./setup_environment
```

Based on the inputted `expname`, initial setup will performed automatically.

# For Usability

In the `.bashrc/.zshrc`, set the `EXP_NAME` environment variable to automatically move to this working directory.

```shell
export EXP_NAME="hoge"
```

The alias `alias dcd='cd $HOME/exp/$EXP_NAME'` will work.

## Useful Scripts

```shell
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
