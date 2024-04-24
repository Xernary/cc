#!/bin/bash

FOLDER_PATH="$HOME/cyberchallenge/net/mc/packets"

dd if=$FOLDER_PATH/raw/$1 of=$FOLDER_PATH/com/$1.zz ibs=1 skip=$2
cat $FOLDER_PATH/com/$1.zz | zlib-flate -uncompress > $FOLDER_PATH/unc/$1.unc
xxd -p -c 100000000 $FOLDER_PATH/unc/$1.unc
xxd -p -c 100000000 $FOLDER_PATH/unc/$1.unc >> $FOLDER_PATH/convos/client_convo.txt
