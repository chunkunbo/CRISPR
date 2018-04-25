# -*- coding: utf-8 -*-
"""

@author: bochunkun
"""

import sys
import random
number = int(sys.argv[1])
pam = sys.argv[2]

foo = ['A','T','G','C']
for i in range(number):
    for j in range(20):
        sys.stdout.write(random.choice(foo)),
    print pam
#print ''
