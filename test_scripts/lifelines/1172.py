from lifelines import WeibullAFTFitter
from lifelines.datasets import load_rossi

rossi = load_rossi()
rossi["arrest"] = 0
wf = WeibullAFTFitter().fit(rossi, "week", "arrest")
wf.print_summary()