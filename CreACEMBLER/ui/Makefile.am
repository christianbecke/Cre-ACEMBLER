uidir = $(pkgpythondir)/ui
ui_PYTHON = \
		__init__.py \
		ui.py

CLEANFILES = ui.py
EXTRA_DIST = ui.py.in
BUILT_SOURCES = ui.py

include $(top_srcdir)/edit.mak

ui.py: Makefile
	$(edit) < '$(srcdir)/$@.in' > $@

ui.py: ui.py.in

