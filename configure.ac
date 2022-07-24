AC_INIT([Cre-ACEMBLER], [1.0.1], [christian.becke@fu-berlin.de], [cre-acembler], [http://github.com/christianbecke/Cre-ACEMBLER/])
AC_CONFIG_SRCDIR([CreACEMBLER/__init__.py])
AM_INIT_AUTOMAKE
AM_PATH_PYTHON

AC_PROG_AWK
AC_PROG_SED

AC_MSG_CHECKING([for Gtk-3.0 python bindings])
`$PYTHON -c "import gi; gi.require_version('Gtk', '3.0'); from gi.repository import Gtk" >/dev/null 2>&1`
AS_IF([test $? -eq 0],
	AC_MSG_RESULT([found]),
	AC_MSG_ERROR([please install Gtk-3.0 python bindings])
)

AC_MSG_CHECKING([for Biopython])
`$PYTHON -c 'import Bio' >/dev/null 2>&1`
AS_IF([test $? -eq 0],
	AC_MSG_RESULT([found]),
	AC_MSG_ERROR([please install Biopython])
)

AC_ARG_ENABLE([uninstalled],
	AS_HELP_STRING([--enable-uninstalled],
		[Enable running Cre-ACEMBLER from the source directory])
)
AS_IF([test "x$enable_uninstalled" = "xyes"],
	[AC_SUBST(ENABLE_UNINSTALLED, [True])],
	[AC_SUBST(ENABLE_UNINSTALLED, [False])]
)
AS_CASE($PYTHON_PLATFORM, [*win*], [AC_SUBST(CREACEMBLER_EXT, [.py])], [AC_SUBST(CREACEMBLER_EXT, [])]
)

AC_SUBST(pkgpythondir, $pythondir/CreACEMBLER)

AC_CONFIG_FILES([
Makefile
data/Makefile
data/icons/Makefile
data/icons/hicolor/Makefile
data/icons/hicolor/16x16/Makefile
data/icons/hicolor/16x16/apps/Makefile
data/icons/hicolor/16x16/actions/Makefile
data/icons/hicolor/22x22/Makefile
data/icons/hicolor/22x22/apps/Makefile
data/icons/hicolor/22x22/actions/Makefile
data/icons/hicolor/24x24/Makefile
data/icons/hicolor/24x24/apps/Makefile
data/icons/hicolor/24x24/actions/Makefile
data/icons/hicolor/32x32/Makefile
data/icons/hicolor/32x32/apps/Makefile
data/icons/hicolor/32x32/actions/Makefile
data/icons/hicolor/48x48/Makefile
data/icons/hicolor/48x48/apps/Makefile
data/icons/hicolor/64x64/Makefile
data/icons/hicolor/64x64/apps/Makefile
data/icons/hicolor/256x256/Makefile
data/icons/hicolor/256x256/apps/Makefile
data/icons/hicolor/128x128/Makefile
data/icons/hicolor/128x128/apps/Makefile
data/icons/hicolor/scalable/Makefile
data/icons/hicolor/scalable/actions/Makefile
data/win32/Makefile
CreACEMBLER/Makefile
CreACEMBLER/ui/Makefile
])
AC_OUTPUT

