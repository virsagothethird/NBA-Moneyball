# Predicting NBA Player Performance


## Thesis

This project aims to leverage machine learning alrgorithms to predict NBA player performances for the upcoming season. In the case of this project, we will be predicting Win Shares per 48 minutes.

The data can be found on https://www.basketball-reference.com/.


## Initial EDA

First, what are Win Shares? 

Win Shares is an advanced stat used on https://www.basketball-reference.com/ to quantify how much a player contributes to wins.

The formula goes:

#### Win Shares(WS) = Offensive Win Shares(OWS) + Defensive Win Shares(DWS)

#### OWS = (Marginal Offense) / (Marginal Points per Win)
#### DWS = (Marginal Defense) / (Marginal Points per Win)

#### Marginal Offense = (points produced) - 0.92 * (league points per possession) * (offensive possessions)

#### Marginal Defense = (player minutes played / team minutes played) * (team defensive possessions) * (1.08 * (league points per possession) - ((Defensive Rating) / 100))

#### Marginal Points per Win = 0.32 * (league points per game) * ((team pace) / (league pace))