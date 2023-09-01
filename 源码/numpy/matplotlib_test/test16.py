import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(100)
plt.boxplot(data, meanline=True, widths=0.3, patch_artist=True,
            showfliers=False)
plt.show()
