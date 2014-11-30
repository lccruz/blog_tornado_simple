#include <iostream>

using namespace std;

int num_pecas;
int p_final[2];
int p_inicial[2];


int domino(int inicial, int matriz[][3], int espacos){

    if (!espacos){
        //testa se a ultima peca se encaixa
        if(inicial == p_final[0]){
            return 1;
        }
    }
    else{
        for(int i=0; i<num_pecas; i++){
            if (!matriz[i][2]){
                // marca a peca como usada
                matriz[i][2] = 1;
                if(matriz[i][1] == inicial){
                    //manta a peca contraria
                    int lado_a = domino(matriz[i][0], matriz, espacos - 1);
                    if (lado_a){
                        return lado_a;
                    }
                }
                if(matriz[i][0] == inicial){
                    //manta a peca contraria
                    int lado_b = domino(matriz[i][1], matriz, espacos - 1);
                    if (lado_b){
                        return lado_b;
                    }
                }
                // desmarca
                matriz[i][2] = 0;
            }
        }
    }

    return 0;
}


int main(){
    int espacos;
    cin >> espacos;
    while(espacos){
        cin >> num_pecas;
        int matriz[num_pecas][3];
        cin >> p_inicial[0] >> p_inicial[1];
        cin >> p_final[0] >> p_final[1];
        for(int i=0; i < num_pecas; i++){
            cin >> matriz[i][0] >> matriz[i][1];
            matriz[i][2] = 0;
        }
        //passa a primeira peca sem modificar
        int dio = domino(p_inicial[1], matriz, espacos);
        if(dio){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
        cin >> espacos;
    }
}

/*
    p_inicial[0] = 0;
    p_inicial[1] = 1;
    p_final[0] = 3;
    p_final[1] = 4;
    int espacos = 1;
    num_pecas = 4;
    int matriz[4][3] = {
        {2,1,0},
        {5,6,0},
        {2,2,0},
        {3,2,0}
    };
    p_inicial[0] = 0;
    p_inicial[1] = 1;
    p_final[0] = 3;
    p_final[1] = 4;
    int espacos = 2;
    num_pecas = 4;
    int matriz[4][3] = {
        {1,4,0},
        {4,4,0},
        {3,2,0},
        {5,6,0}
    };
*/
