#!/bin/bash

echo "------------------"
echo "Extracting strings"
echo -e "------------------\n"

pybabel extract -F babel.cfg -o strings.pot .
#pybabel init -i strings.pot -d translations -l ru -D strings

echo -e "\nDone"