# Flask Image Compression App

This Flask application allows users to upload images, compress them using Principal Component Analysis (PCA), and download the compressed version. The application utilizes OpenCV and scikit-learn for image processing and PCA-based compression.

## Features

- Upload image files in PNG, JPG, or JPEG formats.
- Compress images using PCA with configurable components.
- Download the compressed image.

## Requirements

- Python 3.6+
- Flask
- OpenCV
- scikit-learn

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install the required Python packages:**

    You can create a virtual environment and install dependencies using `pip`:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Access the app:**

    Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Upload an image:**

    Use the form on the homepage to upload an image file. The app will process the image and provide a link to download the compressed version.

## How It Works

1. **Image Upload:** Users upload an image through the web form.
2. **Image Compression:** The uploaded image is saved temporarily, and PCA-based compression is applied to reduce its dimensionality.
3. **Download:** The compressed image is made available for download.

## Code Overview

- `app.py`: Contains the Flask application setup, routes, and image handling logic.
- `image_compression.py`: Defines the `compress_image` function, which performs PCA-based compression on the image.

## Development

- To contribute or develop further, fork the repository and create a pull request.
- For any issues or feature requests, please open an issue on the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [scikit-learn](https://scikit-learn.org/)

