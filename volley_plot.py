import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
from calculate_numeric import calculateNumeric

def plot_probabilities(max_n, p_val, q_val):
    n_values, probabilities = calculateNumeric(max_n, p_val, q_val)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(n_values, probabilities, 'o-', linewidth=2, markersize=8)
    ax.set_xlabel('N (Points to Win)', fontsize=12)
    ax.set_ylabel('Probability of X Winning', fontsize=12)
    ax.set_title(f'Winning Probability with P={p_val}, Q={q_val}', fontsize=14)
    ax.grid(True)
    ax.set_ylim(0, 1)
    
    # Add exact values as text
    for i, (n, prob) in enumerate(zip(n_values, probabilities)):
        ax.annotate(f'{prob:.4f}', 
                   (n, prob), 
                   textcoords="offset points", 
                   xytext=(0,10), 
                   ha='center')
    
    return fig

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Volleyball Tournament Win Probability Calculator")
    
    with gr.Row():
        with gr.Column(scale=1):
            max_n = gr.Slider(minimum=1, maximum=30, value=8, step=1, label="Maximum N (Points to Win)")
            p_val = gr.Slider(minimum=0.5, maximum=1.0, value=0.99, step=0.01, label="P (X's winning probability when serving)")
            q_val = gr.Slider(minimum=0.5, maximum=1.0, value=0.98, step=0.01, label="Q (Y's winning probability when serving)")
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