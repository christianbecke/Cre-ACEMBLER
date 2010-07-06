SUBDIRS = CreRecEMBL data

bin_SCRIPTS = crerecembl

CLEANFILES = crerecembl setup.py
EXTRA_DIST = crerecembl.in setup.py.in
BUILT_SOURCES = crerecembl setup.py

edit = sed -e 's,@PYTHON[@],$(PYTHON),g' \
		-e 's,@PACKAGE_NAME[@],$(PACKAGE_NAME),g' \
		-e 's,@PACKAGE_VERSION[@],$(PACKAGE_VERSION),g'

crerecembl: Makefile
	rm -f $@ $@.tmp
	$(edit) < '$(srcdir)/$@.in' > $@.tmp
	chmod 0755 $@.tmp
	mv $@.tmp $@

setup.py: Makefile
	$(edit) < '$(srcdir)/$@.in' > $@

crerecembl: crerecembl.in
setup.py: setup.py.in

