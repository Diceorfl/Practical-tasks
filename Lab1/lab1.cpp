#include <iostream>
#include <cmath>
#include <string>
#include <chrono>
#include <omp.h>

using std::cout;
using std::cin;
using std::endl;
using std::string;

double f(double);
double trapez_intgrl_atomic(double, double, int, string);
double trapez_intgrl_critical(double, double, int, string);
double trapez_intgrl_locks(double, double, int, string);
double trapez_intgrl_reduction(double, double, int, string);
void trapez_intgrl(double(*)(double, double, int, string), string, int);

int main()
{
  int N;
  cout << "Please enter the number of points: ";
  cin >> N;
  int threads;
  cout << "Please enter the number of threads:";
  cin >> threads;
  if(threads < 1 || threads > omp_get_max_threads())
    threads = omp_get_max_threads();
  omp_set_num_threads(threads);
  std::cout.precision(5);
  std::cout.setf(std::ios::fixed);
  trapez_intgrl(trapez_intgrl_atomic,"Atomic", N);
  trapez_intgrl(trapez_intgrl_critical,"Critical", N);
  trapez_intgrl(trapez_intgrl_locks,"Locks", N);
  trapez_intgrl(trapez_intgrl_reduction,"Redaction", N);
  system("PAUSE");
  return 0;
}

double f(double x)
{
  return 1/(x*x)*pow(sin(1/x),2);
}

double trapez_intgrl_atomic(double A, double B, int N, string table_line)
{
  using namespace std::chrono;
  auto start = high_resolution_clock::now();
  const double eps = (B - A)/N;
  double t_intgrl = 0;
  #pragma omp parallel for
  for(int step = 0; step < N; step++)
  {
    double x1 = A + step*eps;
    double x2 = A + (step + 1)*eps;
    #pragma omp atomic
    t_intgrl+= 0.5*(x2 - x1)*(f(x1) + f(x2));
  }
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  cout << table_line <<  "\ttime(sec) = "<<  duration.count() / 1000000.0 << "\tres = " << t_intgrl << endl;
  return t_intgrl;
}

double trapez_intgrl_critical(double A, double B, int N, string table_line)
{
  using namespace std::chrono;
  auto start = high_resolution_clock::now();
  const double eps = (B - A)/N;
  double t_intgrl = 0;
  #pragma omp parallel for
  for(int step = 0; step < N; step++)
  {
    double x1 = A + step*eps;
    double x2 = A + (step + 1)*eps;
    #pragma omp critical
    t_intgrl+= 0.5*(x2 - x1)*(f(x1) + f(x2));
  }
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  cout << table_line <<  "\ttime(sec) = "<<  duration.count() / 1000000.0 << "\tres = " << t_intgrl << endl;
  return t_intgrl;
}

double trapez_intgrl_locks(double A, double B, int N, string table_line)
{
  using namespace std::chrono;
  auto start = high_resolution_clock::now();
  const double eps = (B - A)/N;
  double t_intgrl = 0;
  omp_lock_t lock;
  omp_init_lock(&lock);
  #pragma omp parallel for
  for(int step = 0; step < N; step++)
  {
    double x1 = A + step*eps;
    double x2 = A + (step + 1)*eps;
    omp_set_lock(&lock);
    t_intgrl+= 0.5*(x2 - x1)*(f(x1) + f(x2));
    omp_unset_lock(&lock);
  }
  omp_destroy_lock(&lock);
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  cout << table_line <<  "\ttime(sec) = "<<  duration.count() / 1000000.0 << "\tres = " << t_intgrl << endl;
  return t_intgrl;
}

double trapez_intgrl_reduction(double A, double B, int N, string table_line)
{
  using namespace std::chrono;
  auto start = high_resolution_clock::now();
  const double eps = (B - A)/N;
  double t_intgrl = 0;
  #pragma omp parallel for reduction(+:t_intgrl)
  for(int step = 0; step < N; step++)
  {
    double x1 = A + step*eps;
    double x2 = A + (step + 1)*eps;
    t_intgrl+= 0.5*(x2 - x1)*(f(x1) + f(x2));
  }
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  cout << table_line <<  "\ttime(sec) = "<<  duration.count() / 1000000.0 << "\tres = " << t_intgrl << endl;
  return t_intgrl;
}

void trapez_intgrl(double(*Function)(double, double, int, string), string func_name, int N)
{
  double A = 0.00001;
  double B = 0.0001;
  cout << func_name << endl;
  for(int i = 0; i < 7; i++)
  {
    string table_line = "A = " + std::to_string(A) + "\t" + "B = " + std::to_string(B);
    Function(A,B,N, table_line);
    A*= 10;
    B*= 10;
  }

}
