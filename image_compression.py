import numpy as np
import cv2
from sklearn.decomposition import PCA

def compress_image(image_path, output_path, n_components=50):
    # Load image and convert to RGB
    img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    # Split into channels
    blue, green, red = cv2.split(img)

    # Normalize channels
    df_blue = blue / 255.0
    df_green = green / 255.0
    df_red = red / 255.0

    # Reshape each channel to 2D (for PCA)
    df_blue_flat = df_blue.reshape(-1, df_blue.shape[1])
    df_green_flat = df_green.reshape(-1, df_green.shape[1])
    df_red_flat = df_red.reshape(-1, df_red.shape[1])

    # Perform PCA
    pca_b = PCA(n_components=n_components)
    trans_pca_b = pca_b.fit_transform(df_blue_flat)

    pca_g = PCA(n_components=n_components)
    trans_pca_g = pca_g.fit_transform(df_green_flat)

    pca_r = PCA(n_components=n_components)
    trans_pca_r = pca_r.fit_transform(df_red_flat)

    # Reconstruct the channels
    b_reconstructed = pca_b.inverse_transform(trans_pca_b).reshape(df_blue.shape)
    g_reconstructed = pca_g.inverse_transform(trans_pca_g).reshape(df_green.shape)
    r_reconstructed = pca_r.inverse_transform(trans_pca_r).reshape(df_red.shape)

    # Merge channels and clip to 0-1 range
    img_reduced = np.clip(cv2.merge((b_reconstructed, g_reconstructed, r_reconstructed)), 0, 1)

    # Convert back to original 0-255 scale
    img_reduced = (img_reduced * 255).astype(np.uint8)

    # Save the compressed image
    cv2.imwrite(output_path, cv2.cvtColor(img_reduced, cv2.COLOR_RGB2BGR))
    