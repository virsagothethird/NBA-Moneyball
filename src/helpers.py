import pandas as pd
import numpy as np


def df_year_split(df, year, drop_columns):
    
    return df[df['Year']==year].drop(columns=drop_columns)\
                            .drop_duplicates('Player')\
                            .reset_index().drop(columns='index')


def time_series_me(df1,df2,df3,df_for_y):
    
    time_series_df = df1.copy()
    
    time_series_df = df1.set_index('Player')\
                        .join(df2.set_index('Player'),lsuffix='_1', rsuffix='_2',how='outer')\
                        .join(df3.set_index('Player'),lsuffix='_2', rsuffix='_3',how='outer')\
                        .join(df_for_y.set_index('Player'),lsuffix='_3', rsuffix='_4',how='outer')\
                        .reset_index()
    
    time_series_df = time_series_df[time_series_df['MP_4']>200].dropna(subset=['TRB_3', 'TRB_4'])
    time_series_df = time_series_df.fillna(0)
    #time_series_df = time_series_df[time_series_df['MP_4']>200].dropna

    columns_to_drop = ['Player', 'Pos_1', 'Tm_1', 'Pos_2',
       'Tm_2', 'Pos_3', 'Tm_3',
       'Pos_4', 'Age_4', 'Tm_4', 'G_4', 'MP_4',
       'WS_4', 'WS/48_4', 'FG_4', 'FGA_4', '3P_4', '3PA_4', '2P_4', '2PA_4',
       'FT_4', 'FTA_4', 'TRB_4', 'AST_4', 'STL_4', 'BLK_4', 'TOV_4', 'PF_4',
       'PTS_4']
    X = time_series_df.drop(columns=columns_to_drop)
    y = time_series_df['WS/48_4']
    
    return time_series_df,X,y


def residual_plot(ax, x, y, y_hat, n_bins=50):
    residuals = y_hat - y
    ax.axhline(0, color="black", linestyle="--")
    ax.scatter(x, residuals, color="grey", alpha=0.5)
    ax.set_ylabel("Residuals ($\hat y - y$)")


def plot_many_residuals(df, var_names, y_hat, n_bins=50):
    fig, axs = plt.subplots(len(var_names), figsize=(12, 3*len(var_names)))
    for ax, name in zip(axs, var_names):
        x = df[name]
        residual_plot(ax, x, df['WS/48_4'], y_hat)
        ax.set_xlabel(name)
        ax.set_title("Model Residuals by {}".format(name))
    return fig, axs