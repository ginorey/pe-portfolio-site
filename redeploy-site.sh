#!/bin/bash

tmux kill-server
echo "There are currently no servers running! Congratz :)"
cd ~/pe-portfolio-site
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install --upgrade pip
pip3 install -r requirements.txt
tmux new-session -d -s pe-portoflio-site 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
