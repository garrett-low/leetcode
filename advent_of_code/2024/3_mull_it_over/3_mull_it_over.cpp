#include <iostream>
#include <string>
#include <string_view>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <format>
#include <unordered_set>
#include <memory>

void read_file(std::string_view filename, std::string &input);

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		perror("Specify an input file!");
		return 1;
	}

	std::string filename = argv[1];

	std::string input{};
	read_file(filename, input);
	std::cout << input << '\n';


}

void read_file(std::string_view filename, std::string &input)
{
	std::string file{filename};
	std::ifstream ifs(file);
	if (!ifs)
	{
		perror("Couldn't open file!");
		return;
	}

	std::getline(ifs, input);
}
