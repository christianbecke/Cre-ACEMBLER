uidir = $(pkgpythondir)/ui
ui_PYTHON = \
			__init__.py \
			ui.py

CLEANFILES = ui.py
EXTRA_DIST = ui.py.in
BUILT_SOURCES = ui.py

edit = sed \
		-e 's,@pkgdatadir[@],$(pkgdatadir),g' \
		-e 's,@ENABLE_UNINSTALLED[@],$(ENABLE_UNINSTALLED),g'

ui.py: Makefile
	$(edit) < '$(srcdir)/$@.in' > $@

ui.py: ui.py.in

