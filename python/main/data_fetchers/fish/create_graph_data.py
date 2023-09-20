import pandas as pd
import json
from datetime import date, timedelta

from ...config.hatchery_provider_meta import HatcheryProviderResponse


def get_recent_escapement(hatchery_provider_response: HatcheryProviderResponse):
    """
        Parameters:
        hatchery_provider_response
    Output:
        bargraph_data: JSON string as:
            List of dictionaries
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer', year_counts: [{'day': int, 'count': int}]}]
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
            example: [{'species': 'Chinook', 'origin': 'WILD', run: 'Summer', year_counts: [{year: int, count: int}]}]
    Info:
        In this study populations are distinguised by what species they are (species), if they are hatchery
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


def get_rolling_average(hatchery_provider_response: HatcheryProviderResponse):
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
        # Normalize counts per day by year calculate average per day
        normalized_df = normalize_data(subset_df)
        # Create dictionary with key-value for every day of year
        DOY_dict = daily_frequency(normalized_df)
        # Smooth data by calculating rolling average
        rolling_avg = calculate_rolling_avg(pops, DOY_dict)
        graph_data.append(
            {
                "species": pops["species"],
                "run": pops["run"],
                "origin": pops["origin"],
                "rolling_average": rolling_avg,
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


def normalize_data(subset_df):
    """
    Parameters:
        subset_df: filtered data frame of distinct population
    Output:
        normalized_df: dataframe with the normalized average return for each day of the year
            output columns: ['adult_count', 'year_sum', '%total']
    """

    # Create year_sum column to normalize by
    year_sum = (
        subset_df.groupby("Year")
        .sum("adult_count")
        .rename(columns={"adult_count": "year_sum"})
    )
    subset_df = subset_df.merge(year_sum, on="Year")

    # Normalize adult_count with year_sum
    subset_df["%total"] = subset_df["adult_count"] / subset_df.year_sum

    # Get the average normalized return for each day of the year
    unique_years = len(subset_df.Year.unique())
    normalized_df = subset_df.groupby("DOY").sum("%total") / unique_years
    return normalized_df


def daily_frequency(normalized_df):
    """
    Parameters:
        normalized_df: dataframe with the normalized average return
        for each day of the year
    Output:
        DOY_dict: dict {int: float}
        Dictionary with key as DOY and value as normalized average
    Description:
        Take the normalized average return dataframe and creates a dictionary
        with a key value for every day of the year
    """
    DOY_dict = {}
    index_list = normalized_df.index.tolist()
    for DOY in range(365):
        if str(DOY) in index_list:
            i = normalized_df.index.get_loc(str(DOY))
            value = normalized_df.iloc[[i]]["%total"][0]
            DOY_dict[DOY] = value
        else:
            DOY_dict[DOY] = 0
    return DOY_dict


def calculate_rolling_avg(population, DOY_dict):
    """
    Parameters:
        population: dict {str: str}
            Disticnt population
            example: {'species': 'Chinook', 'origin': 'WILD', run: 'Summer'}
        DOY_dict: dict {int: float}
            Dictionary with key as DOY and value as normalized average
    Output:
        final_dict: dict {int: float}
            Dictionary with key as DOY and value as smoothed normalized average
    """
    if (
        population["species"] == "Coho"
        or population["species"] == "Chum"
        or population["species"] == "Steelhead"
        and population["run"] == "Winter"
    ):
        shifted_dict = shift_forward(DOY_dict)
        series = pd.Series(shifted_dict)
        series.rolling(5, center=True)
        final_dict = shift_backward(series)
        data = make_json_table_format(final_dict)
    else:
        series = pd.Series(DOY_dict)
        series.rolling(5, center=True)
        series = series.round(decimals=3)
        final_dict = series.to_dict()
        data = make_json_table_format(final_dict)
    return data


def shift_forward(DOY_dict):
    """
    Parameters:
        DOY_dict: dict {int: float}
    Output:
        shifted_dict: dict {int: float}
    Decscription:
        Shifts range of dictionary keys from 1-365 to 181 - 546
        Hack for species with a return season that overlaps the year changing
    """
    shifted_dict = {}
    for key in DOY_dict.keys():
        if key < 181:
            shifted_day = 365 + key
            shifted_dict[shifted_day] = DOY_dict[key]
        else:
            shifted_dict[key] = DOY_dict[key]
    return shifted_dict


def shift_backward(series):
    """
    Parameters:
        series: pandas series with DOY as index and average as value
    Output:
        DOY_dict: dict {int: float}
    Description:
        Unshifts previously shift days from 181 - 546 back to 1-365
    """
    unshifted_dict = {}
    for row in series.items():
        percentage = round(row[1], 3)
        if row[0] > 365:
            day = row[0] - 365
            unshifted_dict[day] = percentage
        else:
            unshifted_dict[row[0]] = percentage
    return unshifted_dict


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
