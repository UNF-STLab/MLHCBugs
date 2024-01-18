from nipype.pipeline import engine as pe
from nipype.interfaces import utility as niu

def test_collapsing():
    select_if = niu.Select(inlist=[[1, 2, 3], [4]], index=1)
    select_nd = pe.Node(niu.Select(inlist=[[1, 2, 3], [4]], index=1), name='select_nd')

    ifres = select_if.run()
    ndres = select_nd.run()

    if ifres.outputs.out == [4] and ndres.outputs.out == [4] and select_nd.result.outputs.out == [4]:
        print("pass")
    else:
        print("Fail")

test_collapsing()