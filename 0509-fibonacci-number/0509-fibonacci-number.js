/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if(n == 0)
        return 0;
    else if(n == 1)
        return 1;
    else
    {
        var first = 0;
        var second = 1;
        var next = 0;
        for(var i=0; i<n-1; i++)
        {
            next = first+second;
            first = second;
            second = next;
        }
        return next;
    }
};