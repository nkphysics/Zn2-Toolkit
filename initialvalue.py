import pandas as pd
def setValue(infile):
    data = pd.read_csv(str(infile))
    df = pd.DataFrame(data)
    inval = df['Arrival Times'].iloc[0]
    return (inval)
setValue('D:\Research\Helpful scripts\Extractor\CorrectedFiles\corr40050-04-11-00_123micro.csv')
