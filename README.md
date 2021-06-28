# OlistChallenge

## Overview

This project tackles Olist's challenge posted on Kaggle -> https://www.kaggle.com/olistbr/brazilian-ecommerce.

The challenge consists in increasing Olist's profit while maintaining a healthy monthy order rate.

The `notebooks` folder contains a Jupyter Notebook detailing the decision science process as well as the data visualization for final communication to Olist's CEO.

The Python code used to load, and clean the data provided on Kaggle as well as engineer the different features is provided in the `olist` package.

## Decision Science methodology

Olist considers that bad reviews (below 4/5) generate the more costs. Therefore the approach here is to identify the sellers who are consistently bad reviewed.

Sequential process:

(1) Feature engineering: monthly sales per seller, monthly costs per seller, monthly revenues per seller, seller-customer distance

(2) Identify the low-performing sellers

(3) Simulate monthly profits (revenues - costs) for different scenarios: 

  * Limiting monthly orders for low-performing sellers
  * Banning worst-performing sellers from Olist
  * Penalizing low-performing sellers by increasing their Olist subscription fees
  * Rewarding high-performing sellers by decreasing their Olist subscription fees

(4) Data visualization for the best scenario (ratio between profit increase/loss of sellers)
