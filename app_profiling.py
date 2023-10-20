import pandas as pd

import streamlit as st

from streamlit_pandas_profiling import st_profile_report

def main():

    st.title("Analyse exploratoire automatisé de ton fichier 🗓️")
    st.subheader("Auteur : Anthony RENARD 🦊")


    type=st.sidebar.selectbox("Choisissez votre type de fichier", ("Excel","CSV"))
 
    if type=="Excel":

        st.sidebar.header("Charger un fichier Excel 🗓️")
        uploaded_file = st.sidebar.file_uploader("Sélectionnez un fichier Excel", type=["xls", "xlsx"])

        if uploaded_file is not None:
            
            try:
                df = pd.read_excel(uploaded_file) #A personnaliser si votre fichier excel contient des spécifités
            except Exception as e:
                st.sidebar.error(f"Erreur lors du chargement du fichier Excel ❌ : {str(e)}")
                df = None

            if df is not None:
                
                st.header("Aperçu des données")
                st.write(df.head())

                
                st.header("Voici une analyse du contenu de ton fichier Excel 📊")
                pr = df.profile_report()
                st_profile_report(pr)

    if type=="CSV":

        st.sidebar.header("Charger un fichier CSV🗓️")
        uploaded_file = st.sidebar.file_uploader("Sélectionnez un fichier Excel", type=["csv"])

        if uploaded_file is not None:
            
            try:
                df = pd.read_csv(uploaded_file) #A personnaliser si votre fichier csv contient des spécifités
            except Exception as e:
                st.sidebar.error(f"Erreur lors du chargement du fichier Excel ❌ : {str(e)}")
                df = None

            if df is not None:
                
                st.header("Aperçu des données")
                st.write(df.head())

                
                st.header("Voici une analyse du contenu de ton fichier Excel 📊")
                pr = df.profile_report()
                st_profile_report(pr)
    
if __name__=='__main__':
        main()