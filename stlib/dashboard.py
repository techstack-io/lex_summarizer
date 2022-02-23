

def run():
 
# Get this figure: fig = py.get_figure("https://plotly.com/~CITAservice/5/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~CITAservice/5/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="CITA-Bar-Graph", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plotly.com/~CITAservice/5/").get_data()[0]["y"]

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

    import streamlit as st
    import chart_studio.plotly as py
    from plotly.graph_objs import bar

    

    st.header("Example app 1")
    st.write("Insert your own Streamlit code here")

# end of app

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()
