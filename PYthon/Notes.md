# 📝 MERN Stack Test (30 Questions)

## Section A: JavaScript (6 Qs)
1. Explain the difference between var, let, and const with examples.  
Ans: Var: it is global variable. redeclare and reAssign, Hoisting is possible
    Let: it is block level variable, not redeclare, reAssign possible and Hoisting not possible,

    Const : it is block level variable, not  redeclare,not  reAssign possible and Hoisting not possible,


2. What is closure in JavaScript? Give an example.  
Closure is nested function type here function store the value on inner variable then return new value on new call.
```js
    const add = ()=>{
        let value = 0;
        return ()=>{
            return value ++
        }
    }

    const add1 = add()
    add1()
```
3. Explain the event loop in Node.js.  
    Event loop is mechanism here javascript handle the multiple task at same execution like asynchrons program . because javaScript is a single thread programming language. every task execute in call tack then any task were take time this go in web Api then complete go call back Que and event loop check call back que every time empty 

4. What will be the output?  
   ```js
   console.log(a);
   var a = 5;
   let b = 10;
   console.log(b);

   <!-- Out PUT -->
   undefine
   10

5. What is the difference between == and ===?
 == it check value only 
 === it check data type and value
6. Write a function to reverse a string in JavaScript.
```js
function revStr(str){
const arrayStr = str.split('')
console.log(arrayStr.reverse().join(''));

}
revStr("amar")
```
7. Difference between state and props in React.
props is properties here pass data one component to another,
sate is value only component use it
8. What is the purpose of useEffect hook? Give an example.
call the data on load API or website
9. How would you implement conditional rendering in React?
    use ternary operator and &&
10. Write React code to display a list of todos = ["Buy Milk", "Read Book"].
```js        
<div>
{todos.map((value)=>{
    return value
})}
<div>
```


11. What is virtual DOM and why is it faster?
 it is copy on real dom
12. How do you handle forms and controlled components in React?
using prventdefault

13. What is middleware in Express? Example.
Middle ware function this function is call on req and res between it check validation example next() in express json() 
14. Write an Express route for GET /users that returns all users.
    ```js
    app.get('/users',(err,req,next,res)=>{
        return res.send("all users")
    })
    ```
15. How do you handle errors in Express apps?
using trycatch

16. Explain the difference between synchronous and asynchronous code in Node.js.
synchronous : code execute line by line top to bottom
asynchronous : promise complete then execute


17. What is the purpose of package.json file?
    here store all package for project  
18. Write code to create a simple Express server running on port 5000.
```js
const express = require('express')
const app = express()
app.listen(5000)
```

Section D: MongoDB (6 Qs)

19. Difference between SQL vs NoSQL.
    SQL: Structure Query language , , data store in table, row column, it vertical expand

    NOSQL: data store in document, field, value, horizontal scale, data tore in JSON and BSON 

20. What is a Mongoose schema? Write a schema for a User with name, email, and password.

Schema is data storing design which data store here.
```js
import mongoose from "mongoose"
const userSchema = new mongoose.Schema({
    name:String,
    email:String,
    password:String
})
```

21. Write a query to find all users with age > 18.
    ```js
    const data=  userData.find({age:{$gt:18}})
    ```
22. How do you connect MongoDB with Node.js using Mongoose?
```js
import mongoose from "mongoose"
mongoose.connect(url)
```
23. Explain indexes in MongoDB. Why are they useful?

24. What is the difference between findOne() and findById() in Mongoose?
findOne(): match first value 
findByID() : find mongoDB ID like ID generated unique


Explain the flow of a MERN app when a user logs in (frontend → backend → DB → response).

How would you implement JWT authentication in MERN stack? Steps only.

Write API endpoints for a Todo app: create, read, delete.

How do you handle CORS issues in a MERN app?

Explain the difference between REST API and GraphQL.

Deploying a MERN app: which services can you use for frontend, backend, and DB?