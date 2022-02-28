
def run():
 
    import streamlit as st
    from streamlit_lottie import st_lottie
    from streamlit_lottie import st_lottie_spinner

    def load_lottieurl(url: str):
     r = requests.get(url)
     if r.status_code != 200:
         return None
     return r.json()

# lottie_url = "https://assets10.lottiefiles.com/packages/lf20_jYTS0r.json"
# lottie_json = load_lottieurl(lottie_url)
st.lottie("https://assets10.lottiefiles.com/packages/lf20_jYTS0r.json")

# end of app

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()

