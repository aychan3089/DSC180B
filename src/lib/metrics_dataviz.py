import pandas as pd
import numpy as np
import metrics
import sort_tweets
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def sci_likes_over_months(politicians, inpath, outpath, x_months):
    """
    takes in list of names for politicians and creates line
    graph for their likes over months
    * takes politician with highest tweet ratio average and 
    lowest tweet ratio average from scientific group
    """
    avg_likes_over_months = metrics.avg_likes_over_months(inpath, x_months)
    
    plt.figure(figsize=(12, 5))
    for i in politicians:
        plt.plot(list(avg_likes_over_months[i].keys())[100:], list(avg_likes_over_months[i].values())[100:])
        
        plt.title('Scientific Average likes Over 4 Months')
        plt.xlabel('Months')
        plt.xticks(rotation=90) 
        plt.ylabel('Number of Likes')
        plt.legend(politicians)

    plt.savefig(outpath, bbox_inches='tight')
    plt.show()
    
    
    
def misinfo_likes_over_months(politicians, inpath, outpath, x_months):
    """
    takes in list of names for politicians and creates line
    graph for their likes over months
    * takes politician with highest tweet ratio average and 
    lowest tweet ratio average from misinfo group
    """
    avg_likes_over_months = metrics.avg_likes_over_months(inpath, x_months)
    
    plt.figure(figsize=(12, 5))
    for i in politicians:
        plt.plot(list(avg_likes_over_months[i].keys())[100:], list(avg_likes_over_months[i].values())[100:])
        
        plt.title('Misinfo Average likes Over 4 Months')
        plt.xlabel('Months')
        plt.xticks(rotation=90) 
        plt.ylabel('Number of Likes')
        plt.legend(politicians)
        
    plt.savefig(outpath, bbox_inches='tight')
    plt.show()
    
    
def compare_sci_misinfo(politicians, sci_path, misinfo_path, outpath, x_months):
    """
    Compares 1 politician from each group
    """
    sci = metrics.max_likes_over_months(sci_path, x_months)
    misinfo = metrics.max_likes_over_months(misinfo_path, x_months)
    
    plt.figure(figsize=(12, 5))
    plt.plot(list(sci[politicians[0]].keys())[100:], list(sci[politicians[0]].values())[100:])
    plt.plot(list(misinfo[politicians[1]].keys())[100:], list(misinfo[politicians[1]].values())[100:])

    plt.title('Comparison of Scientific and Misinfo Max Likes Over 4 Months Window')
    plt.xlabel('Months')
    plt.xticks(rotation=90) 
    plt.ylabel('Max Number of Likes')
    plt.legend(politicians)
        
    plt.savefig(outpath, bbox_inches='tight')
    plt.show()
    
    
def max_all_sci(sci_path, outpath, x_months):
    """
    returns max likes for all scientific politicians
    """
    sci = metrics.max_likes_over_months(sci_path, x_months)

    plt.figure(figsize=(20, 10))
    for i in list(sci.keys()):
        plt.plot(list(sci[i].keys())[100:], list(sci[i].values())[100:])
        
        plt.title('Scientific Max Likes Over 4 Months')
        plt.xlabel('Months')
        plt.xticks(rotation=90) 
        plt.ylabel('Number of Likes')
        plt.legend(list(sci.keys()), bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        
    plt.savefig(outpath, bbox_inches='tight')
    plt.show()

    
def max_all_misinfo(misinfo_path, outpath, x_months):
    """
    returns max likes for all misinfo politicians
    """
    misinfo = metrics.max_likes_over_months(misinfo_path, x_months)

    plt.figure(figsize=(20, 10))
    for i in list(misinfo.keys()):
        plt.plot(list(misinfo[i].keys())[100:], list(misinfo[i].values())[100:])
        
        plt.title('Misinformation Max Likes Over 4 Months')
        plt.xlabel('Months')
        plt.xticks(rotation=90) 
        plt.ylabel('Number of Likes')
        plt.legend(list(misinfo.keys()), bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        
    plt.savefig(outpath, bbox_inches='tight')
    plt.show()

