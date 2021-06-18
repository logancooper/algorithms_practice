console.log("hello world");

//Given an array of integers, find the largest product of three integers.
const problemOneInput = [-10, 7, 29, 30, 5, -10, -70];
// Expected return 21000
function LargestIntegersProduct(inputArray)
{
    let currentLargest = null;
    //for each number in the array
    for(let i = 0; i < inputArray.length; i++)
    {
        //look at every number in the array
        for(let j = 0; j < inputArray.length; j++)
        {
            //AND DO IT AGAIN
            for(let k = 0; k < inputArray.length; k++)
            {
                //if the current largest hasn't been set
                if(currentLargest == null)
                {
                    //assign a the value 
                    console.log("Assigning " + (inputArray[i] * inputArray[j] * inputArray[k]) + " to currentLargest");
                    currentLargest = inputArray[i] * inputArray[j] * inputArray[k];
                }
                //if the new value to test is larger than the old largest
                else if((inputArray[i] * inputArray[j] * inputArray[k]) > currentLargest)
                {
                    //make sure it's not the same index
                    if(i != j && i != k && j != k)
                    {
                        //assign the new current largest
                        console.log("Assigning " + (inputArray[i] * inputArray[j] * inputArray[k]) + " to currentLargest");
                        currentLargest = inputArray[i] * inputArray[j] * inputArray[k];
                    }
                }
            }
        }
    }
    return currentLargest;
}
//console.log(LargestIntegersProduct(problemOneInput));


//Given an array of integers, remove the duplicates and return an array of only unique elements.
const problemTwoInput = [1, 2, 3, 5, 1, 5, 9, 1, 2, 8];
// Excpected return [ 1, 2, 3, 5, 9, 8 ]
function RemoveDuplicates(inputArray)
{
    //for each index
    for(let i = 0; i < inputArray.length; i++)
    {
        //look at every other index
        for(let j = 0; j <inputArray.length;j++)
        {
            //if they are the same numerically
            if(inputArray[i] == inputArray[j])
            {
                //and they are not the same index
                if(i != j)
                {
                    //remove the number
                    inputArray.splice(j,1);
                }
            }
        }
    }
    return inputArray;
}
//console.log(RemoveDuplicates(problemTwoInput));


//Given two arrays, find the intersecting integers of the arrays.
const firstArray = [2, 2, 4, 1];
const secondArray = [1, 2, 0, 2];
// Expected return [2, 1]
function IntersectingArrays(inputArrayOne, inputArrayTwo)
{
    let returnArray = [];
    //for every number in the first array
    for(let i = 0; i < inputArrayOne.length; i++)
    {
        //look at every number in the second array
        for(let j = 0; j < inputArrayTwo.length; j++)
        {
            //if they are matches...
            if(inputArrayOne[i] = inputArrayTwo[j])
            {
                //and if it is not already in the return array
                if(!returnArray.includes(inputArrayOne[i]))
                {
                    //push the number to the return array
                    returnArray.push(inputArrayOne[i]);
                }
            }
        }
    }
    return returnArray;
}
//console.log(IntersectingArrays(firstArray,secondArray));

//How do you get the nth number of a fibonnaci sequence? The Fibonacci Sequence is the series of numbers:
//0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
//The next number is found by adding up the two numbers before it
//input 9
//expected outcome 21
function Fibonnaci(input)
{
    let previousNum = 0;
    let currentNum = 1;
    let nextNum = null;
    for(let i = 2; i < input; i++)
    {
        nextNum = currentNum + previousNum;
        previousNum = currentNum;
        currentNum = nextNum;
    }
    return currentNum;
}
//console.log(Fibonnaci(9));


//Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
const array = [9,6,4,3,2,5,7,0,1];
//expected answer 8
function MissingNumber(inputArray)
{
    let answer = 0;
    //find the highest number in the array
    let highestNumber = 0;
    inputArray.forEach(number => {
        if(number > highestNumber)
        {
            highestNumber = number;
        }
    });

    //iterate from 1->highestNumber
    for(let i = 0; i < highestNumber; i++)
    {
        //at each iteration, check if the current iteration number is missing from the array. If it is...
        if(!inputArray.includes(i))
        {
            //return the number
            answer = i;
            return i;
        }
    }
}
console.log(MissingNumber(array));


//Find the square root of 81.
function SquareRoot()
{

}