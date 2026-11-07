ZETA DREAMER 3D — WALK INSIDE THE TRAINED PHASE FIELD
====================================================



## November 2026: sharp-field viewer / scroll fix

This update leaves the **original 32-arm, 3 × 128 complex hidden-layer neural network** intact. The low-detail example images were from a *different synthetic training run* and are not the user's old trained model. No network capacity was reduced to make the old 3D viewer. The loss of visual detail came mainly from sampling at 64³, large t-spans relative to spatial wavelength, and drawing a dilated phase-winding mask as opaque fog.

### Fix an HTML world you've already exported (no retraining)

From the updated repository folder, run:

    python3.13 upgrade_existing_world.py "F:\\DocsHouse\\1051\\zeta_world_75_85.html"

Alternatively, in the Python GUI click **↻ SHARPEN OLD 3D HTML** and select the old file. The script creates `zeta_world_75_85_sharp.html` next to it, retaining the original sampled RGB and complex field while generating sub-voxel vortex line segments. It does not alter or overwrite the original. You can upgrade the two checked-in sample HTML worlds the same way. **Previously generated HTML files do not update themselves.**

The viewer now provides:
- **Working independent left-panel scrolling**, including wheel and draggable scrollbar thumb. Only mouse-wheel activity over the 3D canvas adjusts flight speed.
- **Thin, RGB-channel-colored vortex wires**: computed from simultaneous Re(Z)=Im(Z)=0 of the sampled complex channels. A six-tetrahedra-per-cell interpolant solves the crossing points inside the grid instead of swelling mask pixels into a beige volume.
- **Specular/edge lighting** for the RGB gradient surfaces in the hybrid and geometry views, with independent wire thickness.
- **A 96³ export default** and an initially narrow t slab around 79.3–80.9, plus an AROUND SLIDER shortcut. This keeps more spatial and phase variation at visible resolution.

### Full-detail re-export

Load your own checkpoint (or train your images again) and use **ENTER 3D WORLD** with a 96³ grid or 128³ if memory/time allow. Choose a narrow t-slab centered on the fascinating structure. Existing 64³ worlds can be visually improved and their complex-zero curves localized below a grid cell, but lost high-frequency information cannot be reconstructed from their old 8-bit textures.

This remains a **sampled** learned field, not direct full-MLP evaluation at every fragment. The full MLP has 3 complex hidden layers of width 128; evaluating it at every raymarch step would be a substantial per-frame compute cost and needs a dedicated GPU implementation rather than simply copying a few weights into a fragment shader. A precise filament is a zero set of the *interpolated* complex field, not proof of a physical singularity in the source photograph.

WHAT THIS DOES
-------------
This extends your original zeta_dreamer6.py rather than replacing its model.
Train on images at different t values, then choose ✦ ENTER 3D WORLD.
The exporter evaluates the genuine trained complex network at 96 x 96 x 96 by default
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

   scipy is not required; sub-voxel curve extraction uses numpy.
   Tkinter is normally bundled with Windows Python.

2. From the extracted directory:

   python3.13 zeta_dreamer_3d.py

   Alternatively double-click RUN_ZETA_3D.bat (uses python3.13).

3. Use + IMAGE or + FOLDER. Assign t-values (the example uses 5,12,19,26.7).
4. Click START DREAMING and train to a reasonable loss; stop training.
5. Click SAVE MODEL to store network weights in a .pt checkpoint.
6. Click ✦ ENTER 3D WORLD at top left.
7. Choose either TRAINED RANGE or FAR FIELD 75..85. Grid size 96 is now default.
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
48^3 is good for quick tests, 96^3 is the new default, and 128^3 is considerably heavier.

FILES
-----
zeta_dreamer_3d.py             patched original neural model + GUI
zeta_volume_export.py          samples complex volumes and their zero sets
zeta_filament_mesh.py           sub-voxel marching-tetrahedra curve extraction
upgrade_existing_world.py       repair and sharpen an existing exported HTML
zeta_volume_viewer_template.html  offline WebGL2 ray marcher template
example_images/                 four original procedural training examples
example_model.pt               synthetic demo checkpoint
zeta_example_trained_3d.html    standalone walkable demo
zeta_example_farfield_3d.html   standalone walkable far-field demo
RUN_ZETA_3D.bat                Windows launcher
