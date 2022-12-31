// AC

#include <bits/stdc++.h>

using namespace std;

int main() {
  ifstream input("badmilk.in");
  ofstream output("badmilk.out");

  int const MAX_DRINK_TIME = 999;
  int const MAX_SICK_TIME = 9999;

  int N, M, D, S;
  input >> N >> M >> D >> S;

  vector<vector<int>> drinkRecord(M + 1, vector<int>(N + 1, MAX_DRINK_TIME));
  for (int d = 0; d < D; d++) {
    int p, m, t;
    input >> p >> m >> t;
    drinkRecord[m][p] = min(drinkRecord[m][p], t);
  }

  vector<int> sickTime(N + 1, MAX_SICK_TIME);
  for (int s = 0; s < S; s++) {
    int p, t;
    input >> p >> t;
    sickTime[p] = t;
  }

  int dosesNeeded = 0;
  for (int m = 1; m <= M; m++) {
    auto const& milkRecord = drinkRecord[m];
    bool maybeBadMilk = true;
    int doses = 0;
    for (int p = 1; p <= N; p++) {
      if (sickTime[p] <=
          milkRecord[p]) {  // Person got sick at or before drank this milk
        maybeBadMilk = false;
        break;
      }
      if (milkRecord[p] < MAX_DRINK_TIME) {  // A person drank this milk
        doses++;
      }
    }
    if (maybeBadMilk) {
      dosesNeeded = max(dosesNeeded, doses);
    }
  }

  output << dosesNeeded << endl;
  return 0;
}
