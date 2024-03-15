# send_runsummary

python script to send ridf information to the google spread sheet

## usage

```sh
poetry install
poetry update
```

test code

```sh
poetry run pytest
```

You need to prepare the google spread sheet correctly (like json key).
Then you can pass the pytest.

```sh
poetry run python src/send_runsummary.py [run_number]
poetry run python src/send_runsummary.py [run_min] [run_max] # runnumber
poetry run python src/send_runsummary.py # send all
```
