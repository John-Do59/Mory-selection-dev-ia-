-- 3.a. Chiffre d'affaires total
SELECT SUM(CAST(c4 AS INTEGER) * CAST(c3 AS REAL)) AS chiffre_affaires_total
FROM ventes
WHERE c1 != 'date';

-- 3.b. Ventes par produit (chiffre d'affaires)
SELECT 
    c2 AS produit,
    SUM(CAST(c4 AS INTEGER) * CAST(c3 AS REAL)) AS chiffre_affaires
FROM ventes
WHERE c1 != 'date'
GROUP BY c2
ORDER BY chiffre_affaires DESC;

-- 3.c. Ventes par région (chiffre d'affaires)
SELECT 
    c5 AS region,
    SUM(CAST(c4 AS INTEGER) * CAST(c3 AS REAL)) AS chiffre_affaires
FROM ventes
WHERE c1 != 'date'
GROUP BY c5
ORDER BY chiffre_affaires DESC;

-- 6.a. Quantité vendue par produit (graphique en barres)
QBAR-SELECT 
    c2 AS L_produit,
    SUM(CAST(c4 AS INTEGER)) AS Y_quantite
FROM ventes
WHERE c1 != 'date'
GROUP BY c2
ORDER BY Y_quantite DESC;

-- 6.b. Chiffre d'affaires par produit (graphique en camembert)
QPIE-SELECT 
    c2 AS L_produit,
    SUM(CAST(c4 AS INTEGER) * CAST(c3 AS REAL)) AS Y_ca
FROM ventes
WHERE c1 != 'date'
GROUP BY c2
ORDER BY Y_ca DESC;