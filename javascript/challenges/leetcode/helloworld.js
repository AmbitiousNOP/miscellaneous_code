var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World"
        
    }
};

var helloworld = createHelloWorld();
console.log(helloworld()); // "Hello World"