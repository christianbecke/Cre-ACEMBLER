SUBDIRS = CreACEMBLER data

bin_SCRIPTS = $(PACKAGE_TARNAME)$(CREACEMBLER_EXT)

CLEANFILES = $(PACKAGE_TARNAME)$(CREACEMBLER_EXT) setup.py installer.nsi installer.nsi.tmp inst_list.sed createdir_list.sed rmdir_list.sed delete_list.sed
EXTRA_DIST = $(PACKAGE_TARNAME).in setup.py.in installer.nsi.in
BUILT_SOURCES = $(PACKAGE_TARNAME)$(CREACEMBLER_EXT) setup.py

include $(top_srcdir)/edit.mak

inst_list_sed = { test ! -d "dist" \
	|| { cd "dist" \
	&& find * -type f | \
	$(AWK) 'BEGIN { printf "s,@INST_LIST[@]," } \
	{ gsub("/", "\\\\"); printf "File \"/oname=" $$0 "\" \"dist\\\\" $$0 "\"\\n" } \
	END { printf ",g\n" }'; }; }

delete_list_sed = { test ! -d "dist" \
	|| { cd "dist" \
	&& find * -type f | \
	$(AWK) 'BEGIN { printf "s,@DELETE_LIST[@]," } \
	{ gsub("/", "\\\\"); printf "Delete \"\\$$INSTDIR\\\\" $$0 "\"\\n" } \
	END { printf ",g\n" }'; }; }

createdir_list_sed = { test ! -d "dist" \
	|| { cd "dist" \
	&& find * -type d | \
	$(AWK) '{ gsub("/", "\\\\"); a[i++]="CreateDirectory \"\\$$INSTDIR\\\\" $$0 "\"\\n" } \
	END { printf "s,@CREATEDIR_LIST[@],"; for (j=i-1; j>=0;) printf a[j--]; printf ",g\n" }'; }; }

rmdir_list_sed = { test ! -d "dist" \
	|| { cd "dist" \
	&& find * -type d | \
	$(AWK) '{ gsub("/", "\\\\"); a[i++]="RMDir \"\\$$INSTDIR\\\\" $$0 "\"\\n" } \
	END { printf "s,@RMDIR_LIST[@],"; for (j=i-1; j>=0;) printf a[j--]; printf ",g\n" }'; }; }

remove_py2exe_distdir =  { test ! -d "dist" \
    || { find "dist" -type d ! -perm -200 -exec chmod u+w {} ';' \
         && rm -fr "dist"; }; }

remove_py2exe_builddir =  { test ! -d "build" \
    || { find "build" -type d ! -perm -200 -exec chmod u+w {} ';' \
         && rm -fr "build"; }; }


$(PACKAGE_TARNAME)$(CREACEMBLER_EXT): Makefile
	rm -f $@ $@.tmp
	$(edit) < '$(srcdir)/$(PACKAGE_TARNAME).in' > $@.tmp
	chmod 0755 $@.tmp
	mv $@.tmp $@

setup.py: Makefile
	$(edit) < '$(srcdir)/$@.in' > $@

py2exe: $(BUILT_SOURCES)
	$(remove_py2exe_distdir)
	$(remove_py2exe_builddir)
	$(PYTHON) setup.py py2exe

inst_list.sed: py2exe
	$(inst_list_sed) > $@

delete_list.sed: py2exe
	$(delete_list_sed) > $@

createdir_list.sed: py2exe
	$(createdir_list_sed) > $@

rmdir_list.sed: py2exe
	$(rmdir_list_sed) > $@

installer.nsi: inst_list.sed delete_list.sed createdir_list.sed rmdir_list.sed installer.nsi.in
	$(edit) < '$(srcdir)/$@.in' > $@.tmp
	$(SED) -f inst_list.sed -f delete_list.sed -f createdir_list.sed -f rmdir_list.sed < $@.tmp > $@
	rm -f $@.tmp

win-installer: installer.nsi
	makensis installer.nsi

$(PACKAGE_TARNAME)$(CREACEMBLER_EXT): $(PACKAGE_TARNAME).in
setup.py: setup.py.in
