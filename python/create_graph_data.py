import pandas as pd
import json
from graph_utils import format_data, normalize_data, daily_frequency, calculate_rolling_avg


def find_distinct_populations(df):
    """
    Parameters:
        df: pandas dataframe of data returned from getWDFWData
    Output: 
        distinct_populations: List of dictionaries
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer'}]
    """
    # Group by species -> run -> origin
    species = df.species.unique()

    distinctPopulations = []

    for s in species:
        df_s = df[df.species == s]
        run = df_s.run.unique()
        for r in run:
            df_r = df_s[df_s.run == r]
            origin = df_r.origin.unique()
            for o in origin:
                distinctPopulations.append(
                    {'species': s, 'run': r, 'origin': o,})              
    return distinctPopulations


def compute_bargraph_data(df, distinct_populations):
    """
    Parameters:
        df: pandas dataframe of data returned from get_WDFW_Data
        distinct_populations: List of dictionaries
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer'}]
    Output:
        bargraph_data: JSON string as:
            List of dictionaries
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer', year_counts: [{year: Int}]}]
    Info:
        In this study populations are distinguised by what species they are (species), if they are hatchery
        or wild (origin), and what time of the year they return (run)
    """
    graph_data = []
    for pops in distinct_populations:
        subset_df = df[(df.species == pops['species']) & (df.run == pops['run']) & (df.origin == pops['origin'])]
        years = subset_df.Year.unique()
        year_counts = []
        for y in years:
            year_sum = subset_df.loc[subset_df['Year'] == y, 'adult_count'].sum()
            # year_counts.append({y: int(year_sum)})
            year_counts.append({'year': int(y), 'count': int(year_sum)})

        graph_data.append(
            {'species': pops['species'], 'run': pops['run'], 'origin': pops['origin'], 'year_counts': year_counts})
    return json.dumps(graph_data)


def get_rolling_average(df, distinct_populations):
    '''
    Parameters:
        df: pandas dataframe of data returned from getWDFWData
        distinct_populations: List of dictionaries
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer'}]
    Output:
        final_dict: JSON string as: 
            dict {int: float}
            Dictionary with key as DOY and value as smoothed normalized average     
    '''
    graph_data = []
    for pops in distinct_populations:
        # Drop duplicate values, format by distinct populations
        subset_df = format_data(pops, df)
        # Normalize counts per day by year calculate average per day
        normalized_df = normalize_data(subset_df)
        # Create dictionary with key-value for every day of year
        DOY_dict = daily_frequency(normalized_df)
        # Smooth data by calculating rolling average
        rolling_avg = calculate_rolling_avg(pops, DOY_dict)
        graph_data.append(
            {'species': pops['species'], 'run': pops['run'], 'origin': pops['origin'], 'rolling_average': rolling_avg})
    return json.dumps(graph_data)

       
