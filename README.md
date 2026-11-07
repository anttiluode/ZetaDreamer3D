ZETA DREAMER 3D — WALK INSIDE THE TRAINED PHASE FIELD
====================================================

WHAT THIS DOES
-------------
This extends your original zeta_dreamer6.py rather than replacing its model.
Train on images at different t values, then choose ✦ ENTER 3D WORLD.
The exporter evaluates the genuine trained complex network at 64 x 64 x 64
positions (x,y,t) and writes a FULLY SELF-CONTAINED HTML world you can
open by double-clicking in Windows. No server or GPU code is required to
OPEN the exported HTML; Chrome / Edge with WebGL2 hardware support is needed.

Two ready-to-open sample worlds are included, trained on procedural images:
- zeta_example_trained_3d.html   t=4..28, near training images
- zeta_example_farfield_3d.html  t=75..85, far beyond training images

These sample worlds do NOT contain your original screenshots or model weights.
Four example images (in example_images/) and their trained example_model.pt
checkpoint are provided for exploration and comparison.

START RIGHT NOW
---------------
1. Extract the ZIP. Open zeta_example_trained_3d.html in Edge/Chrome.
2. Click ENTER CENTER or click the 3D view and use WASD.
3. Try modes 1 through 5, especially 4 (nodal sheets) and 5 (vortices).
4. Open zeta_example_farfield_3d.html to fly around t near 80.

TRAIN ON YOUR OWN IMAGES
------------------------
1. Make sure Python 3.13 and the following libraries are available:

   python3.13 -m pip install numpy torch Pillow opencv-python

   scipy is optional (used only to widen thin vortex filaments slightly).
   Tkinter is normally bundled with Windows Python.

2. From the extracted directory:

   python3.13 zeta_dreamer_3d.py

   Alternatively double-click RUN_ZETA_3D.bat (uses python3.13).

3. Use + IMAGE or + FOLDER. Assign t-values (the example uses 5,12,19,26.7).
4. Click START DREAMING and train to a reasonable loss; stop training.
5. Click SAVE MODEL to store network weights in a .pt checkpoint.
6. Click ✦ ENTER 3D WORLD at top left.
7. Choose either TRAINED RANGE or FAR FIELD 75..85. Grid size 64 is default.
8. Save the generated HTML. It opens in your browser and remains standalone.

If you close this app, LOAD MODEL restores the weights from its .pt file.
Important: the ORIGINAL unmodified Zeta Dreamer program did not save trained
weights. An already running original process cannot be imported by this
separate process; train again or use a saved checkpoint from this new version.

CONTROLS IN 3D
--------------
Click on the canvas to capture mouse / look around. Esc to release.
WASD: fly forward/back/left/right
R / F: rise / descend
Shift: faster movement
G: teleport to center of sphere; O: outside view
1,2,3,4,5: modes
1: hybrid world (colors, gradient sheets, nodal intersections)
2: image gradient structures
3: translucent image intensity
4: complex real/imaginary nodal sheets
5: candidate vortex filaments
Q / E or arrow keys: turn (when mouse isn't captured)
H: hide/show control panels
P: save PNG screenshot
Mouse wheel over canvas: flight speed

Sliders control threshold, density, screen resolution and ray steps. Reducing
screen resolution and ray steps greatly improves speed on modest hardware.

MATHEMATICAL NOTES
------------------
Your original model computes a continuous complex field
  Z(x,y,t) in C^3,
with prime-logarithm feature frequencies (one per arm). Its normal display is
  RGB = abs(Z(x,y,t)).

The new exporter preserves Re(Z) and Im(Z), and samples 3D data.
Candidate phase-vortex segments are found by checking whether the phase winds
by ±2π around small square loops (plaquettes) of the sampled complex field.
The real-zero and imaginary-zero sets are surfaces; their intersections can
form one-dimensional vortex lines.

The world is a 3D mathematical field with images as learned cross-sections.
It is NOT yet a literal AdS boundary dual, or an optical reconstruction from
photographs arranged around a 2D enclosing shell. That would require a
separate, specified boundary-to-bulk propagation map.

The Riemann zeros are displayed as REFERENCE MARKERS only: the network does
not solve the zeta equation, and the attractive far-field patterns do not
by themselves show special behavior at those zeros.

HIGHER QUALITY
--------------
Train longer for better reproductions at the stored image t values. The
intermediate and far-field patterns reflect how the network generalizes and
extrapolates under its prime-frequency encoding. For GPU memory/performance:
48^3 is good for quick tests, 64^3 is a nice default, 80^3 is heavier.

FILES
-----
zeta_dreamer_3d.py             patched original neural model + GUI
zeta_volume_export.py          samples complex volumes and phase winding
zeta_volume_viewer_template.html  offline WebGL2 ray marcher template
example_images/                 four original procedural training examples
example_model.pt               synthetic demo checkpoint
zeta_example_trained_3d.html    standalone walkable demo
zeta_example_farfield_3d.html   standalone walkable far-field demo
RUN_ZETA_3D.bat                Windows launcher
