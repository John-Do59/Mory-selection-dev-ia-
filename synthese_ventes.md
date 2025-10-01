# Fiche synthèse – Analyse des ventes (20 jours)

## 3.a. Chiffre d’affaires total
Le chiffre d’affaires total sur la période de 20 jours s’élève à **108 750 €**.

## 3.b. Ventes par produit (chiffre d’affaires)
| Produit    | Quantité vendue | Chiffre d’affaires |
|------------|------------------|---------------------|
| Produit A  | 2 550            | **25 500 €**        |
| Produit B  | 1 725            | **25 875 €**        |
| Produit C  | 1 005            | **20 100 €**        |

>  **Insight** : Le **Produit B** génère le CA le plus élevé malgré une quantité inférieure au Produit A, grâce à un prix unitaire plus élevé (15 € vs 10 €).

## 3.c. Ventes par région (chiffre d’affaires)
| Région | Chiffre d’affaires |
|--------|---------------------|
| Sud    | **54 375 €**        |
| Nord   | **54 375 €**        |

>  **Insight** : Les ventes sont **parfaitement équilibrées** entre les deux régions (50 % / 50 %), ce qui indique une répartition homogène de la demande ou une stratégie commerciale équilibrée.

---

> **Source des données** : Extrait de 20 jours de ventes fourni par le client.  
> **Méthodologie** : Analyse réalisée via requêtes SQL sur base SQLite, avec conversion des colonnes textuelles en valeurs numériques (`CAST`).