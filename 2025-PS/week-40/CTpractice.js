// 1. 콜백함수란 무엇인지 설명하고, 간단한 예시 코드를 보여주세요.
// 콜백함수는 다른 함수에 전달되어 일부 작업이 완료된 후 호출되는 함수입니다.
function modifyArray(arr, callback) {
  // 일부 작업
  arr.push(100);
  // 콜백 함수 호출
  callback();
}

const arr = [1, 2, 3, 4, 5];

modifyArray(arr, function () {
  console.log("array has been modified.", arr);
  arr.map((e) => console.log(e + 100));
});


// 2. 해당 문자열을 전체 뒤집기, 단어별로 뒤집기를 출력하세요.
let str = "Hello! Welcome to my Velog. Ask me anything.";

let reverseEntireSentence = str.split("").reverse().join("");
let reverseEachWord = str.split(" ").map((word) => word.split("").reverse().join("")).join(" ");

console.log(reverseEntireSentence);
console.log(reverseEachWord);


// 3. 객체가 배열인지 아닌지를 어떻게 체크하나요? 예시 코드를 보여주세요.
// 자바스크립트에서 함수를 호출하는 방법에는 두 가지가 있다.
// 1) 함수 뒤에 ()를 붙여 호출하는 방법.
// 2) call(), apply()를 사용해 호출하는 방법.

// this는 기본적으로 전역 객체인 window나 메서드를 호출한 객체를 가리킨다.
// apply()와 call() 메서드는 함수 객체에 기본적으로 정의된 메서드로, 첫번째 매개변수를 this로 만들어주는 기능을 한다.
// call()과 apply() 함수의 차이점: call() 함수는 두 번째 매개변수부터 호출할 함수의 인수들이 들어가는데 그냥 넣고, apply() 함수는 배열 형태로 넣는다.
let person1 = {
  name: "Jo"
};

let person2 = {
  name: "Kim",
  study: function () {
    console.log(this.name + "이/가 공부를 하고 있습니다.");
  }
};

person2.study(); // Kim이/가 공부를 하고 있습니다.
person2.study.call(person1); // Jo이/가 공부를 하고 있습니다.

// toString() 함수는 개체를 나타내는 문자열을 반환한다. 
// Object.prototype.toString()을 통해 object 타입을 반환해서 배열 여부를 알 수 있다.
const arr2 = [];

console.log(Object.prototype.toString(arr)); // [object Object]
console.log(Object.prototype.toString.call(arr)); // [object Array]

// 또는 Array.isArray()를 활용하는 방법도 있다.
console.log(Array.isArray(arr2)); // true


// 4. 자바스크립트에서 배열을 비우는 방법은 무엇인가요?
// 1번) 빈 배열을 할당한다.
// 하지만 이 방법은 다른 곳에 원래 배열에 대한 참조가 없는 경우에만 권장된다.
let array = [1, 2, 3, 4, 5];

array = [];
// 2번) 배열의 길이를 0으로 설정한다.
// 원래 배열을 가리키는 모든 참조 변수를 업데이트한다.
array.length = 0;

// 3번) splice() 메서드를 활용한다.
array.splice(0, array.length); // 0번 인덱스부터 array 배열 길이만큼의 원소를 없애겠다.


// 5. 숫자가 정수인지 어떻게 체크할 수 있나요?
// 1로 나눴을 때 나머지가 0이면 정수이다.
function isInt(number) {
  console.log(number % 1 === 0 ? true : false);
}

isInt(1); // true
isInt(0.1); // false


// 6. 두 개의 스택을 사용해 queue를 구현하세요.
// enqueue는 push와 같이 뒤로 추가하고, dequeue는 가장 앞 원소가 빠지는 것이다.
const inputStack = [];
const outputStack = [];

function enqueue(stackInput, item) {
  return stackInput.push(item);
}

function dequeue(stackInput, stackOutput) {
  // 길이가 0보다 작거나 같으면
  if (stackOutput.length <= 0) {
    while (stackInput.length > 0) {
      let element = stackInput.pop()
      stackOutput.push(element);
    } 
  }
  // 0보다 크면
  return stackOutput.pop();
}


// 7. 이게 동작하게 만드세요.
// duplicate([1, 2, 3, 4, 5]) // [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
const arr3 = [1, 2, 3, 4, 5];

function duplicate(arr) {
  // 방법 1: concat - 기존 배열을 변경하지 않으면서 끝에 요소를 추가해 새 배열을 반환한다.
  console.log(arr.concat(arr));
  // 방법 2
  console.log([...arr3, ...arr3]);
}

duplicate(arr3);


// 8. 아래와 같은 방식으로 호출될 때 올바르게 동작하는 mul 함수를 작성하세요. 
// console.log(mul(2)(3)(4)); // 24
function mul(x) {
  return function (y) {
    return function (z) {
      return x * y * z;
    }
  }
}