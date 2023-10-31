import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)
ax_one = axs[0, 0]
ax_one.set_title('Title')
ax_two = axs[0, 1]
ax_one.set_title('Title')
ax_thr = axs[1, 0]
ax_thr.set_title('Title')
ax_fou = axs[1, 1]
ax_fou.set_title('Title')
# 调整子图之间的间距
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=2)
plt.show()
