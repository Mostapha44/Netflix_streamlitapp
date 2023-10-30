import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le jeu de données Netflix
netflix_data = pd.read_csv("netflix_titles.csv")


# Calculer l'année avec le plus grand nombre de films et d'émissions
films_and_shows_by_year = netflix_data.groupby('release_year')['type'].count()
annee_max_films_shows = films_and_shows_by_year.idxmax()

# Calculer le top 10 des pays avec le plus de sorties
top_countries = netflix_data.groupby('country')['type'].count().nlargest(10)

# Calculer le nombre de catégories de TV Shows et de films
categories_tv = len(netflix_data[netflix_data['type'] == 'TV Show']['listed_in'].unique())
categories_movies = len(netflix_data[netflix_data['type'] == 'Movie']['listed_in'].unique())

# Calculer le top 10 des réalisateurs sur Netflix
top_directors = netflix_data['director'].value_counts().head(10)

# Titre de l'application
st.title('Analyse de Données Netflix')

# Afficher le dataframe (optionnel)
if st.checkbox('Afficher les données Netflix'):
    st.write(netflix_data)

# Visualisation en camembert pour la répartition entre films et émissions
st.subheader('Répartition des Films et Émissions sur Netflix')
fig1, ax1 = plt.subplots()
ax1.pie(netflix_data['type'].value_counts(), labels=['Films', 'Émissions'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'])
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

# Afficher l'année avec le plus grand nombre de films et d'émissions
st.subheader('Année avec le Plus Grand Nombre de Films et d\'Émissions')
st.write("Année :", annee_max_films_shows)

# Créer un graphique à barres pour montrer le nombre de films et d'émissions par année
st.subheader('Nombre de Films et d\'Émissions par Année sur Netflix')
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(films_and_shows_by_year.index, films_and_shows_by_year.values, color='skyblue')
ax.set_xlabel('Année')
ax.set_ylabel('Nombre de Films et d\'Émissions')
ax.set_title('Nombre de Films et d\'Émissions par Année sur Netflix')
st.pyplot(fig)
st.write("Année avec le plus grand nombre de films et d'émissions :", annee_max_films_shows)

# Données
categories = ['TV Shows', 'Films']
nombre_categories = [categories_tv, categories_movies]

# Créer un graphique à barres pour afficher le nombre total de catégories
st.subheader('Nombre Total de Catégories de TV Shows et de Films sur Netflix')
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.bar(categories, nombre_categories, color=['skyblue', 'lightgreen'])
ax2.set_xlabel('Type de Contenu')
ax2.set_ylabel('Nombre de Catégories')
ax2.set_title('Nombre Total de Catégories de TV Shows et de Films sur Netflix')
st.pyplot(fig2)

# Afficher le top 10 des pays avec le plus de sorties
st.subheader('Top 10 des Pays avec le Plus de Sorties sur Netflix')
st.bar_chart(top_countries)

# Afficher le nombre de catégories de TV Shows et de films
st.subheader('Répartition des Catégories de TV Shows et de Films')
st.write("Nombre de catégories de TV :", categories_tv)
st.write("Nombre de catégories de films :", categories_movies)

# Afficher le top 10 des réalisateurs sur Netflix
st.subheader('Top 10 des Réalisateurs sur Netflix')
sns.barplot(x=top_directors.values, y=top_directors.index, palette='viridis')
plt.xlabel('Nombre de Films et d\'Émissions')
plt.ylabel('Réalisateur')
plt.title('Top 10 des Réalisateurs sur Netflix')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

