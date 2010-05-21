SUBDIRS = CreRecEMBL data

bin_SCRIPTS = crerecembl

CLEANFILES = crerecembl
EXTRA_DIST = crerecembl.in
BUILT_SOURCES = crerecembl

edit = sed -e 's,@PYTHON[@],$(PYTHON),g'

crerecembl: Makefile
	rm -f $@ $@.tmp
	$(edit) < '$(srcdir)/$@.in' > $@.tmp
	chmod 0755 $@.tmp
	mv $@.tmp $@

crerecembl: crerecembl.in

