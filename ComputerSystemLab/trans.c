/*
 * trans.c - Matrix transpose B = A^T
 *
 * Each transpose function must have a prototype of the form:
 * void trans(int M, int N, int A[N][M], int B[M][N]);
 *
 * A transpose function is evaluated by counting the number of misses
 * on a 1KB direct mapped cache with a block size of 32 bytes.
 */
#include <stdio.h>
#include "cachelab.h"

int is_transpose(int M, int N, int A[N][M], int B[M][N]);

/*
 * transpose_submit - This is the solution transpose function that you
 *     will be graded on for Part B of the assignment. Do not change
 *     the description string "Transpose submission", as the driver
 *     searches for that string to identify the transpose function to
 *     be graded.
 */
char transpose_submit_desc[] = "Transpose submission";
void transpose_submit(int M, int N, int A[N][M], int B[M][N])
{
    int i,j,k,l;
    int tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,tmp8;
    if(M==32&&N==32) {
        for(i=0; i<32; i+=8) {
            for(j=0; j<32; j++) {
                tmp1=A[i][j];
                tmp2=A[i+1][j];
                tmp3=A[i+2][j];
                tmp4=A[i+3][j];
                tmp5=A[i+4][j];
                tmp6=A[i+5][j];
                tmp7=A[i+6][j];
                tmp8=A[i+7][j];

                B[j][i]=tmp1;
                B[j][i+1]=tmp2;
                B[j][i+2]=tmp3;
                B[j][i+3]=tmp4;
                B[j][i+4]=tmp5;
                B[j][i+5]=tmp6;
                B[j][i+6]=tmp7;
                B[j][i+7]=tmp8;
            }
        }
    }

    if(M==64&&N==64) {
        for(i=0; i<64; i+=8) {
            for(j=0; j<64; j+=8) {
                for(k=i; k<i+4; k++) {
                    tmp1=A[k][j];
                    tmp2=A[k][j+1];
                    tmp3=A[k][j+2];
                    tmp4=A[k][j+3];
                    tmp5=A[k][j+4];
                    tmp6=A[k][j+5];
                    tmp7=A[k][j+6];
                    tmp8=A[k][j+7];

                    B[j][k]=tmp1;
                    B[j+1][k]=tmp2;
                    B[j+2][k]=tmp3;
                    B[j+3][k]=tmp4;

                    B[j][k+4]=tmp8;
                    B[j+1][k+4]=tmp7;
                    B[j+2][k+4]=tmp6;
                    B[j+3][k+4]=tmp5;
                }
                for(l=0; l<4; l++) {
                    tmp1=A[i+4][j+3-l];
                    tmp2=A[i+5][j+3-l];
                    tmp3=A[i+6][j+3-l];
                    tmp4=A[i+7][j+3-l];
                    tmp5=A[i+4][j+4+l];
                    tmp6=A[i+5][j+4+l];
                    tmp7=A[i+6][j+4+l];
                    tmp8=A[i+7][j+4+l];

                    B[j+4+l][i]=B[j+3-l][i+4];
                    B[j+4+l][i+1]=B[j+3-l][i+5];
                    B[j+4+l][i+2]=B[j+3-l][i+6];
                    B[j+4+l][i+3]=B[j+3-l][i+7];

                    B[j+3-l][i+4] = tmp1;
                    B[j+3-l][i+5] = tmp2;
                    B[j+3-l][i+6] = tmp3;
                    B[j+3-l][i+7] = tmp4;
                    B[j+4+l][i+4] = tmp5;
                    B[j+4+l][i+5] = tmp6;
                    B[j+4+l][i+6] = tmp7;
                    B[j+4+l][i+7] = tmp8;
                }
            }
        }
    }
     if(M==61&&N==67) {
        for(i=0; i<67; i+=17) {
            for(j=0; j<61; j+=17) {
                for(k=i; k<i+17&&k<67; k++) {
                    tmp1=-1;
                    tmp2=0;
                    for(l=j; l<j+17&&l<61; l++) {
                        if(l==k) {
                            tmp1=k;
                            tmp2=A[k][l];
                        } else {
                            B[l][k]=A[k][l];
                        }
                    }
                    if(tmp1!=-1) {
                        B[tmp1][tmp1]=tmp2;
                    }
                }
            }
        }
    }
    /*
    if(M==61&&N==67) {
        for(i=0; i<67; i+=8) {
            for(j=0; j<61; j+=8) {
                for(k=i; k<i+8&&k<67; k++) {
                    tmp1=-1;
                    tmp2=0;
                    for(l=j; l<j+8&&l<61; l++) {
                        if(l==k) {
                            tmp1=k;
                            tmp2=A[k][l];
                        } else {
                            B[l][k]=A[k][l];
                        }
                    }
                    if(tmp1!=-1) {
                        B[tmp1][tmp1]=tmp2;
                    }
                }
            }
        }
    }
    */
/*
    if(M==61&&N==67) {
        for(i=0; i<67; i+=16) {
            for(j=0; j<61; j+=16) {
                for(k=i; k<i+16&&k<67; k++) {
                    tmp1=-1;
                    tmp2=0;
                    for(l=j; l<j+16&&l<61; l++) {
                        if(l==k) {
                            tmp1=k;
                            tmp2=A[k][l];
                        } else {
                            B[l][k]=A[k][l];
                        }
                    }
                    if(tmp1!=-1) {
                        B[tmp1][tmp1]=tmp2;
                    }
                }
            }
        }
    }
*/

    /*
    if(M==64&&N==64){
    	for(i=0;i<64;i+=4)
    	{
    	    for(j=0;j<64;j++)
    	    {
    	        tmp1=A[i][j];
    	        tmp2=A[i+1][j];
    	        tmp3=A[i+2][j];
    	        tmp4=A[i+3][j];


    	        B[j][i]=tmp1;
    	        B[j][i+1]=tmp2;
    	        B[j][i+2]=tmp3;
    	        B[j][i+3]=tmp4;
    	    }
    	}
    }
    */
    /*
    if(M==64&&N==64)
    {
    	for(i=0;i<64;i+=8)
    	{
    	    for(j=0;j<64;j+=8)
    	    {
    	    	for(k=i;k<i+4;k++)
    	    	{
    	    	    tmp1=A[k][j];
    	            tmp2=A[k][j+1];
    	            tmp3=A[k][j+2];
    	            tmp4=A[k][j+3];
    	            tmp5=A[k][j+4];
    	            tmp6=A[k][j+5];
    	            tmp7=A[k][j+6];
    	            tmp8=A[k][j+7];
    	    	    B[j][k]=tmp1;
    	    	    B[j+1][k]=tmp2;
    	    	    B[j+2][k]=tmp3;
    	    	    B[j+3][k]=tmp4;
    	    	    B[j][k+4]=tmp5;
    	    	    B[j+1][k+4]=tmp6;
    	    	    B[j+2][k+4]=tmp7;
    	    	    B[j+3][k+4]=tmp8;
    	    	}
    	    	for(k=j;k<j+4;k++)
    	    	{
    	    	    tmp1=A[i+4][k];
    	    	    tmp2=A[i+5][k];
    	    	    tmp3=A[i+6][k];
    	    	    tmp4=A[i+7][k];
    	    	    tmp5=B[k][i+4];
    	    	    tmp6=B[k][i+5];
    	    	    tmp7=B[k][i+6];
    	    	    tmp8=B[k][i+7];

    	    	    B[k][i+4]=tmp1;
    	    	    B[k][i+5]=tmp2;
    	    	    B[k][i+6]=tmp3;
    	    	    B[k][i+7]=tmp4;
    	    	    B[k+4][i]=tmp5;
    	    	    B[k+4][i+1]=tmp6;
    	    	    B[k+4][i+2]=tmp7;
    	    	    B[k+4][i+3]=tmp8;
    	    	}
    	        for(k=i+4;k<i+8;k++)
    	        {
    	            tmp1=A[k][j+4];
    	            tmp2=A[k][j+5];
    	            tmp3=A[k][j+6];
    	            tmp4=A[k][j+7];
    	            B[j+4][k]=tmp1;
    	            B[j+5][k]=tmp2;
    	            B[j+6][k]=tmp3;
    	            B[j+7][k]=tmp4;
    	        }
    	    }
    	}
    }
    */
}

/*
 * You can define additional transpose functions below. We've defined
 * a simple one below to help you get started.
 */

/*
 * trans - A simple baseline transpose function, not optimized for the cache.
 */
char trans_desc[] = "Simple row-wise scan transpose";
void trans(int M, int N, int A[N][M], int B[M][N])
{
    int i, j, tmp;

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            tmp = A[i][j];
            B[j][i] = tmp;
        }
    }

}

/*
 * registerFunctions - This function registers your transpose
 *     functions with the driver.  At runtime, the driver will
 *     evaluate each of the registered functions and summarize their
 *     performance. This is a handy way to experiment with different
 *     transpose strategies.
 */
void registerFunctions()
{
    /* Register your solution function */
    registerTransFunction(transpose_submit, transpose_submit_desc);

    /* Register any additional transpose functions */
    registerTransFunction(trans, trans_desc);

}

/*
 * is_transpose - This helper function checks if B is the transpose of
 *     A. You can check the correctness of your transpose by calling
 *     it before returning from the transpose function.
 */
int is_transpose(int M, int N, int A[N][M], int B[M][N])
{
    int i, j;

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; ++j) {
            if (A[i][j] != B[j][i]) {
                return 0;
            }
        }
    }
    return 1;
}

