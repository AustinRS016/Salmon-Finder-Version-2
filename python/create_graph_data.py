import pandas as pd
import json
from datetime import date, timedelta
import numpy as np
from numpy import asarray
from numpy import exp
from sklearn.neighbors import KernelDensity


from hatchery_provider_meta import HatcheryProviderResponse


def get_recent_escapement(hatchery_provider_response: HatcheryProviderResponse):
    """
        Parameters:
        hatchery_provider_response
    Output:
        bargraph_data: JSON string as:
            List of dictionaries
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer', 
                year_counts: [{'day': int, 'count': int}]}]
    """
    distinct_populations = hatchery_provider_response.distinct_populations
    df = hatchery_provider_response.df

    two_weeks_prior = pd.to_datetime(date.today() + timedelta(days=-14))

    filtered_df = df[df["date"] > two_weeks_prior]

    if len(filtered_df) == 0:
        return json.dumps([])

    graph_data = []
    for pops in distinct_populations:
        subset_df = filtered_df[
            (filtered_df.species == pops["species"])
            & (filtered_df.run == pops["run"])
            & (filtered_df.origin == pops["origin"])
        ]
        if len(subset_df) == 0:
            continue
        grouped = subset_df.groupby("date").sum()
        grouped.index = grouped.index.strftime("%Y-%m-%d")
        grouped_dict = grouped.to_dict()
        day_counts = []
        for i in range(14):
            day = pd.to_datetime(two_weeks_prior + timedelta(days=i))
            day = day.strftime("%Y-%m-%d")
            day_dict = {}
            if day in grouped_dict["adult_count"]:
                day_dict["day"] = day
                count = int(grouped_dict["adult_count"][day])
                day_dict["count"] = count
            else:
                day_dict["day"] = day
                day_dict["count"] = 0
            day_counts.append(day_dict)
        graph_data.append(
            {
                "species": pops["species"],
                "run": pops["run"],
                "origin": pops["origin"],
                "day_counts": day_counts,
            }
        )
    return json.dumps(graph_data)


def compute_bargraph_data(hatchery_provider_response: HatcheryProviderResponse):
    """
    Parameters:
        hatchery_provider_response
    Output:
        bargraph_data: JSON string as:
            List of dictionaries
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer', 
                year_counts: [{year: int, count: int}]}]
    Info:
        In this study populations are distinguised by what species they are 
            (species), if they are hatchery
        or wild (origin), and what time of the year they return (run)
    """
    distinct_populations = hatchery_provider_response.distinct_populations
    df = hatchery_provider_response.df

    graph_data = []
    for pops in distinct_populations:
        subset_df = df[
            (df.species == pops["species"])
            & (df.run == pops["run"])
            & (df.origin == pops["origin"])
        ]
        years = subset_df.Year.unique()
        year_counts = []
        for y in years:
            year_sum = subset_df.loc[subset_df["Year"] == y, "adult_count"].sum()
            # year_counts.append({y: int(year_sum)})
            year_counts.append({"year": int(y), "count": int(year_sum)})

        graph_data.append(
            {
                "species": pops["species"],
                "run": pops["run"],
                "origin": pops["origin"],
                "year_counts": year_counts,
            }
        )
    return json.dumps(graph_data)


def compute_KDE(hatchery_provider_response: HatcheryProviderResponse):
    """
    Parameters:
        hatchery_provider_response
    Output:
        final_dict: JSON string as:
            Output: list[dict['year': int, 'count': float]]
    """
    distinct_populations = hatchery_provider_response.distinct_populations
    df = hatchery_provider_response.df
    graph_data = []
    for pops in distinct_populations:
        # Drop duplicate values, format by distinct populations
        subset_df = format_data(pops, df)
        # Format data as 1D array
        total = []
        for index, row in subset_df.iterrows():
            arr = np.repeat(np.float32(row.DOY), row.adult_count)
            total = np.append(arr, total)
        # Fit model to 2 years of data
        half_length = int(len(total) / 2)
        below = total[-half_length:] - 366
        above = total[:half_length] + 366
        sample = np.concatenate([below, total, above])
        model = KernelDensity(bandwidth=8, kernel="epanechnikov")
        sample = sample.reshape((len(sample), 1))
        model.fit(sample)
        # Get probabilities for one year
        values = asarray([value for value in range(0, 366)])
        values = values.reshape((len(values), 1))
        probabilities = model.score_samples(values)
        probabilities = exp(probabilities)
        probabilities = probabilities * 2
        probabilities = probabilities.round(4)
        values = np.ravel(values)
        stack = np.vstack((values, probabilities)).T
        final_df = pd.DataFrame(stack[:, 1].T)
        # Format data for front end
        density_data = make_json_table_format(final_df.to_dict()[0])
        graph_data.append(
            {
                "species": pops["species"],
                "run": pops["run"],
                "origin": pops["origin"],
                "density_data": density_data,
            }
        )
    return json.dumps(graph_data)

def format_data(population, df):
    """
    Parameters:
        population: dict {str: str}
            Disticnt population
            example: {'species': 'Chinook', 'origin': 'WILD', run: 'Summer'}
        df: pandas dataframe with columns:
            ['species', 'origin', 'run', 'facility', 'adult_count', 'date', 'DOY', 'Year']
    Output:
        pandas dataframe filtered by population dictionary
    Description:
        Takes a dataframe and a distinct population and return a filtered dataframe
            with columns that match the keys from the dictionary
    """
    subset_df = df[
        (df.species == population["species"])
        & (df.run == population["run"])
        & (df.origin == population["origin"])
    ]
    # For now any duplicates are simply removed
    duplicates_df = subset_df.index[subset_df.duplicated("date")].tolist()
    for dup in duplicates_df:
        subset_df = subset_df.drop(dup)
    return subset_df

def make_json_table_format(dict):
    """
    Parameters: dict {string: number}
    Output: list[dict[year: int, count: float]]
    Description:
    Changes data from {DayOfYear: FishCount} to {day: DayOfYear, and count: FishCount}
    Data format is more easily consumed by D3.js
    """
    dictArr = []
    for key in dict:
        new_value = {"day": key, "count": dict[key]}
        dictArr.append(new_value)
    return dictArr
