#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

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
		perror("Couldn't open file!");
		return 1;
	}

	vector<vector<int>> reports;
	string report;
	while (getline(ifs, report))
	{
		istringstream stream(report);
		vector<int> levels;
		string level;

		while (stream >> level)
		{
			levels.push_back(stoi(level));
		}

		reports.push_back(levels);
	}

	for (int i = 0; i < reports.size(); i++)
	{
		vector<int> report = reports[i];
		for (int j = 0; j < report.size(); j++)
		{
			cout << report[j] << " ";
		}
		cout << '\n';
	}
}
