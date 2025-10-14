#!/bin/bash

echo "DOWNLOADING DATA SOURCES...saving files to './storage'"
mkdir -p storage

echo " > images and probe"
wget --no-check-certificate \
  "https://www.dropbox.com/scl/fi/2xt7815a9un3daau68ns4/multi_image_identities.tar?rlkey=68oj82dqyhj0aa7unbuyo3uc9&st=vtl5s0da&dl=1" \
  -O storage/multi_image_identities.tar

echo " > Extracting..."
tar -xvf storage/multi_image_identities.tar -C storage/


rm storage/multi_image_identities.tar

echo "DONE."
