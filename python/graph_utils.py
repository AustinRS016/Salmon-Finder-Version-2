import pandas as pd

def format_data(population, df):
        '''
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
        '''
        subset_df = df[(df.species == population['species']) & (df.run == population['run']) & (df.origin == population['origin'])]
        # For now any duplicates are simply removed
        duplicates_df = subset_df.index[subset_df.duplicated('date')].tolist()
        for dup in duplicates_df:
            subset_df = subset_df.drop(dup) 
        return subset_df

def normalize_data(subset_df):
        '''
        Parameters:
            subset_df: filtered data frame of distinct population
        Output:
            normalized_df: dataframe with the normalized average return for each day of the year
                output columns: ['adult_count', 'year_sum', '%total']
        '''
        
        # Create year_sum column to normalize by
        year_sum = subset_df.groupby('Year').sum('adult_count').rename(columns = {'adult_count': 'year_sum'})
        subset_df = subset_df.merge(year_sum, on='Year')

        # Normalize adult_count with year_sum
        subset_df['%total'] = subset_df['adult_count']/subset_df.year_sum

        # Get the average normalized return for each day of the year
        unique_years = len(subset_df.Year.unique())
        normalized_df = subset_df.groupby('DOY').sum('%total')/unique_years  
        return normalized_df

def daily_frequency(normalized_df):
        '''
        Parameters: 
            normalized_df: dataframe with the normalized average return 
            for each day of the year
        Output:
            DOY_dict: dict {int: float}
            Dictionary with key as DOY and value as normalized average
        Description:
            Take the normalized average return dataframe and creates a dictionary 
            with a key value for every day of the year
        '''
        DOY_dict = {}
        index_list = normalized_df.index.tolist()
        for DOY in range(365):
            if str(DOY) in index_list:
                i = normalized_df.index.get_loc(str(DOY))
                value = normalized_df.iloc[[i]]['%total'][0]
                DOY_dict[DOY] = value
            else:
                DOY_dict[DOY] = 0
        return DOY_dict

def calculate_rolling_avg(population, DOY_dict):
        '''
        Parameters:
            population: dict {str: str}
                Disticnt population
                example: {'species': 'Chinook', 'origin': 'WILD', run: 'Summer'} 
            DOY_dict: dict {int: float}
                Dictionary with key as DOY and value as normalized average
        Output:
            final_dict: dict {int: float}
                Dictionary with key as DOY and value as smoothed normalized average
        '''
        if population['species'] == 'Coho' or population['species'] == 'Chum' or population['species'] == 'Steelhead' and population['run'] == 'Winter':
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
        '''
        Parameters: 
            DOY_dict: dict {int: float}
        Output: 
            shifted_dict: dict {int: float}
        Decscription: 
            Shifts range of dictionary keys from 1-365 to 181 - 546
            Hack for species with a return season that overlaps the year changing
        '''
        shifted_dict = {}
        for key in DOY_dict.keys():
            if (key < 181):
                shifted_day = 365 + key
                shifted_dict[shifted_day] = DOY_dict[key]
            else:
                shifted_dict[key] = DOY_dict[key]
        return shifted_dict

def shift_backward(series):
        '''
        Parameters:
            series: pandas series with DOY as index and average as value
        Output:
            DOY_dict: dict {int: float}
        Description:
            Unshifts previously shift days from 181 - 546 back to 1-365
        '''
        unshifted_dict = {}
        for row in series.iteritems():
            percentage = round(row[1], 3)
            if row[0] > 365:
                day = row[0] - 365
                unshifted_dict[day] = percentage
            else:
                unshifted_dict[row[0]] = percentage
        return unshifted_dict

def make_json_table_format(dict):
        '''
        Parameters: dict {string: number}
        Output: dict [{string: number, string, number}...]
        Description:
        Changes data from {DayOfYear: FishCount} to {day: DayOfYear, and count: FishCount}
        Data format is more easily consumed by D3.js
        '''
        dictArr = []
        for key in dict:
            new_value = {"day": key, "count": dict[key]}
            dictArr.append(new_value)
        return dictArr
          
        