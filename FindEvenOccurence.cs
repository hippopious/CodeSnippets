using System.IO;
using System.Collections.Generic;
using System;

class Program
{
    // Iterate the input and populate a dictionary with occurences values
    // Then iterate through the dictionary and find the first
    // key that has an even amount of occurrences
    static void FindEvenOccurence(List<int> input)
    {
        // Displaying input
        Console.WriteLine("Input Values:");
        foreach (int number in input)
        {
            Console.Write("{0} ", number);
        }
        Console.WriteLine("\n");
     
        Dictionary<int, int> occurrences = new Dictionary<int, int>();
        
        foreach (int number in input)
        {
            if (occurrences.ContainsKey(number))
            {
                occurrences[number] = occurrences[number] + 1;
            }
            else
            {
                occurrences.Add(number, 1);
            }
        }
        
        foreach( KeyValuePair<int, int> kvp in occurrences )
        {
            if ( (kvp.Value % 2) == 0 )
            {
                Console.WriteLine("Number {0} has {1} occurences.",
                    kvp.Key, kvp.Value);
            }
        }

    }

    static void Main()
    {
        Console.WriteLine("Hello, World!");
        
        // Populate some values
        List<int> randomNumbers = new List<int>();
        randomNumbers.Add(3);
        randomNumbers.Add(1);
        randomNumbers.Add(1);
        randomNumbers.Add(5);
        randomNumbers.Add(1);
        randomNumbers.Add(5);
        randomNumbers.Add(3);
        randomNumbers.Add(7);
        randomNumbers.Add(5);

        FindEvenOccurence(randomNumbers);
    }
}