#include "NumCpp/Stats.hpp"
#include "NumCpp/Parse.hpp"
#include "NumCpp/Series.hpp"

#include <iomanip>  // std::fixed, std::setprecision

int main() {
  std::string fname = "../../data/Monthly_3_FamaFrench_Factors.csv";
  std::vector<std::vector<double>> data = *NumCpp::readCSV(fname, false);

  std::vector<double> log_returns;
  std::vector<double> returns;
  std::vector<double> dates;
  for (int i = 0; i < data.size(); i++) {
    dates.push_back(data[i][0]);

    double pct_return = data[i][1];  // excess returns
    double rf_rate = data[i][4];
    double return_relative = 1 + (rf_rate + pct_return)/100.0;

    log_returns.push_back(std::log(return_relative));
    returns.push_back((rf_rate + pct_return) / 100.0);
  }


  size_t window = 12;
  std::vector<double> vols;
  std::vector<double> vols_dates;
  for (size_t i = window-1; i < log_returns.size(); i++) {
    std::vector<double> tmp;
    for (size_t j = i - window + 1; j <= i; j++) {
      tmp.push_back(log_returns[j]);
    }
    vols.push_back(std::sqrt(12)*NumCpp::std(tmp));
    vols_dates.push_back(dates[i]);
  }

  NumCpp::Series volatilities(vols, vols_dates);
  volatilities.sort();
  volatilities.print();
  std::cout << std::endl;

  std::cout << "Historical US stock market volatility "
            << data[0][0] << "-" << data[data.size() - 1][0]
            << ": " << std::sqrt(12)*NumCpp::std(log_returns)
            << ". (Computed as annualized standard deviation of monthly log returns)"<< std::endl;

  std::cout << std::fixed;
  std::cout << std::setprecision(4);
  std::cout << "Statistic \t Returns \t Log-returns" << std::endl;
  std::cout << "     Mean \t " << NumCpp::mean(returns) << "          " << NumCpp::mean(log_returns) << std::endl;
  std::cout << "      Std \t " << NumCpp::std(returns) << "          " << NumCpp::std(log_returns) << std::endl;
  std::cout << "     Skew \t " << NumCpp::skew(returns) << "          " << NumCpp::skew(log_returns) << std::endl;
  std::cout << " Kurtosis \t " << NumCpp::kurtosis(returns) << "          " << NumCpp::kurtosis(log_returns) << std::endl;
}

