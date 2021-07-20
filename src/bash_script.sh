#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python3, but it looks like Python is not installed on your system.
    To install Python3, check out https://installpython3.com/' >&2
  exit 1
fi


sudo python3 snake.py $1
