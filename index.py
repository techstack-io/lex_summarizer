#===========================================================================
#                       STACKMETRIC IO
#===========================================================================

message = """
        # __By Stackmetric IO__
        """

import streamlit as st
# st.set_page_config(layout = "wide") # optional

# with st.sidebar:
#     st.image("https://lh3.googleusercontent.com/nDOoz4Jb1mkEZWxLOgCoZ2LXmeaL1rmBfJRAKftffgwUSNKaqe-a9_3WzMLaPkB2Qt-k71zaqG14icbC5Pg0DcZ2voKZsWd5uKiwaspyjhqqIv0b_38amdEVJMUTASC7oBZ8JnAnjw=w250")

import pkgutil
import importlib
import stlib    # default library name for apps

col1, col2, col3 = st.columns([12.5,75,12.5])

with col2:
    st.image("https://lh3.googleusercontent.com/5XLeASxlnhN_3iYtrVf2Z8Dhw7QyoRKqJbVI832d8ZWM26PYM3WUb6GR_9tqw3yV_9b2YsN2vgtRqef3vEA5Aem7Gfmi-DDPkKyif-E_2fF2HjXUX3rrorB3kEcFT6C5NhBsbls=w2000")

# Global arrays for holding the app names, modules and descriptions of the apps
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

# Display the sidebar with a menu of apps
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',names, format_func=format_func) 
    
st.sidebar.header('Built on and with:')
    # Badges
with st.sidebar:
    st.image("https://img.shields.io/pypi/pyversions/django?style=for-the-badge")
    st.image("https://img.shields.io/conda/vn/conda-forge/python?color=green&style=for-the-badge")
    st.image("https://img.shields.io/badge/DASHBOARDING WITH-Streamlit-green?style=for-the-badge")
with st.sidebar.expander("NLTK"):
    st.write("""Natural Language Toolkit is an open source Python library for Natural Language Processing.""")
with st.sidebar.expander("Sumy"):
    st.write("""Sumy - Simple library and command line utility for extracting summary from HTML pages or plain texts.""")
with st.sidebar.expander("BERT"):
    st.write("""BERT (Bidirectional tranformer) is a transformer used to overcome the limitations of RNN and other neural networks as Long term dependencies. It is a pre-trained model that is naturally bidirectional. This pre-trained model can be tuned to easily to perform the NLP tasks as specified, Summarization in our case..""")

# Run the chosen app
modules[names.index(page)].run()