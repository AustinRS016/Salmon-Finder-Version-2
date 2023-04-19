
def filterHatcheryData(data):
    desired_columns = ['species', 'origin','run','facility','adult_count','date']
    desired_species = ['Chinook','Coho','Sockeye','Pink','Chum','Steelhead']

    # Use only 'Trap Estimate' events
    df = data[data.event == 'Trap Estimate']

    print(df.head(5))

    # Filter desired columns
    df = df[desired_columns]

    # Filter desired species
    df = df[df.species.isin(desired_species)]
    
    # Remove rows where 'adult_count' == 0
    df = df[df['adult_count'] != 0]

    return df