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

So you need to set "EXP_NAME" environment variable and make directory `${HOME}/exp/${EXP_NAME}` by using


```shell
> cd ~/exp
> git clone --recursive https://github.com/okawak/crib_daq_mgmt.git expname
```

# sub repository

[send_runsummary](https://github.com/okawak/send_runsummary/tree/main)

