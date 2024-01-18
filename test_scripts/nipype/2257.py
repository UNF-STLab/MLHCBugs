from nipype import Workflow, Node, JoinNode
from nipype.interfaces.utility import Merge, Function


def sq(x):
    return x ** 2


wf = Workflow('wf')

square = Node(Function(function=sq), name='square')
square.iterables = ('x', [1, 2])

square_join = JoinNode(Merge(1, ravel_inputs=True),
                       name='square_join',
                       joinsource=square,
                       joinfield=['in1'])

wf.connect(square, 'out', square_join, "in1")

wf.run()