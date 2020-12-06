#include <iostream>
#include <cuda.h>
#include <cuda_runtime.h>
#include <chrono>

using namespace std;
// Описание внешней функции, располагающейся в .cu-файле
void dist_cuda(float *a, float *b, int n);
// Размер вектора (должен быть кратен 16)
const int N = 1024;
// Вектора
float a[N*N], b[N*N];
int main()
{
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      *(a + i * N + j) = (i + 1) * 2 + (j + 1);
  using namespace std::chrono;
  auto start = high_resolution_clock::now();
  dist_cuda(a, b, N);
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  for (int i = 0; i < 5; i++)
  {
    for (int j = 0; j < 5; j++)
      cout << *(b + i * N + j) << " ";
    cout << endl;
  }
  cout << duration.count() / 1000000.0 << " sec " << endl;
  getchar();
  return 0;
}
