#include <mpi.h>
#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    int rank, size, namelen;

    cout << "Start" << endl;
    char name[MPI_MAX_PROCESSOR_NAME];
    MPI_Init(&argc, &argv);

    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Get_processor_name(name, &namelen);

    cout << "Hello from rank: " << rank << " running on: " << name << endl;

    MPI_Finalize();
    return 0;
}
