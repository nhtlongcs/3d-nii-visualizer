import numpy as np
# default brain settings
APPLICATION_TITLE = "Theia – NIfTI (nii.gz) 3D Visualizer"
BRAIN_SMOOTHNESS = 500
BRAIN_OPACITY = 0.2
BRAIN_COLORS = [(1.0, 0.9, 0.9)]  # RGB percentages

# default mask settings
MASK_SMOOTHNESS = 500


def color_map(n=256, normalized=False):
    def bitget(byteval, idx):
        return (byteval & (1 << idx)) != 0

    dtype = "float32" if normalized else "uint8"
    cmap = np.zeros((n, 3), dtype=dtype)
    for i in range(n):
        r = g = b = 0
        c = i
        for j in range(8):
            r = r | (bitget(c, 0) << 7 - j)
            g = g | (bitget(c, 1) << 7 - j)
            b = b | (bitget(c, 2) << 7 - j)
            c = c >> 3

        cmap[i] = np.array([r, g, b])

    cmap = cmap / 255 if normalized else cmap
    return cmap


MASK_COLORS = color_map(normalized=True)[1:][::-1]
# [(1, 0, 0),
#                 (0, 1, 0),
#                 (1, 1, 0),
#                 (0, 0, 1),
#                 (1, 0, 1),
#                 (0, 1, 1),
#                 (1, 0.5, 0.5),
#                 (0.5, 1, 0.5),
#                 (0.5, 0.5, 1)]  # RGB percentages
MASK_OPACITY = 1.0