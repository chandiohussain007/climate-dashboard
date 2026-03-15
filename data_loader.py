import pandas as pd

def load_data():
    url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
    df = pd.read_csv(url, skiprows=1)

    df.columns = df.columns.str.strip()
    df = df[['Year','J-D']].copy()
    df.rename(columns={'J-D':'Temp_Anomaly'}, inplace=True)

    df['Temp_Anomaly'] = pd.to_numeric(df['Temp_Anomaly'], errors='coerce')
    df['Temp_Anomaly'] = df['Temp_Anomaly'].interpolate()
    df['Temp_Anomaly'] = df['Temp_Anomaly'].fillna(df['Temp_Anomaly'].median())

    df['5yr_MA'] = df['Temp_Anomaly'].rolling(5).mean()
    df['10yr_MA'] = df['Temp_Anomaly'].rolling(10).mean()

    return df