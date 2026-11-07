"""Deterministic mathematics checks for Zeta Dreamer sub-voxel filaments."""
import ast
import base64
import pathlib
import unittest
import numpy as np
from zeta_filament_mesh import _face_roots, extract_vortex_segments

ROOT=pathlib.Path(__file__).resolve().parents[1]


class FilamentTests(unittest.TestCase):
    def test_triangle_complex_zero(self):
        values=np.array([[[1.,0.],[0.,1.],[-1.,-1.]]],dtype=np.float32)
        tri=np.array([[[0.,0.,0.],[1.,0.,0.],[0.,1.,0.]]],dtype=np.float32)
        valid,points=_face_roots(values,tri)
        self.assertTrue(bool(valid[0]))
        np.testing.assert_allclose(points[0],[1/3,1/3,0],atol=1e-6)

    def test_known_line_intersects_volume(self):
        n=22
        grid=np.linspace(-1,1,n,dtype=np.float32)
        Z,Y,X=np.meshgrid(grid,grid,grid,indexing='ij')
        raw=np.ones((n,n,n,3,2),dtype=np.float32)
        # The red complex field is exactly (x-0.13)+i(y-0.19).
        # Its simultaneous zero set is a straight vertical filament.
        raw[...,0,0]=X-.13
        raw[...,0,1]=Y-.19
        encoded,stats=extract_vortex_segments(raw)
        self.assertGreater(stats['filament_segment_count'],5)
        binary=base64.b64decode(encoded)
        arr=np.frombuffer(binary,dtype='<u2').reshape(-1,8)
        self.assertTrue(np.all(arr[:,6]==0))
        pts=arr[:,:6].reshape(-1,2,3).astype(np.float64)/32767.5-1.
        np.testing.assert_allclose(pts[:,:,0],.13,atol=0.0002)
        np.testing.assert_allclose(pts[:,:,1],.19,atol=0.0002)
        self.assertGreater(float(np.ptp(pts[:,:,2])),1.0)

    def test_constant_complex_field_has_no_filaments(self):
        field=np.ones((12,12,12,3,2),dtype=np.float32)
        encoded,stats=extract_vortex_segments(field)
        self.assertEqual(stats['filament_segment_count'],0)
        self.assertEqual(base64.b64decode(encoded),b'')

    def test_templates_and_python_syntax(self):
        for path in ('zeta_volume_export.py','zeta_filament_mesh.py','zeta_dreamer_3d.py'):
            ast.parse((ROOT/path).read_text('utf-8'),filename=path)
        html=(ROOT/'zeta_volume_viewer_template.html').read_text('utf-8')
        for term in ('LINE_VERT=','LINE_FRAG=','drawArraysInstanced','canvas.addEventListener(\'wheel\'','overflow-y:scroll','__EMBEDDED_DATA__'):
            self.assertIn(term,html)
        exporter=(ROOT/'zeta_volume_export.py').read_text('utf-8')
        self.assertIn("'segments': segments",exporter)


if __name__=='__main__':
    unittest.main()
