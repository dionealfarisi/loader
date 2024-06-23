#!/bin/bash

modules=(
    "tqdm"
    "progressbar2"
    "alive-progress"
    "rich"
    "halo"
    "progress"
    "click"
    "yaspin"
)

check_and_install() {
    for module in "${modules[@]}"; do
        pip show "$module" > /dev/null 2>&1
        if [ $? -ne 0 ]; then
            echo "Menginstal $module..."
            pip install "$module"
        else
            echo "$module sudah terinstal."
        fi
    done
}

check_and_install
cp -r Loader /data/data/com.termux/files/usr/lib/python3.11/site-packages
