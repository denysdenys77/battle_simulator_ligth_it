#!/bin/bash

entrypoint(){
  pip install -r requirements.txt
  python main.py
  while :
  do
    sleep 1
  done
}
entrypoint
