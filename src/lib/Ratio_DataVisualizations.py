import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def ratio_means(lst):
    '''
    takes in list of csv files, returns tuple
    * first item in tuple is list of means of ratios for scientific group
    * second item in tuple is list of names of politicians
    '''
    means = []
    names = []
    for file in lst:
        
        df = pd.read_csv(file, index_col=0)
        df = df[df['ratio'] != 0]
        df_ratio_mean = df[df['ratio'] != float('inf')]['ratio'].mean()
        means.append(df_ratio_mean)
        
        names.append(file[:-4])
        
    return means, names


def scientific_ratios_graph(ratios_names):
    '''
    takes in tuple of lists
    * first list contains scientific ratios of politicians
    * second list contains politician names
    '''
    ratios = ratios_names[0]
    names = ratios_names[1]
    
    df = pd.DataFrame.from_dict({'ratios': ratios, 'names': names}).sort_values(['ratios'], axis=0, ascending=True)

    plt.barh(df['names'], df['ratios'])
    
    plt.barh(df['names'], df['ratios'], color="blue")
    plt.title('Scientific Ratios')
    plt.xlabel('Ratio')
    plt.ylabel('Politician')
    plt.savefig('src/out/Scientific_Ratios.png', bbox_inches='tight')
    
    
def misinfo_ratios_graph(ratios_names):
    '''
    takes in tuple of lists
    * first list contains misinfo ratios of politicians
    * second list contains politician names
    '''
    ratios = ratios_names[0]
    names = ratios_names[1]
    
    df = pd.DataFrame.from_dict({'ratios': ratios, 'names': names}).sort_values(['ratios'], axis=0, ascending=True)

    plt.barh(df['names'], df['ratios'], color="orange")
    plt.title('Misinformation Ratios')
    plt.xlabel('Ratio')
    plt.ylabel('Politician')
    plt.savefig('src/out/Misinfo_Ratios.png', bbox_inches='tight')

