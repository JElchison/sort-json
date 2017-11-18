# sort-json
Python script that sorts a JSON object according to its keys.

The product of this script is deterministic, so this is useful for diff'ing two JSON files.

## Example Usage

Sort a JSON file:
```
user@computer:~$ cat abc.json 
{
    "c": 0,
    "b": 0,
    "a": {
      "a3": 1,
      "a2": 2,
      "a1": 3
    }
}
user@computer:~$ ./sort-json.py abc.json 
{
    "a": {
        "a1": 3,
        "a2": 2,
        "a3": 1
    },
    "b": 0,
    "c": 0
}
```

Diff two JSON files:
```
user@computer:~$ cat abcd.json 
{
    "d": 0,
    "c": 0,
    "b": 0,
    "a": {
      "a3": 1,
      "a2": 2,
      "a1": 3
    }
}
user@computer:~$ diff <(./sort-json.py abc.json) <(./sort-json.py abcd.json)
8c8,9
<     "c": 0
---
>     "c": 0,
>     "d": 0
```

## References

* https://docs.python.org/2/library/json.html#json.dump
