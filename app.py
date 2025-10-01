import plotly.express as px
import pandas as pd

# Charger les données depuis Google Sheets
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
donnees = pd.read_csv(url)

# Nettoyer les données : supprimer la ligne d'en-tête parasite si elle est présente comme donnée
donnees = donnees[donnees['qte'] != 'qte']

# Convertir les colonnes en numérique (important pour les calculs)
donnees['qte'] = pd.to_numeric(donnees['qte'], errors='coerce')
donnees['prix'] = pd.to_numeric(donnees['prix'], errors='coerce')

# Supprimer les lignes invalides (ex. où 'qte' ou 'prix' ne sont pas des nombres)
donnees = donnees.dropna(subset=['qte', 'prix'])

# 1. Graphique : quantité vendue par région (existant)
fig_region = px.pie(donnees, values='qte', names='region', title='Quantité vendue par région')
fig_region.write_html('ventes-par-region.html')
print('ventes-par-region.html généré avec succès !')

# 2. Graphique : quantité vendue par produit (nouveau)
fig_produit_qte = px.bar(donnees, x='produit', y='qte', title='Quantité vendue par produit')
fig_produit_qte.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

# 3. Graphique : chiffre d'affaires par produit (nouveau)
donnees['ca'] = donnees['qte'] * donnees['prix']
fig_produit_ca = px.pie(donnees, values='ca', names='produit', title='Chiffre d\'affaires par produit')
fig_produit_ca.write_html('ca-par-produit.html')
print('ca-par-produit.html généré avec succès !')