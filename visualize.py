import re
import matplotlib.pyplot as plt

# Path to the uploaded G‑code file
gcode_path = 'data/maze-8x8.gcode'

coords = []
x = y = None

# Parse the file for G0 / G1 moves to build the XY tool‑path
with open(gcode_path) as f:
    for line in f:
        if line.startswith(';'):           # skip comments
            continue
        m = re.match(r'G0?[01]\s*(.*)', line)
        if not m:
            continue
        params = m.group(1)
        xm = re.search(r'X([-+]?[0-9]*\.?[0-9]+)', params)
        ym = re.search(r'Y([-+]?[0-9]*\.?[0-9]+)', params)
        if xm:
            x = float(xm.group(1))
        if ym:
            y = float(ym.group(1))
        if (x is not None) and (y is not None):
            coords.append((x, y))

# Separate into X and Y lists for plotting
xs, ys = zip(*coords)

plt.figure(figsize=(6, 6))
plt.plot(xs, ys)
plt.gca().set_aspect('equal', 'box')
plt.title('Tool‑path preview: maze‑8x8.gcode')
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')
plt.tight_layout()

# Show the chart to the user
plt.show()
