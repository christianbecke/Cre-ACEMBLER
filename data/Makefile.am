SUBDIRS = icons win32

Multimediadir = $(datadir)/applications
Multimedia_DATA = $(PACKAGE_TARNAME).desktop

uidir = $(pkgdatadir)
ui_DATA = cre_assistant.ui $(PACKAGE_TARNAME).ui

EXTRA_DIST = $(Multimedia_DATA) $(ui_DATA) $(PACKAGE_TARNAME).desktop.in 

CLEANFILES = $(PACKAGE_TARNAME).desktop

include $(top_srcdir)/edit.mak

$(PACKAGE_TARNAME).desktop: Makefile
	$(edit) < '$(srcdir)/$@.in' > $@

$(PACKAGE_TARNAME).desktop: $(PACKAGE_TARNAME).desktop.in
