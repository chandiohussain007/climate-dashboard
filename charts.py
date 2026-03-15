import plotly.express as px
import plotly.graph_objects as go

def trend_chart(df):
    fig = px.line(
        df,
        x="Year",
        y=["Temp_Anomaly","5yr_MA","10yr_MA"],
        title="Global Temperature Trend"
    )
    return fig


def gauge_chart(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text':"Current Temperature Anomaly"},
        gauge={
            'axis':{'range':[-1,2]},
            'bar':{'color':"red"}
        }
    ))
    return fig


def heatmap_chart(df):

    df['Decade'] = (df['Year']//10)*10
    pivot = df.pivot_table(values="Temp_Anomaly",index="Decade")

    fig = px.imshow(
        pivot,
        color_continuous_scale="RdBu_r",
        title="Temperature Heatmap"
    )

    return fig