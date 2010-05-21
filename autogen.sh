aclocal --force
autoconf --force
automake --foreign --add-missing --copy
./configure $@
