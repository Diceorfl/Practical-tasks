__global__ void DistKernel(float *a, float *b, int n)
{
 // Определение индекса потока
 int k = threadIdx.x + blockIdx.x*blockDim.x;
 // Обработка соответствующей порции данных
 for(int i = 0; i < n; i++)
 {
   float s = 0.0;
   for(int j = 0; j < n; j++)
     s+= (*(a + k * n + j) - *(a + i * n + j))*(*(a + k * n + j) - *(a + i * n + j));
   *(b + k * n + i) = s;
 }
}

// a, b – указатели на исходные массивы
// n – размер массивов (число элементов)
void dist_cuda(float *a, float *b, int n)
{
 int SizeInBytes = n * n * sizeof(float);
 // Указатели на массивы в видеопамяти
 float *a_gpu = NULL;
 float *b_gpu = NULL;
 // Выделение памяти под массивы на GPU
 cudaMalloc( (void **)&a_gpu, SizeInBytes );
 cudaMalloc( (void **)&b_gpu, SizeInBytes );
 // Копирование исходных данных из CPU на GPU
 cudaMemcpy(a_gpu, a, SizeInBytes, cudaMemcpyHostToDevice); // a_gpu = a
 // Задание конфигурации запуска ядра
 dim3 threads = dim3(16, 1); // 16 потоков в блоке
 dim3 blocks = dim3(n/threads.x, 1); // n/16 блоков в сетке
 // Запуск ядра
 DistKernel<<<blocks, threads>>>(a_gpu, b_gpu, n);
 // Копирование результата из GPU в CPU
 cudaMemcpy(b, b_gpu, SizeInBytes, cudaMemcpyDeviceToHost); // b_gpu = b
 // Освобождение памяти GPU
 cudaFree(a_gpu);
 cudaFree(b_gpu);
}
