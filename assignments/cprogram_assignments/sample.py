import sys
from sum_num import sumNum
from stringadd import addString

if len(sys.argv) == 1:
        print("Pass cmd arguments (either num or string)")
else:
        count = 0
        for val in sys.argv[1:]:
                if val.isdigit():
                        count += 1
                        pass
                else:
                        break
        else:
                sumNum(sys.argv[1:])

        if count == 0:
                if all(isinstance(e, str) for e in sys.argv[1:]):
                        for val in sys.argv[1:]:
                                if val.isdigit():
                                        print("Pass cmd arguments (either num or string)")
                                        sys.exit()
                        addString(sys.argv[1:])
                else:
                        print("Pass cmd arguments (either num or string)")
