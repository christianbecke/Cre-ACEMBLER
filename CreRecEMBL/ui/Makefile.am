uidir = $(pkgpythondir)/ui
ui_PYTHON = \
			__init__.py \
			ui.py

CLEANFILES = ui.py
EXTRA_DIST = ui.py.in
BUILT_SOURCES = ui.py

edit = sed \
		-e 's,@pkgdatadir[@],$(pkgdatadir),g' \
		-e 's,@ENABLE_UNINSTALLED[@],$(ENABLE_UNINSTALLED),g' \
		-e 's,@PACKAGE_NAME[@],$(PACKAGE_NAME),g' \
		-e 's,@PACKAGE_VERSION[@],$(PACKAGE_VERSION),g' \
		-e 's,@PACKAGE_URL[@],$(PACKAGE_URL),g'

ui.py: Makefile
	$(edit) < '$(srcdir)/$@.in' > $@

ui.py: ui.py.in

