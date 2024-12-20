#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <unordered_map>

int main(int argc, char** argv)
{
    using namespace std;
    
    if (argc != 2)
    {
        perror("Specify an input file!");
        return 1;
    }
    
    string filename = argv[1];    
    
    ifstream ifs(filename);
    if (!ifs)
    {
        perror("couldn't open");
        return 1;
    }
    
    vector<int> list1;
    vector<int> list2;
    
    for (string line; getline(ifs, line); )
    {
        istringstream stream(line);
        vector<int> nums;
        
        for (string num; stream >> num; )
        {
            try 
            {
                nums.push_back(stoi(num));
            } 
            catch (const std::invalid_argument& e) 
            {
                std::cerr << "Invalid number format: " << line << std::endl;
            } 
            catch (const std::out_of_range& e) 
            {
                std::cerr << "Number out of range: " << line << std::endl;
            }
        }
        
        if (nums.size() != 2)
        {
            perror("Line didn't have two numbers on it!");
            return 1;
        }
        
        list1.push_back(nums[0]);
        list2.push_back(nums[1]);
    }
    
    sort(list1.begin(), list1.end());
    sort(list2.begin(), list2.end());
    
    // for (int i = 0; i < list1.size(); i++) 
    // {
        // cout << list1[i] << '\n';
    // }

    // for (int i = 0; i < list2.size(); i++) 
    // {
        // cout << list2[i] << '\n';
    // }
    
    int sum;
    for (int i = 0; i < list1.size(); i++)
    {
        sum += abs(list1[i] - list2[i]);
    }
    
    cout << "P1: " << sum << '\n';
    
    // P2
    unordered_map<int, int> right_count;
    for (int i = 0; i < list2.size(); i++)
    {
        int curr = list2[i];
        // if (right_count.contains(curr))
        // {
            // // int count = right_count[curr];
            // // right_count[curr] = count + 1;
            // right_count[curr]++;
        // }
        // else
        // {
            // right_count[curr] = 1;
        // }
        right_count[curr]++;
    }
    
    // for (const auto& [key, value] : right_count)
    // {
        // std::cout << key << ": " << value << std::endl;
    // }
    
    int p2_score = 0;
    // C++ you have to initialize
    // cout << p2_score << '\n';
    for (int i = 0; i < list1.size(); i++)
    {
        int curr = list1[i];
        int count = right_count[curr];
        p2_score += curr * count;
        // cout << "curr: " << curr << ", count: " << count << ", p2: " << p2_score << '\n';
    }
    
    cout << "P2: " << p2_score << '\n';
    
    return 0;
}