# Outfit Optics

## Description

This Gradio app allows you to virtually try on different outfits by uploading a model image (a person wearing clothes) and a garment image (a clothing item). The app uses a machine learning model to generate an output image of the model wearing the garment.

## Motivation

I made this app at the request of my wife, who wanted to try on different outfits online wihtout having to go to a physical store. It's a fun way to experiment with different outfits and see how they look on a person.

## Prerequisites

* Gradio
* Python 3.8 or higher
* pip install -r requirements.txt

## How to use

1. Upload a model image by clicking the "Upload Model Image" button.
2. Upload a garment image by clicking the "Upload Garment Image" button.
3. Adjust the "Number of Samples" slider to control how many output images are generated.
4. Adjust the "Steps" slider to control how many iterations the model runs.
5. Adjust the "Scale" slider to control the size of the output image.
6. Click the "Generate Outfit" button to generate an output image.
7. The output image will be displayed in the "Generated Output" section.

## Notes

* The model may not work well if the garment image is very large or very small.
* The model may not work well if the model image is not a person wearing clothes.
* The model may not work well if the garment image is not a clothing item.
* The model may not work well if the background of the model image or garment image is not a solid color.
* The model may not work well if the garment image is transparent.

## Setting up locally

1. Clone the repository with `git clone https://github.com/Fepozopo/outfit-optics`
2. Install the required packages with `pip install -r requirements.txt`
3. If you want to use your own Hugging Face token, create a `.env` file with `HUGGING_FACE_HUB_TOKEN=<your token here>`. This will allow for more quota.
4. Run the app with `python app.py`
5. Open the app in a web browser at `http://localhost:7860`
