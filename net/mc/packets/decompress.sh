dd if=$HOME/cyberchallenge/net/mc/packets/$1 of=$HOME/cyberchallenge/net/mc/packets/$1.zz ibs=1 skip=$2 && cat $1.zz | zlib-flate -uncompress > $1.unc
