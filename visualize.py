import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401, needed for 3‑D projection

gcode_path = 'data/maze-8x8.gcode'

coords = []
x = y = z = None

with open(gcode_path) as f:
    for line in f:
        if line.startswith(';'):
            continue
        m = re.match(r'[GM]0?[01]\s*(.*)', line)
        if not m:
            continue
        params = m.group(1)
        xm = re.search(r'X([-+]?[0-9]*\.?[0-9]+)', params)
        ym = re.search(r'Y([-+]?[0-9]*\.?[0-9]+)', params)
        zm = re.search(r'Z([-+]?[0-9]*\.?[0-9]+)', params)
        if xm:
            x = float(xm.group(1))
        if ym:
            y = float(ym.group(1))
        if zm:
            z = float(zm.group(1))
        if (x is not None) and (y is not None) and (z is not None):
            coords.append((x, y, z))

xs, ys, zs = zip(*coords)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs)

# Equal aspect ratio in 3‑D
max_range = max(max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)) / 2.0
mid_x = (max(xs) + min(xs)) / 2.0
mid_y = (max(ys) + min(ys)) / 2.0
mid_z = (max(zs) + min(zs)) / 2.0
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
ax.set_title('3‑D Tool‑path preview: maze‑8x8.gcode')
plt.tight_layout()
plt.show()
