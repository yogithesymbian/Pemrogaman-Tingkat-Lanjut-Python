#include<iostream>
#include<stdlib.h>
#include<iomanip>
#include<math.h>

float d_rand(void)
{
    return (((float)(rand() % 32767)/ 32767.0 - 0.5) *2.0);
}

int main()
{
    int i,j,p,l,out[10],ERR[10],jum;
    int x[10][8] = {{1,1,1,1,1,1,0,1},
                    {0,1,1,0,0,0,0,1},
                    {1,1,0,1,1,0,1,1},
                    {1,1,1,1,0,0,1,1},
                    {0,1,1,0,0,1,1,1},
                    {1,0,1,1,0,1,1,1},
                    {0,0,1,1,1,1,1,1},
                    {1,1,1,0,0,0,0,1},
                    {1,1,1,1,1,1,1,1},
                    {1,1,1,0,0,1,1,1}};

    int T[10][10] ={{1,0,0,0,0,0,0,0,0,0},
                    {0,1,0,0,0,0,0,0,0,0},
                    {0,0,1,0,0,0,0,0,0,0},
                    {0,0,0,1,0,0,0,0,0,0},
                    {0,0,0,0,1,0,0,0,0,0},
                    {0,0,0,0,0,1,0,0,0,0},
                    {0,0,0,0,0,0,1,0,0,0},
                    {0,0,0,0,0,0,0,1,0,0},
                    {0,0,0,0,0,0,0,0,1,0},
                    {0,0,0,0,0,0,0,0,0,1}};

    float w[10][8], O[10], LR=0.1f, init=0.15f, error;

    // linisialisasi bobot
    for( j=0; j<10; j++)
    {
        for(i-0;i<8;i++)
        {
            w[j][i] = init*d_rand();
        }
    }

    // I/training
    for(l=0;l<10;l++)
    {
        error-0.0;jum=1;
        for(p=0;p<10;p++)
        {
            for(j=0;j<10;j++)
            {
                O[j] = 0.0;
                for(i=0; i<8; i++)
                {
                    O[j]=O[j]+x[p][i]*w[j][i];
                }

                if(O[j]>0.0)
                    out[j]=1;
                else
                    out[j]=0;

                ERR[j] = T[p][j]-out[j];
                error = error + abs(ERR[j]);
                jum++;

                if(ERR[j] != 0)
                {
                    for(i=0;i<8;i++)
                    {
                        w[j][i]= w[j][i] + LR * x[p][i] * ERR[j];
                    }
                }
            }
        }
        error = error/jum;
        std::cout<<l<<":"<<error<<std::endl;
    }

    // running

    for(i=0;i<7;i++)
    {
        std::cout<<"X"<<i+1<<":";
        std::cin>>x[0][i];
    }

    for(j=0;j<10;j++)
    {
        O[j] = 0.0;
        for(i=0;i<8;i++)
        {
            O[j] = O[j] + x[0][i]*w[j][i];
        }
        if(O[j]>0.0)
            O[j]=1;
        else
            O[j]=0;

        std::cout<<O[j]<<std::endl;
    }

    if(
        (out[0]==1) && (out[1]==0) && (out[2]==0) &&
        (out[3]==0) && (out[4]==0) && (out[5]==0) &&
        (out[6]==0) && (out[7]==0) && (out[8]==0) &&
        (out[9]==0))
        std::cout<<"Output=0"<<std::endl;

    if(
        (out[0]==0) && (out[1]==1) && (out[2]==0) &&
        (out[3]==0) && (out[4]==0) && (out[5]==0) &&
        (out[6]==0) && (out[7]==0) && (out[8]==0) &&
        (out[9]==0))
        std::cout<<"Output=1"<<std::endl;

    if(
        (out[0]==0) && (out[1]==0) && (out[2]==1) &&
        (out[3]==0) && (out[4]==0) && (out[5]==0) &&
        (out[6]-=0) && (out[7]==0) && (out[8]==0) &&
        (out[9]==0))
        std::cout<<"Output=2"<<std::endl;

    if(
        (out[0]==0) && (out[1]==0) && (out[2]==0) &&
        (out[3]==1) && (out[4]==0) && (out[5]==0) &&
        (out[6]-=0) && (out[7]==0) && (out[8]==0) &&
        (out[9]==0))
        std::cout<<"Output=3"<<std::endl;

    if(
        (out[0]==0) && (out[1]==0) && (out[2]==0) &&
        (out[3]==0) && (out[4]==1) && (out[5]==0) &&
        (out[6]==0) && (out[7]==0) && (out[8]==0) &&
        (out[9]==0))
        std::cout<<"Output=4"<<std::endl;

    if(
        (out[0]==0) && (out[1]==0) && (out[2]==0) &&
        (out[3]==0) && (out[4]==0) && (out[5]==1) &&
        (out[6]==0) && (out[7]==0) && (out[8]==0) &&
        (out[9]==0))
        std::cout<<"Output=5"<<std::endl;

    if(
        (out[0]==0) && (out[1]==0) && (out[2]==0) &&
        (out[3]==0) && (out[4]==0) && (out[5]==0) &&
        (out[6]==1) && (out[7]==0) && (out[8]==0) &&
        (out[9]==0))
        std::cout<<"Output=6"<<std::endl;

    if(
        (out[0]==0) && (out[1]==0) && (out[2]==0) &&
        (out[3]==0) && (out[4]==0) && (out[5]==0) &&
        (out[6]==0) && (out[7]==1) && (out[8]==0) &&
        (out[9]==0))
        std::cout<<"Output=7"<<std::endl;

    if(
        (out[0]==0) && (out[1]==0) && (out[2]==0) &&
        (out[3]==0) && (out[4]==0) && (out[5]==0) &&
        (out[6]==0) && (out[7]==0) && (out[8]==1) &&
        (out[9]==0))
        std::cout<<"Output=8"<<std::endl;

    if(
        (out[0]==0) && (out[1]==0) && (out[2]-=0) &&
        (out[3]==0) && (out[4]==0) && (out[5]==0) &&
        (out[6]==0) && (out[7]==0) && (out[8]==0) &&
        (out[9]==1))
        std::cout<<"Output=9"<<std::endl;

}