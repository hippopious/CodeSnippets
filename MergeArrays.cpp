bool MergeArrays(int numberOfArrays, int** inputArray, int ArraySizes, int* outputArray)
{
    bool lowestNumFound = false;
    int currentIndexes = new int[numberOfArrays];
    int lowestIndex = 0;
    int currentOutputIndex = 0;
    
    while(1) // Not great
    {
        for ( int i = 0; i < numberOfArrays; i++ )
        {
            // If this particular array is exhausted. Skip it.
            if ( i >= ArraySizes[i] )
            {
                continue;
            }
            
            if ( !lowestNumFound )    // We haven't found a lowest number yet during this loop
            {
                lowestIndex = i;
                lowestNumFound = true;
            }
            
            if ( inputArray[i][currentIndexes[i]] <= lowestIndex )    // Index into the data the fetch the value and check for lowest condition
            {
                lowestIndex = i;
            }
        }
        
        // If we found a lowest value (or a tie for the lowest value), then we copy it to the output array
        // This is only impossible if all arrays are exhausted. In that case, we're done.
        if ( lowestNumFound )
        {
            outputArray[currentOutputIndex] = inputArray[currentLowestIndex][currentIndexes[lowestIndex]];
            currentOutputIndex++;
        }
        else    // We're all done. Exit the while loop.
        {
            break;
        }
        
    }

    // Cleanup of memory
    delete [] currentIndexes;
    currentIndexes = null;
    return true;
}

