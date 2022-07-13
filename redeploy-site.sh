#!/bin/bash

cd ~/pe-portfolio-site
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install --upgrade pip
pip3 install -r requirements.txt
systemctl daemon-reload
systemctl restart myportfolio
