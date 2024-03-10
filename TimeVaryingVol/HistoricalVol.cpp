#include "NumCpp/Stats.hpp"
#include "NumCpp/Parse.hpp"

int main() {
  std::vector<std::vector<double>> data = *NumCpp::readCSV("../../data/Monthly_3_FamaFrench_Factors.csv");

  std::vector<double> log_returns;
  for (int i = 0; i < data.size(); i++) {
    double pct_return = data[i][0];  // excess returns
    double rf_rate = data[i][3];
    double return_relative = 1 + (rf_rate + pct_return)/100.0;
    log_returns.push_back(std::log(return_relative));
  }

  std::cout << std::sqrt(12)*NumCpp::std(log_returns) << std::endl;
}

