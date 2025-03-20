import gradio as gr
import numpy as np
import plotly.graph_objects as go
from calculate_numeric import calculateNumeric

def plot_probabilities(max_n, p_val, q_val, scale_type="linear"):
    max_n = int(max_n)
    p_val = float(p_val)
    q_val = float(q_val)

    print(f'Calculating for N={max_n}, P={p_val}, Q={q_val}, Scale={scale_type}')

    n_values, probabilities = calculateNumeric(max_n, p_val, q_val)

    # Create a Plotly figure with hover information
    fig = go.Figure()

    # Transform to log-odds if selected
    y_values = probabilities.copy()
    hover_format = '%{y:.6f} [n = %{x}]<extra></extra>'
    y_title = 'Probability of X Winning'
    y_range = [0, 1]

    if scale_type == "log-odds":
        # Avoid division by zero or log(0) by clipping probabilities
        clipped_probs = np.clip(probabilities, 1e-10, 1 - 1e-10)
        y_values = np.log(clipped_probs / (1 - clipped_probs))
        hover_format = 'Prob: %{customdata:.6f}<br>Log-odds: %{y:.4f}<br>n = %{x}<extra></extra>'
        y_title = 'Log-odds of X Winning'
        y_range = None  # Auto-scale for log-odds

    # Add the line with markers
    fig.add_trace(go.Scatter(
        x=n_values,
        y=y_values,
        mode='lines+markers',
        line=dict(width=2),
        marker=dict(size=10),
        hovertemplate=hover_format,
        customdata=probabilities if scale_type == "log-odds" else None
    ))

    # Update layout for better appearance
    fig.update_layout(
        title=f'Winning Probability with P={p_val}, Q={q_val}',
        xaxis_title='N (Points to Win)',
        yaxis_title=y_title,
        yaxis=dict(range=y_range) if y_range else {},
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

    # for bigger numbers we get:
    # RecursionError: maximum recursion depth exceeded while calling a Python object
    maxNPossible = 400

    with gr.Row():
        with gr.Column(scale=1):
            max_n = gr.Number(value=30, label="Maximum N (Points to Win)", precision=0, minimum=1, maximum=maxNPossible)
            p_val = gr.Number(value=0.9, label="P (X's winning probability when serving)", precision=4, minimum=0.0, maximum=1.0)
            q_val = gr.Number(value=0.8, label="Q (Y's winning probability when serving)", precision=4, minimum=0.0, maximum=1.0)
            scale_type = gr.Radio(["linear", "log-odds"], label="Scale Type", value="linear")
            calculate_btn = gr.Button("Calculate and Plot")

        with gr.Column(scale=2):
            plot_output = gr.Plot()

    # Button click event
    calculate_btn.click(
        fn=plot_probabilities,
        inputs=[max_n, p_val, q_val, scale_type],
        outputs=plot_output
    )

    # Trigger calculation on Enter in input fields or when radio changes
    max_n.submit(fn=plot_probabilities, inputs=[max_n, p_val, q_val, scale_type], outputs=plot_output)
    p_val.submit(fn=plot_probabilities, inputs=[max_n, p_val, q_val, scale_type], outputs=plot_output)
    q_val.submit(fn=plot_probabilities, inputs=[max_n, p_val, q_val, scale_type], outputs=plot_output)
    scale_type.change(fn=plot_probabilities, inputs=[max_n, p_val, q_val, scale_type], outputs=plot_output)

    # Auto-run the calculation when the page loads
    demo.load(
        fn=plot_probabilities,
        inputs=[max_n, p_val, q_val, scale_type],
        outputs=plot_output
    )

    gr.Markdown("""
    ## How to Use
    1. Set the maximum number of points needed to win (N)
    2. Set P - the probability of team X winning when serving
    3. Set Q - the probability of team Y winning when serving
    4. Choose scale type (linear or log-odds)
    5. Click "Calculate and Plot" to see the results

    Note: Log-odds scale transforms probability p to log(p/(1-p)), which helps visualize small probability differences near 0 or 1.
    """)

if __name__ == "__main__":
    demo.launch()