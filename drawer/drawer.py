import plotly.graph_objects as go


class Drawer:


    @staticmethod
    def draw_data(x, y, country):
        '''
        
        '''

        # Create a Plotly figure
        fig = go.Figure()

        # Add a trace for the line graph
        fig.add_trace(
            go.Scatter(
                x = x,
                y =  y,
                mode='lines+markers',
                name='Data'
            )
        )

        # Update layout
        fig.update_layout(
            title='Population of ' + country,
            xaxis_title='years',
            yaxis_title='Numbers of people',
        )

        return fig
