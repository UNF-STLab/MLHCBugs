from nipype.pipeline import engine as pe
from nipype.interfaces import utility as niu

select_if = niu.Select(inlist=[[1, 2, 3], [4]], index=1)
select_nd = pe.Node(niu.Select(inlist=[[1, 2, 3], [4]], index=1), name='select_nd')

ifres = select_if.run()
ndres = select_nd.run()

assert ifres.outputs.out == [4]
assert ndres.outputs.out == 4