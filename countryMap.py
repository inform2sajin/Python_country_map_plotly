import plotly.express as pe

# Prompt the user to enter a country name
country = input("Type the country name: ")
data = {
    'Country' : [country],
    'Values' : [100]
}
# Generate a choropleth (geographical heatmap) using Plotly Express
fig = pe.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Values',
    color_continuous_scale='Blues',
    title=f"🌍 Highlighted country map: {country}"
)
# Display the interactive map
fig.show()