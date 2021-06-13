import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

def drop_missing_values(df, column, target_key):
    """
    
    drop_missing_values: Gets the specified event (target) and converts it into a dataframe.
    
    Parameters:
        df: Transcript dataset
        column: The name of the column where the json objects are located.
        target_key: Name of the key to extract the information
        
    Return:
        df: Normalized dataframe with the specified key, as column, and their respective values.
    """
    df = df[column].apply(pd.Series)
    
    df_final = df[[target_key]]
    df_final = df_final.dropna()
    df_final = df_final.reset_index()
    
    return df_final


def merge_dataset(general_dataset, column, target_key):
    """
    merge_dataset: merge transcript dataset with the values of the specified key (target_key) 
    
    Parameters:
        general_dataset: transcript dataset.
        column: The name of the column where the json objects are located.
        target_key: Name of the key to extract the information
        
    Return:
        df: Normalized dataframe with the specified key, as column, and their respective values.
    
    """
    data_normalize = drop_missing_values(general_dataset, column, target_key)
    general_dataset =  general_dataset.reset_index()
    
    final_data = pd.merge(general_dataset, data_normalize.reset_index(), on='index', how="inner")
    final_data.drop(['level_0', 'value'], axis=1, inplace=True)   
    
    return final_data

def plot_category_variable(data, column):
    """
    plot_category_variable: Display plot of categorical variables 
    
    Paramters
        column: Name of the column of the dataframe to be displayed
        
    Return 
        None                
    """
    
    plt.figure(figsize=(8, 6)) 
    ax = sns.countplot(x=column, data=data)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.suptitle('Frecuency of ' + column)

    plot_percentage(ax, data[column])
    
def plot_percentage(ax, feature):
    """
    plot_percentage: Shows the percentage that the category represents in the overall data set.
    
    Parameteres
        plot: seaborn data type
        feature: Name of the feature of the dataset
        
    Return
        None    
    """
    
    total = len(feature)
    for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/total)
        x = p.get_x() + p.get_width() / 2 - 0.05
        y = p.get_y() + p.get_height()
        ax.annotate(percentage, (x, y), size = 12)
    plt.show()

def preprocessing_data(df):
    """
    preprocessing_data: It receives a dataframe to which two rescalers RobustScaler and MinMaxScaler are applied.
    
    
    Paramters:
        df: Dataframe to transform.
        
    
    Return
        df: Dataframe columns age, time and income transformed.
    """
    
    
    num_features = ['time', 'income']
    cat_features = ['gender', 'channels', 'reward', 'difficulty', 'duration', 'offer_type']
    
    # Apply RobustScaler
    df[num_features] = preprocessing.RobustScaler().fit_transform(df[num_features])
    
    # Apply MinMaxScaler
    df[num_features] = preprocessing.MinMaxScaler().fit_transform(df[num_features])
    
    # Set preprocessor for categorical variables
    le = preprocessing.LabelEncoder()
    
    # Apply LabelEncoder
    df[cat_features] = df[cat_features].apply(le.fit_transform)

    
    return df    