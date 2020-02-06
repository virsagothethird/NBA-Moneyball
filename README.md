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
Now let's look at how the NBA changed since 2011:

![scatter1](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/04_year_ws48.png)
![scatter2](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/05_pos_ws48.png)
![scatter3](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/06_3p_ws48.png)
![scatter4](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/07_3pa_ws48.png)
![scatter5](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/08_ft_ws48.png)
![scatter6](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/09_fta_ws48.png)
![scatter7](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/10_blk_ws48.png)

3-points made and attempted (3P, 3PA) have certainly increased which coincides with the current NBA play style. However, we also see that the top blockers(BLK) seem to contribute more to wins now than they used to. As important as 3-point shooters are in today's NBA, it seems that good defensive play is all the more important because of it.


## The model

For this project, I decided to go with the RandomForestRegressor from the scikit-learn library for it's ease of use.

I decided to go with the following features:

**Age, Games played(G), Minutes played(MP), Win Shares(WS), WS/48, Field Goals(FG), Field Goal Attempts(FGA), 3-pointers(3P), 3-pointer attempts(3PA), 2-pointers(2P), 2-pointer attempts(2PA), Free Throws(FT), Free Throw Attempts(FTA), Total Rebounds(TRB), Assists(AST), Steals(STL), Blocks(BLK), Turnovers(TOV), Personal Fouls(PF), Total Points Scored(PTS).**

In order to predict future performance, the data was arranged in a time series format, using the past 3 seasons of stats to predict the following season.

Our data was formatted as so:
X = 
<table>
    <tr>
        <td>2011_stats,  2012_stats,  2013_stats</td>
        <td>2012_stats,  2013_stats,  2014_stats</td>
        <td>2013_stats,  2014_stats,  2015_stats</td>
        <td>2014_stats,  2015_stats,  2016_stats</td>
        <td>2015_stats,  2016_stats,  2017_stats</td>
        <td>2016_stats,  2017_stats,  2018_stats</td>
    </tr>
</table>

#### X  =   2011_stats  2012_stats  2013_stats     y   =    2014_WS/48
####        2012_stats  2013_stats  2014_stats              2015_WS/48
####        2013_stats  2014_stats  2015_stats              2016_WS/48
####        2014_stats  2015_stats  2016_stats              2017_WS/48
####        2015_stats  2016_stats  2017_stats              2018_WS/48
####        2016_stats  2017_stats  2018_stats              2019_WS/48

The base RandomForestRegressor model return an OOB score of **0.4483**, an R2 score of **0.5217**, and a mean squared error of **0.00156**.

Using scikit-learn's GridSearchCV to run through 6000 RandomForestRegressor fits, the model it returned gave me an OOB score of **0.472**, and R2 score of **0.515**, and a mean squared error of **0.00159**. Slightly better than the base model.

Doing a KFolds cross validation, it returned mean R2 scores of **0.451** for the base model and **0.474** for the "best" model. I ended up using the "best" model for my predictions.

Here are the plots of feature importance and permutation importance of my model:

![bar1](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/11_rf_best_feature_importance.png)

![bar2](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/12_rf_best_permutation_importance.png)

We can see that my model lists previous season WS and WS/48 scores as most important as expected, but then we see TRB and BLK as the next most important features followed by 3P and 3PA. Perhaps defense trumps offense?


## Predictions for 2020

![table1](https://github.com/virsagothethird/NBA-Moneyball/blob/master/img/13_predicted_vs_actual.png)

The left table hows my model's top 20 predictions for the 2020 season. The right is the actual 2020 top 20 list(this table was taken on Feb 6, 2011, and is subject to change as the season has not yet concluded).

Many familiar names show up on both tables.


## Conclusions

Given the low R2 and OOB scores, I believe that this model should only be used as a starting point when trying to determine a player's future performance. Inconsistencies in performance from season to season could have contributed to the low scores. There could be many reasons for these inconsistencies such as injuries, team changes, etc.



## Technologies Used
* Scikit-learn
* Pandas
* Matplotlib