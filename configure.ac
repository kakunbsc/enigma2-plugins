AC_INIT(plugins,0.0.1)
AM_INIT_AUTOMAKE(plugins,0.0.1)

TUXBOX_APPS_DIRECTORY

AM_PATH_PYTHON()
AC_PYTHON_DEVEL

AC_PROG_CXX

AC_ARG_WITH(boxtype,
	[  --with-boxtype=NAME box type [[none,dm7025,dm800...]]],
	[BOXTYPE="$withval"],[BOXTYPE="dm800"])

AC_SUBST(BOXTYPE)
AC_DEFINE_UNQUOTED(BOXTYPE,"$BOXTYPE",[box type])

AM_CONDITIONAL([DM8000], [test "$BOXTYPE" = "dm8000"])
AM_CONDITIONAL([DM7025], [test "$BOXTYPE" = "dm7025"])

AC_OUTPUT([
Makefile
DB/Makefile
DB/AutoBackup/Makefile
DB/Panel/Makefile
DB/Panel/data/Makefile
DB/SoftcamSetup/Makefile
DB/NFSServer/Makefile
DB/Bitrate/Makefile
DB/Bitrate/bitratetool/Makefile
DB/NewsReader/Makefile
DB/NewsReader/data/Makefile
DB/RemoteControlChannel/Makefile
DB/ScreenPosition/Makefile
DB/StreamInterface/Makefile
DB/SnmpAgent/Makefile
UPnP/Makefile
UPnP/UShare/Makefile
])
