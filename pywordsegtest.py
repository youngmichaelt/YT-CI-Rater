# import the module
from pywordseg import *

# declare the segmentor.
seg = Wordseg(batch_size=64, embedding='w2v', mode="TW")

# input is a list of raw sentences.
# seg.cut(["今天天氣真好啊!", "潮水退了就知道，誰沒穿褲子。"])

print(seg.cut(["今天天氣真好啊!", "潮水退了就知道，誰沒穿褲子。"])
)