#!/bin/bash

cd $(dirname $0)

day=$(date +"%-d")
year=$(date +"%Y")
day_dir="day$(printf '%02d' $day)"

if [[ -d ${day_dir} ]]
then
    exit 1
fi

url="https://adventofcode.com/${year}/day/${day}"

firefox --new-window ${url}
wget -q --load-cookies=cookies.txt -P ${day_dir} "${url}/input"
touch "${day_dir}/${day_dir}.py"

