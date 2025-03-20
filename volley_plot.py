import gradio as gr
import numpy as np
import plotly.graph_objects as go
from calculate_numeric import calculateNumeric

def plot_probabilities(max_n, p_val, q_val):
    max_n = int(max_n)
    p_val = float(p_val)
    q_val = float(q_val)

    print(f'Calculating for N={max_n}, P={p_val}, Q={q_val}')

    n_values, probabilities = calculateNumeric(max_n, p_val, q_val)

    print(f'Results: {probabilities}')

    # Create a Plotly figure with hover information
    fig = go.Figure()
    
    # Add the line with markers
    fig.add_trace(go.Scatter(
        x=n_values, 
        y=probabilities,
        mode='lines+markers',
        line=dict(width=2),
        marker=dict(size=10),
        hovertemplate='<b>N=%{x}</b><br>P(win)=%{y:.6f}<extra></extra>'
    ))
    
    # Update layout for better appearance
    fig.update_layout(
        title=f'Winning Probability with P={p_val}, Q={q_val}',
        xaxis_title='N (Points to Win)',
        yaxis_title='Probability of X Winning',
        yaxis=dict(range=[0, 1]),
        hovermode='closest',
        template='plotly_white',
        height=500,
        width=800
    )
    
    # Add grid
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

    return fig

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Volleyball Tournament Win Probability Calculator")

    with gr.Row():
        with gr.Column(scale=1):
            max_n = gr.Number(value=8, label="Maximum N (Points to Win)", precision=0, minimum=1, maximum=100)
            p_val = gr.Number(value=0.99, label="P (X's winning probability when serving)", precision=4, minimum=0.0, maximum=1.0)
            q_val = gr.Number(value=0.98, label="Q (Y's winning probability when serving)", precision=4, minimum=0.0, maximum=1.0)
            calculate_btn = gr.Button("Calculate and Plot")

        with gr.Column(scale=2):
            plot_output = gr.Plot()

    calculate_btn.click(
        fn=plot_probabilities,
        inputs=[max_n, p_val, q_val],
        outputs=plot_output
    )

    gr.Markdown("""
    ## How to Use
    1. Set the maximum number of points needed to win (N)
    2. Set P - the probability of team X winning when serving
    3. Set Q - the probability of team Y winning when serving
    4. Click "Calculate and Plot" to see the results
    """)

if __name__ == "__main__":
    demo.launch()