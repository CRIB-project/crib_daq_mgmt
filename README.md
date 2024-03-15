# Usage

It assume the directory structure like this:

```shell
> cd ~
> tree
.
├── exp
│   ├── expname1
│   │   ├── hoge

-- snip --

│   │   └── hoge
│   ├── expname2

-- snip --
```

```shell
> cd ~/exp
> git clone https://github.com/okawak/crib_daq_mgmt.git expname
```

## Initial setup

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
