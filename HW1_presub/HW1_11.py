# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 02:28:13 2016

@author: Tshark
"""

import re

#11
text2 = '"Droll?" said Mr. Newman, laughing too. "Did you ever hear of Christopher Columbus?"'
text = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."

m = re.split('(?<!\w\.\w.)(?<![A-Z]\.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s' , text2)

for i in m :
    print(i + '\n')
    