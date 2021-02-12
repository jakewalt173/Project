#Grabbing and Sorting Metadata of Spotify's top 40 songs
#By Liam Egan, Jacob Walter, and Ziyang Lan

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_songs_daily(filename1):
    index_list=[]
    df1 = pd.read_csv(filename1)
    df1.rename(columns={'Position':'Song Rank','Track Name':'Song Name'},inplace=True)
    df1 = df1.drop(columns=['URL','Streams'])    
    for i in range(40,200):
        index_list.append(i)
    df_daily = df1.drop(df1.index[index_list])
    df_daily.to_csv('modified_daily.csv')
    return df_daily

def read_songs_weekly(filename2):
    index_list=[]
    df2 = pd.read_csv(filename2)
    df2.rename(columns={'Position':'Song Rank','Track Name':'Song Name'},inplace=True)
    df2 = df2.drop(columns=['URL','Streams'])   
    for i in range(40,200):
        index_list.append(i)
    df_weekly=df2.drop(df2.index[index_list])
    df_weekly.to_csv('modified_weekly.csv')
    df_weekly = df_weekly.loc[:, ~df_weekly.columns.str.contains('^Unnamed')]
    return df_weekly

def song_sorts(df_daily):
    df3 = pd.read_csv(df_daily)
    df3 = df3.drop(columns=['Unnamed: 0'])
    my_dict = df3.set_index('Song Name').T.to_dict('list')
    return my_dict

def song_rank(df_daily, df_weekly):
    df_by_song = pd.merge(df_daily, df_weekly, on="Song Name", how="outer")
    df_by_song = df_by_song.loc[:, ~df_by_song.columns.str.contains('^Unnamed')]
    del df_by_song['Artist_y']
    df_by_song = df_by_song.rename(columns = {'Song Rank_x':'Daily Rank','Artist_x':'Artist','Song Rank_y':'Weekly Rank'})
    df_by_song.at[1,'Weekly Rank']= 2.0
    df_by_song.at[4,'Weekly Rank']= 5.0
    df_by_song.at[27,'Weekly Rank']= 28.0
    df_by_song.at[31,'Weekly Rank']= 32.0
    df_by_song.at[33,'Weekly Rank']= 34.0
    df_by_song.at[37,'Weekly Rank']= 38.0
    df_by_song.at[40,'Artist']= '21 Savage'
    df_by_song.at[40,'Daily Rank']= 40
    df_by_song = df_by_song.drop([41,42,43,44,45])
    df_by_song['Weekly vs Daily Rank Change'] = df_by_song['Weekly Rank'] - df_by_song['Daily Rank']
    return df_by_song

def data_visual(df_by_song):
    x = df_by_song['Weekly Rank']
    y = df_by_song['Daily Rank']
    n = df_by_song['Song Name']
    fig, ax=plt.subplots()
    ax.scatter(x, y)
    for i, txt in enumerate(n):
        ax.annotate(txt,(x[i],y[i]))
    plt.title('Song Ranks')
    plt.xlabel('Weekly Rank')
    plt.ylabel('Daily Rank')
    
def top_artist(my_dict):
    vals = {}                      
    for i in my_dict.values():
        for j in set(i):              
            vals[j] = 1 + vals.get(j,0)
            if j in range(0,201):
                del vals[j]
    val = list(vals.values())
    ky = list(vals.keys())
    return ky[val.index(max(val))]

def main(file_daily, file_weekly):
    df_day = read_songs_daily(file_daily)
    print(df_day)
    df_week = read_songs_weekly(file_weekly)
    print(df_week)
    df_rank = song_rank(df_day, df_week)
    print(df_rank)
    print(data_visual(df_rank))
    dct_day = song_sorts('modified_daily.csv')
    tp_art = top_artist(dct_day)
    print("The top artist for the day is {}.".format(tp_art))
    
if __name__ == '__main__':
    main('us-daily.csv','weekly-list.csv')