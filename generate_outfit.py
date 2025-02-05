from gradio_client import Client, handle_file
import re
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Hugging Face token from environment variable
hf_token = os.getenv("HUGGING_FACE_HUB_TOKEN")

# Initialize client with auth
client = Client(
    "levihsu/OOTDiffusion",
    hf_token=hf_token
)

def generate_outfit(model_image, garment_image, n_samples=1, n_steps=20, image_scale=2, seed=-1):
    if model_image is None or garment_image is None:
        return None, "Please upload both model and garment images"
        
    max_retries = 3
    for attempt in range(max_retries):
        try:
            # Use the client to predict
            result = client.predict(
                vton_img=handle_file(model_image),
                garm_img=handle_file(garment_image),
                n_samples=n_samples,
                n_steps=n_steps,
                image_scale=image_scale,
                seed=seed,
                api_name="/process_hd"
            )
            
            # If result is a list, get the first item
            if isinstance(result, list):
                result = result[0]
            
            # If result is a dictionary, try to get the image path
            if isinstance(result, dict):
                if 'image' in result:
                    return result['image'], None
                else:
                    return None, "API returned unexpected format"
                
            return result, None
            
        except Exception as e:
            error_msg = str(e)
            if "exceeded your GPU quota" in error_msg:
                wait_time_match = re.search(r'retry in (\d+:\d+:\d+)', error_msg)
                wait_time = wait_time_match.group(1) if wait_time_match else "60:00"  # Default to 1 hour
                wait_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(wait_time.split(':'))))  # Convert wait time to seconds
                if attempt < max_retries - 1:
                    time.sleep(wait_seconds)  # Wait before retrying
                return None, f"GPU quota exceeded. Please wait {wait_time} before trying again."
            else:
                return None, f"Error: {str(e)}"