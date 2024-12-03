#include <vector>
#include <iostream>
#include <string>
#include <fstream>

int main() 
{
    // using namespace std;
    
    std::ifstream ifs("sample.txt");
    if (!ifs)
    {
        perror("couldn't open");
        return 1;
    }
    
    std::vector<std::string> list1;
    std::vector<std::string> list2;
    
    for (std::string line; std::getline(ifs, line); )
    {
        list1.push_back(line);
    }
    
    for (int i = 0; i < list1.size(); i++) 
    {
        std::cout << list1[i] << '\n';
    }
    
    return 0;
}