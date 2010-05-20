AC_INIT([CreRecEMBL], [0.1])
AC_CONFIG_SRCDIR([CreRecEMBL/__init__.py])
AM_INIT_AUTOMAKE
AM_PATH_PYTHON

AC_ARG_ENABLE([uninstalled],
	AS_HELP_STRING([--enable-uninstalled],
		[Enable running CreRecEMBL from the source directory])
)
AS_IF([test "x$enable_uninstalled" = "xyes"],
	[AC_SUBST(ENABLE_UNINSTALLED, [True])],
	[AC_SUBST(ENABLE_UNINSTALLED, [False])]
)

AC_OUTPUT([
Makefile
data/Makefile
data/icons/Makefile
data/icons/hicolor/Makefile
data/icons/hicolor/48x48/Makefile
data/icons/hicolor/48x48/apps/Makefile
CreRecEMBL/Makefile
CreRecEMBL/ui/Makefile
])

