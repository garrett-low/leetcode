#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <format>
#include <unordered_set>

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
}
