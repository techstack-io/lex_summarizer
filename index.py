# ---------------------------------------------------------------------------- #
#          Stackmetric IO - Copyright ©️ 2022 All Rights Reserved.         #
# ---------------------------------------------------------------------------- #

message = """
        # __By Stackmetric IO__
        """

import streamlit as st
# st.set_page_config(layout = "wide") # optional

import pkgutil
import importlib
import stlib

# 🌐 Global arrays for holding the app names, modules and descriptions of the apps
names = []
modules = []
descriptions = [] 

package = stlib # default name for the library containg the apps

# Find the apps and import them
for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    #print ("Found submodule %s (is a package: %s)" % (modname, ispkg))
    if modname.startswith('_'):
        pass  # ignore any modules beginning with _
    else:
        m = importlib.import_module('.'+modname,'stlib')
        names.append(modname)
        modules.append(m)
        # If the module has a description attribute use that in the select box
        # otherwise use the module name
        try:
            descriptions.append(m.description)
        except:
            descriptions.append(modname)

def format_func(name):
    return descriptions[names.index(name)]

# ---------------------------------- Sidebar --------------------------------- #

with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',names, format_func=format_func) 

modules[names.index(page)].run()