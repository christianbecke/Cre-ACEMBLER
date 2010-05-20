from distutils.core import setup
import py2exe

setup (
	name="CreRecEMBL",
	version="0.1",
	windows=[
		{
			"script": "crerecembl",
		}
	],

	options={
		"py2exe": {
			"includes": "cairo, pango, pangocairo, atk, gobject",
		}
	},

	data_files=[
		"data/crerecembl.glade",
		"data/cre_assistant.glade"
	]
)
