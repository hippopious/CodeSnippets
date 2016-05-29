// Given an array (or any linear data structure), print out all unique combinations of ints that sums to a target value
// To simplify the problem, the target value cannot exceed 200
// Bool's problem is that two identical numbers that add to target will not be logged (i.e. 100 + 100 = 200)

// arrayOfValues [0, 100]  <-- 101 possible values
// arraySize - Any Size
// target [0, 200] <-- 201 possible values
// valueSet [0, 101] <-- 102 possible values

include <iostream>

void PrintAllSumCombos(int target, int arraySize, int arrayOfValues[])
{
    bool valueSet[101];
    
    // Make sure all values are reset to false
    for (int i = 0; i < 101; i++)
    {
        valueSet = false;
    }
    
    // Populate 
    for (int i = 0; i < arraySize, i++)
    {
        valueSet[arrayOfValues[i]] = true;
    }
    
    // Iterate over the first half of the set and see if the number and its corresponding pair are both true.
    for (int i = 0; i < target/2; i++)
    {
        if ( (valueSet[i] == true) && (valueSet[target-i] == true) )
        cout << "(" << i << ", " << target-i << ")" << endl;
    }
    
    // Cleanup? Memory's in the stack
    
    return;
}