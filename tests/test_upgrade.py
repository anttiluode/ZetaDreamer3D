"""End-to-end test: old packed volume HTML to upgraded standalone viewer."""
import base64
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import numpy as np

from upgrade_existing_world import upgrade, read_payload, unpack_complex


class WorldUpgradeTest(unittest.TestCase):
    def test_old_html_upgrades_without_training(self):
        n=13
        a=np.linspace(-1,1,n,dtype=np.float32)
        zz,yy,xx=np.meshgrid(a,a,a,indexing='ij')
        raw=np.ones((n,n,n,3,2),dtype=np.float32)
        raw[...,0,0]=xx-.13
        raw[...,0,1]=yy-.19
        encoded=np.clip(np.rint((raw*.5+.5)*255),0,255).astype(np.uint8)
        c0=encoded[...,:2,:].reshape(n,n,n,4)
        c1=np.concatenate((encoded[...,2,:],np.zeros((n,n,n,2),dtype=np.uint8)),axis=-1)
        rgb=np.zeros((n,n,n,4),dtype=np.uint8)
        def b64(array):
            return base64.b64encode(array.tobytes()).decode('ascii')
        data={
            'rgb':b64(rgb),'c0':b64(c0),'c1':b64(c1),
            'size':n,'t0':79.3,'t1':80.9,'anchors':[5,12],'zeros':[79.337]
        }
        with TemporaryDirectory() as temp:
            old=Path(temp)/'old.html'
            old.write_text('<script>const EMBEDDED = '+json.dumps(data)+';</script>',encoding='utf-8')
            recovered=read_payload(old.read_text('utf-8'))
            np.testing.assert_allclose(unpack_complex(recovered)[...,0,0],np.clip(raw[...,0,0],-1,1),atol=.009)
            details=upgrade(old)
            self.assertGreater(details['filament_segment_count'],0)
            new=Path(details['output'])
            html=new.read_text('utf-8')
            self.assertIn('drawArraysInstanced',html)
            self.assertIn('overflow-y:scroll',html)
            self.assertIn('LINE_VERT',html)
            self.assertIn('"segments":"',html)
            self.assertTrue(old.exists())
            self.assertNotEqual(new,old)


if __name__=='__main__':
    unittest.main()
