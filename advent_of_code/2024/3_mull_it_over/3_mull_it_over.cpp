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

int parse(std::string_view input, std::unique_ptr<int> index);

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

	int* index = 0;
	std::unique_ptr<int> index_ptr{new int};
	*index_ptr = 1234;
	std::cout << &index_ptr << '\n';
	std::cout << *index_ptr << '\n';


	parse(input, index_ptr);
}

int parse(std::string_view input, std::unique_ptr<int> index) {
	int r = *index + 3;
	std::cout << "right index: " << r << '\n';
	if (r > input.length() - 1) {
		return 0;
	}
	std::string input_str{input};
	std::string op = input_str.substr(*index, *index + 3);

	std::cout << "op: " << op << '\n';
	return 1234;
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
