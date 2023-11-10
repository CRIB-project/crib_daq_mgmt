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
> git clone --recursive https://github.com/okawak/crib_daq_mgmt.git expname
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
username: root or daq

1. init_babirl (root)

`./init_babirl`

2. kill_babirl (root)

`./kill_babirl`

3. mpvrestart (root, daq)

`./mpvrestart`

4. set_EBsize (daq)

`./set_EBsize number`

5. setup_environment (daq)

`./setup_environment`

6. do_sync.sh (root, daq)

`./do_sync.sh`


# sub repository

[send_runsummary](https://github.com/okawak/send_runsummary/tree/main)

