#!/bin/bash

# SOME LINES ARE COMMENTED OUT DUE TO WORK ON WSL INSTEAD OF NATIVE LINUX

# cd $(dirname $0)


hour=$(date +"%-H")
day=$(date +"%-d")
year=$(date +"%Y")
day_dir="day$(printf '%02d' $day)"

if [[ -d "${year}/${day_dir}" ]] || [ $hour -lt 6 ]
then
    echo "New puzzle is not available yet!"
    exit 1
fi

url="https://adventofcode.com/${year}/day/${day}"

# firefox --new-window ${url} & 
wslview ${url} 
wget -q --load-cookies=cookies.txt -P "${year}/${day_dir}" "${url}/input"
cp base.py "${year}/${day_dir}/${day_dir}.py"
# code
