import streamlit as st


title = "RECO_PLANTES - Reconnaissance de plants et de leurs maladies.🍎"
sidebar_name = "Introduction"


def run():

    # TODO: choose between one of these GIFs
    st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif")

    st.title(title)

    st.markdown("---")

    st.markdown(
        """
  

Contexte:

Le projet Reco_Plantes s'inscrit dans le cadre de la formation Datascientest et vise à valider les concepts théoriques d'intelligence artificielle (IA) acquis sur un exemple réel.

L'objectif du projet, au delà de la mise en pratique des concepts vus lors de la formation, c'est également d'écrire un outil informatique en langage python permettant de prendre en entrée un répertoire d'images de plusieurs plantes et produit en sortie pour chaque image :

1️⃣ le type de la plante

2️⃣ la maladie éventuelle dont souffre la plante (si cette dernière est malade)

3️⃣ le type de maladie de la plante.

C'est donc un projet faisant appel à plusieurs techniques d'IA allant des prétraitements du dataset des images jusqu'à leur classification en passant bien sur par des modélisations à base d'algorithme de deep learning.



Ce document commence par décrire les données sur lesquelles les algorithmes implémentés ont été entrainés et testés. 
Il abordera par la suite les différentes étapes de prétraitements utilisés pour transformer les données
 aux formats attendus par les algorithmes étudiés pour la réalisation du projet. 
Il présentera également les deux approches d'apprentissage implémentés comme solutions à la problématique posée
et justifera le choix de la solution retenue par l'équipe projet.

Données
Etapes de la réalisation

Prétraitements

Traitement

Machine learning

Deep learning

Modélisation retenue

Test et validation

Conclusion
"""
)
    ''' 
        """
        """
        Here is a bootsrap template for your DataScientest project, built with [Streamlit](https://streamlit.io).

        You can browse streamlit documentation and demos to get some inspiration:
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into streamlit [documentation](https://docs.streamlit.io)
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset] (https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset]
          (https://github.com/streamlit/demo-uber-nyc-pickups)
        """
    )
    '''
