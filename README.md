# Predicting NBA Player Performance


## Thesis

This project aims to leverage machine learning alrgorithms to predict NBA player performances for the upcoming season. In the case of this project, we will be predicting Win Shares per 48 minutes.

The data can be found on https://www.basketball-reference.com/.


## Initial EDA

First, what are Win Shares? 

Win Shares is an advanced stat used on https://www.basketball-reference.com/ to quantify how much a player contributes to wins.

The formula goes:

### Win Shares(WS) = Offensive Win Shares(OWS) + Defensive Win Shares(DWS)

#### OWS = (Marginal Offense) / (Marginal Points per Win)
#### DWS = (Marginal Defense) / (Marginal Points per Win)

#### Marginal Offense = (points produced) - 0.92 * (league points per possession) * (offensive possessions)

#### Marginal Defense = (player minutes played / team minutes played) * (team defensive possessions) * (1.08 * (league points per possession) - ((Defensive Rating) / 100))

#### Marginal Points per Win = 0.32 * (league points per game) * ((team pace) / (league pace))

Kareem Abdul Jabbar's holds the single season record of **25.4 Win Shares** in the 1971-72 season.

However, as we are predicting Win Shares per 48 minutes (WS/48),
we can see Michael Jordan holds that record at **0.2505**.

Here's a histogram of all WS/48 counts from 2011-2019:

![hist1](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/01_ws48_hist.png)

Too many players with low WS/48. Let's filter some of them out by looking at players who have played at least 200 minutes in a season:

![hist2](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/02_ws48_hist_200.png)

Much better.
