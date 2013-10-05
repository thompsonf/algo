#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

unsigned int binary_search( unsigned int key, unsigned int* search_array, unsigned int size)
{
	unsigned int cur_min = 0;
	unsigned int cur_max = size;
	unsigned int cur_mid;
	while(cur_max >= cur_min)
	{
		cur_mid = (cur_max + cur_min) / 2;
		if( search_array[cur_mid] < key )
			cur_min = cur_mid + 1;
		else if( search_array[cur_mid] > key )
			cur_max = cur_mid - 1;
		else
			return cur_mid;
	}
	return -1;
}

unsigned int nChoosek( unsigned int n, unsigned int k )
{
    if (k > n) return 0;
    if (k * 2 > n) k = n-k;
    if (k == 0) return 1;

    int result = n;
    for( int i = 2; i <= k; ++i ) {
        result *= (n-i+1);
        result /= i;
    }
    return result;
}

double mymin(double x, double y)
{
	if( x < 0 )
		return y;
	else if( y < 0 )
		return x;
	else
	{
		if( x < y )
			return x;
		else
			return y;
	}
}

int main()
{
    FILE* fp;
    fp = fopen("tsp.txt", "r");
    if( fp )
    {
        int num_nodes;
        double **pos;
        double **dists;
        {
        double x;
        double y;
        int i;
        int j;

        fscanf(fp, "%d", &num_nodes);
        pos = (double**)malloc(num_nodes * sizeof(double*));
        dists = (double**)malloc(num_nodes * sizeof(double*));
        for(i = 0; i < num_nodes; i++)
        {
            pos[i] = (double*)malloc(2 * sizeof(double));
            dists[i] = (double*)malloc(num_nodes * sizeof(double));
        }
        i = 0;
        while(fscanf(fp, "%lf %lf", &x, &y) != EOF)
        {
            pos[i][0] = x;
            pos[i][1] = y;
            i++;
        }
        for(i = 0; i < num_nodes; i++)
        {
            printf("%lf %lf\n", pos[i][0], pos[i][1]);
        }
        for( i = 0; i < num_nodes; i++ )
        {
            for( j = 0; j <= i; j++ )
            {
                double dx = pos[i][0] - pos[j][0];
                double dy = pos[i][1] - pos[j][1];
                double result = sqrt(dx * dx + dy * dy);
                dists[i][j] = result;
                dists[j][i] = result;
            }
        }
        }

        //At this point, we have dists[i][j] as the sqrt distance between i and j
        {
			double* prev_A = NULL;
			double* A = NULL;
			double* swap_double;

			unsigned int* prev_A_search_array = NULL;
			unsigned int* A_search_array = NULL;
			unsigned int* swap_uint;
			
			unsigned int num_combos;
			unsigned int prev_num_combos;

			unsigned int m;
			for( m = 2; m <= num_nodes; m++ )
			{
				num_combos = nChoosek(num_nodes - 1, m - 1);
				A_search_array = (unsigned int*)realloc(A_search_array, num_combos * sizeof(unsigned int));
				A = (double*)realloc(A, num_combos * (m - 1) * sizeof(double));

				printf("now on: %d\n", m);

				//Use Gosper's hack to fill in both A and A_search_array
				//of subsets of everything but the initial node using exactly m - 1 nodes
				//http://read.seas.harvard.edu/cs207/2012/
				//we need ONLY sets that include 1, so use m-1 and num_nodes-1, and then remember that everything is offset.
				//i.e. the subset represented by 011011 has nodes 1, 2, 3, 5, and 6
				unsigned int set = (1 << m - 1) - 1;
				unsigned int limit = 1 << (num_nodes - 1);
				unsigned int c;
				unsigned int r;
				unsigned int set_idx = 0;
				unsigned int j_pos;
				unsigned int subset;
				unsigned int j_sub_idx;
				unsigned int j;
				while( set < limit )
				{
					//insert set into the array that tracks all combinations
					A_search_array[set_idx] = set;

					//set is a string of 32 bits, with each 1 marking a node used in our subset
					//e.g. 0011000100 is a subset consisting of nodes 1, 4, 8, 9 (since 1 is always included)
					//Now we need to cycle through subsets minus one element
					j_pos = 1;
					j_sub_idx = 0;
					j = 1;
					//start check_pos at 1 and shift it left one bit each time
					while(j_pos < limit )
					{
						if( j_pos & set )
						{
							//zero-out the position
							subset = set & ~j_pos;
							//Now cycle through all possible end vertices of this set
							double min_val = -1;
							unsigned int end_vert_bit = 1;
							unsigned int end_vert_sub_idx = 0;
							unsigned int end_vert_int = 1;
							//set min_val for when k = 0 (i.e. the first node, called 1 in the slides)
							if( m == 2 )
								min_val = mymin(min_val, dists[j][0]);
							else
							{
								while( end_vert_bit < limit )
								{
									if( subset & end_vert_bit )
									{
										unsigned int arr_idx = binary_search(subset, prev_A_search_array, prev_num_combos) * (m - 2) + end_vert_sub_idx;
										min_val = mymin(min_val, prev_A[arr_idx] + dists[end_vert_int][j]);
										end_vert_sub_idx++;
									}
									end_vert_bit <<= 1;
									end_vert_int++;
								}
							}

							if( set_idx * (m - 1) + j_sub_idx >= num_combos * (m - 1) )
								printf("bad news!\n");
							if( j_sub_idx > m - 2 )
								printf("oops");
							A[set_idx * (m - 1) + j_sub_idx] = min_val;
							//do the necessary computations with the subset
							//need to find some way to turn subset into an array index
							//or I guess I could just use a hash table
							//think about using c++ map
							//since we put the count in there too, subset now contains BOTH the actual subset
							//AND the 
							j_sub_idx++;
						}
						j_pos <<= 1;
						j++;
					}

					//Get to the subset
					c = set & -set;
					r = set + c;
					set = (((r^set) >> 2) / c) | r;

					set_idx++;
				}
				swap_double = prev_A;
				prev_A = A;
				A = swap_double;

				swap_uint = prev_A_search_array;
				prev_A_search_array = A_search_array;
				A_search_array = swap_uint;

				prev_num_combos = num_combos;
			}
			double final_val = -1;
			for( m = 1; m < num_nodes; m++ )
			{
				final_val = mymin(final_val, prev_A[m - 1] + dists[m][0]);
			}
			printf("final number: %lf\n", final_val);
			free(A);
			free(prev_A);
			free(A_search_array);
			free(prev_A_search_array);
        }
    }
	system("pause");
}