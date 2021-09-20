# log-file-monitor

A cli tool used to monitor file status. The logic is very simple, as it is only a tool for personal use.

Currently supported status types:
* file length
* line count

## Usage

```
$ python3 cli.py monitor --help
Usage: cli.py monitor [OPTIONS] FILE

  monitor file status

Options:
  --interval INTEGER     interval of refreshing (milliseconds)
  --show_length BOOLEAN  whether show file length
  --show_line BOOLEAN    whether show file line count
  --help                 Show this message and exit.
```