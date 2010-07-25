AC_INIT([CreRecEMBL], [0.1], [christianbecke@gmail.com], [CreRecEMBL], [http://github.com/christianbecke/CreRecEMBL/])
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
data/icons/hicolor/16x16/Makefile
data/icons/hicolor/16x16/actions/Makefile
data/icons/hicolor/16x16/apps/Makefile
data/icons/hicolor/22x22/Makefile
data/icons/hicolor/22x22/actions/Makefile
data/icons/hicolor/22x22/apps/Makefile
data/icons/hicolor/24x24/Makefile
data/icons/hicolor/24x24/actions/Makefile
data/icons/hicolor/24x24/apps/Makefile
data/icons/hicolor/32x32/Makefile
data/icons/hicolor/32x32/actions/Makefile
data/icons/hicolor/32x32/apps/Makefile
data/icons/hicolor/48x48/Makefile
data/icons/hicolor/48x48/apps/Makefile
data/icons/hicolor/256x256/Makefile
data/icons/hicolor/256x256/apps/Makefile
data/icons/hicolor/scalable/Makefile
data/icons/hicolor/scalable/actions/Makefile
data/icons/hicolor/scalable/apps/Makefile
CreRecEMBL/Makefile
CreRecEMBL/ui/Makefile
])

