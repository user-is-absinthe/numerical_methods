# from matplotlib import pyplot as plt
# from matplotlib.patches import Rectangle
# someX, someY = 0.5, 0.5
# plt.figure()
# currentAxis = plt.gca()
# currentAxis.add_patch(Rectangle((someX - .1, someY - .1), 0.2, 0.2, alpha=1))
# # currentAxis.add_patch(Rectangle((someX - 0.1, someY - 0.1), 0.2, 0.2, alpha=1, facecolor='none'))
# plt.show()


# from matplotlib import pyplot as plt
# from matplotlib.patches import Rectangle
# someX, someY = 0.5, 0.5
# fig, ax = plt.subplots()
# currentAxis = plt.gca()
# currentAxis.add_patch(Rectangle((someX - 0.1, someY - 0.1), 0.2, 0.2,
#                       alpha=1, facecolor='none'))
# plt.show()


from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

a = 0

someX, someY = 0.5, 0.5
plt.figure()
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((someX - .1, someY - .1), 0.2, 0.2, fill=None, alpha=1))
plt.grid(True)
plt.show()
