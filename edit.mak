
edit = $(SED) \
		-e 's,@ENABLE_UNINSTALLED[@],$(ENABLE_UNINSTALLED),g' \
		-e 's,@PACKAGE_BUGREPORT[@],$(PACKAGE_BUGREPORT),g' \
		-e 's,@PACKAGE_NAME[@],$(PACKAGE_NAME),g' \
		-e 's,@PACKAGE_TARNAME[@],$(PACKAGE_TARNAME),g' \
		-e 's,@PACKAGE_URL[@],$(PACKAGE_URL),g' \
		-e 's,@PACKAGE_VERSION[@],$(PACKAGE_VERSION),g' \
		-e 's,@pkgdatadir[@],$(pkgdatadir),g' \
		-e 's,@PYTHON[@],$(PYTHON),g'
