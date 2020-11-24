import pandas as pd

def preprocess(df):
    """Function that preprocesses a dataframe before feeding it to text classification libraries"""
    
    # Filter English songs
    df = df.loc[df['language'] == 'en']
    
    # Filter relevant columns
    df = df[['track_id', 'lyrics', 'playlist_genre']]
    
    # Change column names for model
    df = df.rename(columns={'lyrics': 'text', 'playlist_genre': 'label'})
    
    return(df)