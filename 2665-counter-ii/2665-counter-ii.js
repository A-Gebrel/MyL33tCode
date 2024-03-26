/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var initial = init;
    var num = init;
    
    function increment() {
        return ++num;
    }
    function decrement() {
        return --num;
    }
    function reset() {
        num = initial;
        return num;
    }
    return { increment, decrement, reset };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */