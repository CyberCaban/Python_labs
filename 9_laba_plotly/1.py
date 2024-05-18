import plotly.express as px
import pandas as pd

df = pd.read_csv("./data_country.csv")
fig = px.imshow(
    df,
    text_auto=True,
    aspect="auto",
    origin="lower",
    labels=dict(x="Stats", y="Country", color="Value"),
)
fig.show()
