/// AC

#include <bits/stdc++.h>

// #include <cstdio>
// #include <ios>
// #include <iostream>
// #include <string>
// #include <unordered_map>
// #include <vector>

using namespace std;

struct Bits {
  vector<int> data_;

  void set(size_t index) {
    if (index >= data_.size()) {
      data_.resize(index + 1);
    }
    data_[index] = 1;
  }
};

int count_both_set_bits(Bits const& set1, Bits const& set2) {
  int count = 0;
  for (int i = 0; i < min(set1.data_.size(), set2.data_.size()); i++) {
    if (set1.data_[i] && set2.data_[i]) {
      count++;
    }
  }
  return count;
}

int main() {
  //   ios::sync_with_stdio(false);
  //   input.tie(nullptr);

  ifstream input("guess.in");
  ofstream output("guess.out");

  int N, K;
  string animal, characteristic;

  input >> N;
  unordered_map<string, size_t> ch2index;
  size_t num_ch = 0;
  vector<Bits> animals;
  for (int i = 0; i < N; i++) {
    input >> animal >> K;
    Bits ch_bits;
    for (int j = 0; j < K; j++) {
      input >> characteristic;

      size_t index;
      auto it = ch2index.find(characteristic);
      if (it == ch2index.end()) {
        ch2index[characteristic] = index = num_ch;
        num_ch++;
      } else {
        index = it->second;
      }
      ch_bits.set(index);
    }
    animals.push_back(ch_bits);
  }

  int result = 0;
  for (int i = 0; i < animals.size(); i++) {
    for (int j = i + 1; j < animals.size(); j++) {
      int n = count_both_set_bits(animals[i], animals[j]);
      result = max(result, n);
    }
  }

  output << result + 1 << endl;
  return 0;
}
