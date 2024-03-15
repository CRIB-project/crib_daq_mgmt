## Usage

Assume that you installed "poetry" and "pyenv".

```console
> git clone https://github.com/okawak/send_runsummary.git
> cd send_runsummary
> poetry install
> poetry run pytest
```

You need to prepare the google spread sheet correctly (like json key).
Then you can pass the pytest.

```console
> poetry run python3 src/send_runsummary.py [run_number]
> poetry run python3 src/send_runsummary.py [run_min] [run_max] # runnumber
> poetry run python3 src/send_runsummary.py # send all
```

