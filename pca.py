import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import cv2

# Load the image
img = cv2.cvtColor(cv2.imread('D:\koshis\pca\image1.jpg'), cv2.COLOR_BGR2RGB)

# Splitting into channels
blue, green, red = cv2.split(img)

# Normalize the channels
df_blue = blue / 255
df_green = green / 255
df_red = red / 255

# Perform PCA on each channel separately
pca_b = PCA(n_components=50)
pca_b.fit(df_blue)
trans_pca_b = pca_b.transform(df_blue)

pca_g = PCA(n_components=50)
pca_g.fit(df_green)
trans_pca_g = pca_g.transform(df_green)

pca_r = PCA(n_components=50)
pca_r.fit(df_red)
trans_pca_r = pca_r.transform(df_red)

# Reconstruct the channels
b_reconstructed = np.dot(trans_pca_b, pca_b.components_) + pca_b.mean_
g_reconstructed = np.dot(trans_pca_g, pca_g.components_) + pca_g.mean_
r_reconstructed = np.dot(trans_pca_r, pca_r.components_) + pca_r.mean_

# Merge the channels back together
img_reduced = np.clip(cv2.merge((b_reconstructed, g_reconstructed, r_reconstructed)), 0, 1)

# Display the original and reduced images
fig = plt.figure(figsize=(10, 7.2))
fig.add_subplot(121)
plt.title("Original Image")
plt.imshow(img)
fig.add_subplot(122)
plt.title("Reduced Image")
plt.imshow(img_reduced)
plt.show()
