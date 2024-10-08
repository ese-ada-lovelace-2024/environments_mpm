# import os
# import sys
# package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(package_path)

from envtest import rand_array

shape = (3, 3)

print(rand_array(shape))
