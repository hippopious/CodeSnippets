main()
{
    int x_Size = 100;
    int y_Size = 50;
    
    bool** myArray = null;
    
    myArray = new bool* [x_Size];
    
    for (int i = 0; i < x_Size; i++)
    {
        myArray[i] = new bool[y_Size];
    }
    
    // Optional: populate the array if you like.
    
    // Cleanup
    
    for (int i = 0; i < x_Size; i++)
    {
        delete[] myArray[i];
    }
    delete[] myArray;
    myArray = NULL;
    
}

void Iterate2DArray(bool** arrayPointer, int x_Size, int y_Size)
{
    bool tempVar = false;

    for (int i = 0; i < x_Size; i++)
    {
        for (int j = 0; j < y_Size; j++)
        {
            tempVar = arrayPointer[x_Size][y_Size];
        }
    }
}