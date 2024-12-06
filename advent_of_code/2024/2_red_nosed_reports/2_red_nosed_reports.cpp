#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <format>

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

	// for (int i = 0; i < reports.size(); i++)
	// {
	// 	vector<int> report = reports[i];
	// 	for (int j = 0; j < report.size(); j++)
	// 	{
	// 		cout << report[j] << " ";
	// 	}
	// 	cout << '\n';
	// }

	int p1_safe_score = 0;
	for (int i = 0; i < reports.size(); i++)
	{
		vector<int> report = reports[i];
		bool is_safe = true;
		bool is_decrease_first = false;
		for (int j = 0; j < report.size() - 1; j++)
		{
			// cout << "hello world: " << j << '\n';
			int l = report[j];
			int r = report[j + 1];
			int diff = abs(l - r);
			if (diff <= 0 || diff > 3)
			{
				// cout << format("report {} is too different! {} {} ", i, l, r) << '\n';
				is_safe = false;
				break;
			}

			bool is_decrease = l > r;

			if (j == 0)
			{
				is_decrease_first = is_decrease;
				continue;
			}
			if (is_decrease_first != is_decrease)
			{
				// cout << format("report {} is not monotonic! {} {}", i, l, r) << '\n';
				is_safe = false;
				break;
			}
		}

		if (is_safe)
		{
			// cout << "report #: " << i << ", is_safe: " << is_safe << '\n';
			p1_safe_score++;
		}
	}

	cout << "P1: " << p1_safe_score << '\n';


	int p2_safe_score = 0;
	for (int i = 0; i < reports.size(); i++)
	{
		vector<int> report = reports[i];
		bool is_safe = true;
		int count_unsafe = 0;
		bool is_decrease_first = false;
		for (int j = 0; j < report.size() - 1; j++)
		{
			// cout << "hello world: " << j << '\n';
			int l = report[j];
			int r = report[j + 1];
			int diff = abs(l - r);
			if (diff <= 0 || diff > 3)
			{
				cout << format("report {} is too different! {} {} ", i, l, r) << '\n';
				count_unsafe++;
				if (count_unsafe < 2)
				{
					continue;
				}
				is_safe = false;
				break;
			}

			bool is_decrease = l > r;

			if (j == 0)
			{
				is_decrease_first = is_decrease;
				continue;
			}
			if (is_decrease_first != is_decrease)
			{
				cout << format("report {} is not monotonic! {} {}", i, l, r) << '\n';
				count_unsafe++;
				if (count_unsafe < 2)
				{
					continue;
				}
				is_safe = false;
				break;
			}

			// if (count_unsafe > 1)
			// {
			// 	is_safe = false;
			// 	break;
			// }
		}

		if (is_safe)
		{
			cout << "report #: " << i << ", is_safe: " << is_safe << '\n';
			p2_safe_score++;
		}
	}

	cout << "P2: " << p2_safe_score << '\n';
}

