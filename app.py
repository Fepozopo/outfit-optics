import gradio as gr
from generate_outfit import generate_outfit

# Create Gradio interface
with gr.Blocks() as app:
    gr.Markdown("""
    ## Outfit Optics - Virtually Try On Different Outfits

    - Wait between attempts if you get a quota error

  
    """)

    with gr.Row():
        with gr.Column():
            model_image = gr.Image(
                label="Upload Model Image (person wearing clothes)", 
                type="filepath",
                height=300
                
            )
            model_examples = [
                "./images/models/shane.jpg",
                "./images/models/shanyia.jpg",
                "./images/models/gpa.jpg"
            ]
            gr.Examples(examples=model_examples, inputs=model_image)

            garment_image = gr.Image(
                label="Upload Garment Image (clothing item)", 
                type="filepath",
                height=300
            )
            garment_examples = [
                "./images/garment/b3_bomber-removebg.png",
                "./images/garment/gb_packers_jacket-removebg.png"
            ]
            gr.Examples(examples=garment_examples, inputs=garment_image)

        
        with gr.Column():
            output_image = gr.Image(label="Generated Output")
            error_text = gr.Markdown()  # Add error display
    
    with gr.Row():
        with gr.Column():
            n_samples = gr.Slider(
                label="Number of Samples", 
                minimum=1, 
                maximum=5, 
                step=1, 
                value=1
            )
            n_steps = gr.Slider(
                label="Steps (lower = faster, try 10-15)", 
                minimum=1, 
                maximum=50, 
                step=1, 
                value=10  # Reduced default
            )
            image_scale = gr.Slider(
                label="Scale (lower = faster, try 1-2)", 
                minimum=1, 
                maximum=5, 
                step=1, 
                value=1  # Reduced default
            )
            seed = gr.Number(
                label="Random Seed (-1 for random)", 
                value=-1
            )
    
    generate_button = gr.Button("Generate Outfit")

    # Set up the action for the button
    generate_button.click(
        fn=generate_outfit,
        inputs=[model_image, garment_image, n_samples, n_steps, image_scale, seed],
        outputs=[output_image, error_text]
    )

# Launch the app
app.launch()