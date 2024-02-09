## 🏁 5308. Hello Algo
헬로알고는 강의를 듣는 여러분들을 매우 환영하기 위해 한 가지 무한 문자열을 만들려 한다.<br>
$Welcome$(1) = "Hello "<br>
$Welcome$(2) = "Hello Algo "<br>
$Welcome$(3) = "Hello Algo Hello "<br>
$Welcome$(4) = "Hello Algo Hello Hello Algo "<br>
$Welcome$(5) = "Hello Algo Hello Hello Algo Hello Algo Hello "

환영문자열 Welcome은 피보나치 수열과 유사하게 $Welcome$($i$)는 $Welcome$($i$-1) 뒤에 $Welcome$($i$-2)를 이어 붙힌 것으로 정의된다.
<br>이 때 충분히 큰 $N$에 대해서 $Welcome$($N$)의 x번째 글자가 무엇인지 궁금해졌다. 

첫째 줄에 테스트케이스의 개수 $T$($T$ ≤ 100)가 주어진다.
<br>이후 $T$개 줄에 걸쳐 알고자하는 문자열의 문자 번호 $x$가 주어진다.

$T$개 줄에 걸쳐 주어진 $x$에 대해 $Welcome$ 문자열에서 $x$번째 문자가 무엇인지 출력한다.(1 ≤ $x$ ≤ $2^{30}-1$)
<br>단 $x$번째 문자가 공백일 경우에는 "Hello Algo"를 출력한다.

### 📝 입력 예제
5<br>
3<br>
6<br>
10<br>
15<br>
21

### 🖨️ 출력 예제
l<br>
Hello Algo<br>
o<br>
l<br>
l