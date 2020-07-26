From Wikipedia, the free encyclopedia

# JavaScript Language

Often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.[7] JavaScript is high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.

## History

The Mosaic web browser was released in 1993. As the first browser with a graphical user interface accessible to non-technical people, it played a prominent role in the rapid growth of the nascent World Wide Web.[10] The lead developers of Mosaic then founded the Netscape corporation, which released a more polished browser, Netscape Navigator, in 1994. Navigator quickly became the most used browser.

## Simple examples

### A simple recursive function

```
function factorial(n) {
	if (n === 0)
		return 1; // 0! = 1
	return n * factorial(n - 1);
}
factorial(3); // returns 6
```

