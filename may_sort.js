
function bubble_sort(my_array) {
  let temp;
  for (let i = 0; i < my_array.length; i++) {
    for (let j = 0; j < my_array.length; j++) {
      if (my_array[j] > my_array[j+1]) {
        temp = my_array[j+1];
        my_array[j+1] = my_array[j];
        my_array[j] = temp;
      }
    }
  }
}

function merge_sort(my_array) {
  if (my_array.length <= 1) {
    return my_array;
  }
  // DONE: slice array
  let middle = 0 | my_array.length / 2;
  let left_part = merge_sort(my_array.slice(0, middle));
  let right_part = merge_sort(my_array.slice(middle));
  return merge(left_part, right_part);
}

function merge(left, right) {
  let new_array = [];
  while (left.length != 0 && right.length != 0) {
    // sort stuff
    if (left[0] > right[0]) {
      // append one part here
      new_array.push(right[0]);
      right.shift();
    }
    else {
      new_array.push(left[0]);
      left.shift();
    }
  }
  // append bigger part here
  if (right.length == 0) {
    new_array = new_array.concat(left);
  }
  else {
    new_array = new_array.concat(right);
  }
  return new_array;
}

function insertion_sort(my_array) {
  let pivot;
  let key;
  for (let i = 1; i < my_array.length; i++) {
    pivot = i - 1;
    key = my_array[i];
    while (pivot >= 0 && my_array[pivot] > key) {
      my_array[pivot + 1] = my_array[pivot];
      pivot--;
    }
    my_array[pivot + 1] = key;
  }
}
// insert all semicolons online app

let my_array = ['8', '9', '1', '2',
                '4', '6', '8', '9',
                '1', '4', '6', '8',
                '9', '1'];

console.log(my_array)
// bubble_sort(my_array)
// insertion_sort(my_array)
// console.log(my_array)
let merge_result = merge_sort(my_array)
console.log(merge_result)
