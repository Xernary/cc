dd if=$HOME/cyberchallenge/net/mc/$1 of=$HOME/cyberchallenge/net/mc/plz_with_offset ibs=1 skip=$2 && cat plz_with_offset | zlib-flate -uncompress
