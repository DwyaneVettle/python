import matplotlib.gridspec as gredspec
import matplotlib.pyplot as plt

fig3 = plt.figure()
gs =fig3.add_gridspec(3, 3)
f3_ax1 = fig3.add_subplot(gs[0, :])
f3_ax2 = fig3.add_subplot(gs[0, :-1])
f3_ax3 = fig3.add_subplot(gs[1:, -1])
f3_ax4 = fig3.add_subplot(gs[-1, 0])
f3_ax5 = fig3.add_subplot(gs[-1, -1])
plt.show()
