// Determine if a sequence of ints inside an array sum to a value (all positive values)

bool (int dataArray, int dataArraySize, int sumValue)
{
    int trailingIndex = 0;
    int currentIndex = 0;
    int runnningTotal = 0;
    
    // Get some conditions out of the way
    if (dataArraySize == 0)
    {
        return false;
    }
    else if (dataArraySize == 1)
    {
        if (dataArray[0] == sumValue)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    
    // Outer loop will advance the current index. Inner loop will advance the inner loop as necessary.
 
    runningTotal = dataArray[0];
    do
    {
        currentIndex++;
        runningTotal = runningTotal + dataArray[currentIndex];
        
        // This will subtract values off the trailing sequence until the sequence's sum is less than or equal
        // to the value we're looking for
        while (runningTotal > sumValue)
        {
            // Don't let the trailing index be bigger than the current index
            // We will try to drop the runningTotal later
            if (trailingIndex >= currentIndex)
            {
                break;
            }
            
            runningTotal = runningTotal - dataArray[trailingIndex];
            trailingIndex++;
        }
        
        if (runningTotal == sumValue)
        {
            return true;
        }
    }
    while (currentIndex < dataArraySize - 1)
    
    // currentIndex has reached the end of the array and no sequence sum was found to match the value
    return false;
}


// Another Approach