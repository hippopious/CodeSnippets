// This class represents a moving window of data (float) and can calculate the average of this data
// If insufficient data is present in the window, the average of only the existing data will be used
class MovingAverageWindow
{
  private:
  
    float* AverageWindow;
    int sizeWindow;
    int recentDatapoint;
    int periodsOfDataCollected;
	
  public:
  
	//Public Constructor - Creates dynamically allocated objects
    void MovingAverageWindow(int size)
	{
	  delete AverageWindow;
	  AverageWindow = new float[size];
	  recentDatapoint = 0;
	  periodsOfDataCollected = 0;
	}
	
	// Destructor to remove data off the heap
	~MovingAverageWindow()
	{
	  delete AverageWindow;
	}
	
	// Can we consolidate the if-else? 
	float CalculateAverage()
	{
	  float sum = 0;
	  if (periodsOfDataCollected < sizeWindow)
	  {
	    for (int i = 0; i < sizeWindow; i++)
		{
		  sum += AverageWindow[i];
		}
		
		return sum / periodsOfDataCollected;
	  }
	  else
	  {
	    for (int i = 0; i < sizeWindow; i++)
		{
		  sum += AverageWindow[i];
		}
		return sum / sizeWindow;
	  }
	}
	
	// This function adds a more recent datapoint to the moving window and will overwrite the existing value if applicable
	// Move the current index, and then overwrite the data (this should overwrite the oldest datapoint)
	bool AddDataPoint(float newData)
	{
	  recentDatapoint = (recentDatapoint + 1) % sizeWindow;
	  AverageWindow[recentDatapoint] = newData;
	  periodsOfDataCollected++;
	}
    
}