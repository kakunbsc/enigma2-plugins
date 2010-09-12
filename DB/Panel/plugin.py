from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	from panel import ToplevelPanel
	session.open(ToplevelPanel)

def Plugins(**kwargs):
	return PluginDescriptor(name = "Panel", description = "Lets you execute your Panel", where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc = main)
