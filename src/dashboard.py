import pandas as pd
import plotly.express as px
from data_processing import load_data, clean_data

def create_genre_distribution_chart(data):
    """Create a bar chart for genre distribution."""
    genre_counts = data['Genre'].value_counts().reset_index()
    genre_counts.columns = ['Genre', 'Count']
    fig = px.bar(genre_counts, x='Genre', y='Count', title='Distribution of Movie Genres')
    return fig

def create_revenue_vs_rating_scatter(data):
    """Create a scatter plot for revenue vs rating."""
    fig = px.scatter(data, x='Revenue', y='Rating', color='Genre',
                     title='Revenue vs Rating by Genre')
    return fig

def create_rating_distribution_chart(data):
    """Create a histogram for rating distribution."""
    fig = px.histogram(data, x='Rating', title='Distribution of Movie Ratings')
    return fig

def create_dashboard(data):
    """Create and display the dashboard."""
    genre_chart = create_genre_distribution_chart(data)
    revenue_rating_scatter = create_revenue_vs_rating_scatter(data)
    rating_chart = create_rating_distribution_chart(data)

    genre_chart.show()
    revenue_rating_scatter.show()
    rating_chart.show()

if __name__ == "__main__":
    data = load_data('/Users/abdalrhmandarra/Desktop/movie_data_visualization/data/movies.csv')
    clean_data = clean_data(data)
    create_dashboard(clean_data)
