import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
# Add 'overweight' column
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = [ '1' if i >= 25 else "0" for i in df['overweight']] 
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = [ '0' if i == 1 else "1" for i in df['gluc']]
df['cholesterol'] = [ '0' if i == 1 else "1" for i in df['cholesterol']]
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars =['cardio'], value_vars =['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    groups = df_cat.groupby(df_cat.cardio)
    df0 = groups.get_group(0)
    df1 = groups.get_group(1)
    print(df0.value_counts(), df1.value_counts())
    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x = 'variable', hue = 'value', col = 'cardio', kind = 'count', data = df_cat, ci="sd", palette = "dark", alpha = .6, height = 6)
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]
    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(df_heat.corr()))



    # Set up the matplotlib figure
    plt.figure(figsize=(8, 6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(df_heat.corr(), annot=True, mask = mask) 
    plt.show()
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig