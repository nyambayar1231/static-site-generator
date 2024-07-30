const { assert } = require('node:console');

function morphFoo(foo) {
  assert(foo.bar !== undefined, 'foo must exist');
  return foo.bar * 5;
}

morphFoo({
  bar: undefined,
});
