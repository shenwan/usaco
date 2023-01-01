// AC except case 11

#include <bits/stdc++.h>

#include <cstdio>
#include <ios>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

struct ContactRecord {
  int t;
  int x;
  int y;

  ContactRecord(int tt, int xx, int yy) : t(tt), x(xx), y(yy) {}
};

inline bool operator<(ContactRecord const& left, ContactRecord const& right) {
  return left.t < right.t;
}

string format(int maxK, int limit) {
  if (maxK >= limit) return "Infinity";
  return to_string(maxK);
}

bool contact(int K, int x, int y, vector<int> const& currentState,
             vector<int>& oldState, vector<int>& shakes) {
  if (oldState[x] == 0 && oldState[y] == 0) {
    return true;
  }
  if (oldState[x] && oldState[y]) {
    // It's OK if # of shakes exceed K
    ++shakes[x];
    ++shakes[y];
    return true;
  }
  if (oldState[x]) {
    if (shakes[x] >= K) {
      return true;
    }
    // x infects y
    ++shakes[x];
    oldState[y] = 1;
    if (currentState[y] == 0) {
      cout << "Cow " << y
           << ": currentState is healthy, but it was infected by cow " << x
           << endl;
    }
    return currentState[y] == 1;
  }
  if (oldState[y]) {
    if (shakes[y] >= K) {
      return true;
    }
    // y infects x
    ++shakes[y];
    oldState[x] = 1;
    if (currentState[x] == 0) {
      cout << "Cow " << x
           << ": currentState is healthy, but it was infected by cow " << y
           << endl;
    }
    return currentState[x] == 1;
  }
  assert(false);
}

bool simulate(int N, int K, vector<ContactRecord> const& contactRecords,
              vector<int> const& currentState, vector<int>& oldState) {
  vector<int> shakes(N + 1, 0);
  for (auto const& contactRecord : contactRecords) {
    if (!contact(K, contactRecord.x, contactRecord.y, currentState, oldState,
                 shakes)) {
      return false;
    }
  }
  return true;
}

int main() {
  //   istream& input = cin;
  //   ostream& output = cout;
  ifstream input("tracing.in");
  ofstream output("tracing.out");

  int N, T;
  input >> N >> T;

  vector<int> currentState(N + 1, 0);
  int sickCows = 0;
  int sickCow;
  for (int n = 1; n <= N; ++n) {
    char c;
    input >> c;
    currentState[n] = c - '0';
    if (currentState[n]) {
      ++sickCows;
      sickCow = n;
    }
  }
  assert(sickCows > 0);
  if (sickCows == 1) {
    for (int i = 0; i < T; ++i) {
      int t, x, y;
      input >> t >> x >> y;
      if (x == sickCow || y == sickCow) {
        // With any K > 0, another cow would be infected.
        output << "1 0 0" << endl;
        return 0;
      }
    }
    // The sick cow has not shaken hoof with any cows.
    output << "1 0 Infinity" << endl;
    return 0;
  }

  vector<ContactRecord> contactRecords;
  vector<int> numShakes(N + 1, 0);
  for (int i = 0; i < T; ++i) {
    int t, x, y;
    input >> t >> x >> y;
    contactRecords.push_back(ContactRecord(t, x, y));
    ++numShakes[x];
    ++numShakes[y];
  }
  sort(contactRecords.begin(), contactRecords.end());
  int maxNumShakes = *max_element(numShakes.begin(), numShakes.end());
  cout << "maxNumShakes: " << maxNumShakes << endl;

  int possibleCows = 0;
  int minK = INT_MAX;
  int maxK = 0;

  for (int patientZero = 1; patientZero <= N; patientZero++) {
    if (currentState[patientZero] == 0) {
      // patient zero cannot be healthy in the current state
      continue;
    }

    bool possiblePatientZero = false;
    cout << endl << "patient zero: " << patientZero << endl;
    for (int K = 1; K <= maxNumShakes; K++) {
      vector<int> oldState(N + 1, 0);
      oldState[patientZero] = 1;

      cout << "simulate(K=" << K << ")" << endl;
      if (!simulate(N, K, contactRecords, currentState, oldState)) {
        break;
      }

      if (oldState == currentState) {
        cout << "Found possible patient zero: " << patientZero << ", K=" << K
             << endl;
        possiblePatientZero = true;
        minK = min(minK, K);
        maxK = max(maxK, K);
      } else {
        cout << "Found impossible patient zero: " << patientZero
             << ", oldState: ";
        copy(oldState.begin(), oldState.end(),
             ostream_iterator<int>(cout, " "));
        cout << endl;
      }
    }

    if (possiblePatientZero) {
      ++possibleCows;
    }
  }

  output << possibleCows << ' ' << minK << ' ' << format(maxK, maxNumShakes)
         << endl;
  return 0;
}
