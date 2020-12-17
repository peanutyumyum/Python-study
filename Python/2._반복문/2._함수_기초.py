import test
test.add()

from test import * # test파일에 있는 모든 것을 가져온다는 뜻 이러면 평소에 함수 이용하는 문법으로 이용하면 됨

import test as p # test를 p처럼 사용하겠다
p.add()