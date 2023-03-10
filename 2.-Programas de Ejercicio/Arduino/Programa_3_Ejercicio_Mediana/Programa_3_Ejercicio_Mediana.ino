int potenciometro = A0;
int tamMuestra = 10;
int i,j,k,m,aux,valor, L[10];
double med;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  for(i=0;i<tamMuestra; i++){
    valor=analogRead(potenciometro);
    Serial.println(valor);
    L[i]=valor;
    delay(1000);
  }
  for(j=0;j<tamMuestra-1;j++){
    for(k=0;k<tamMuestra-j-1;k++){
      if(L[k+1]<L[k]){
        aux = L[k + 1];
        L[k + 1] = L[k];
        L[k] = aux;
      }
    }
  }
  Serial.println("<<ORDENADO>>");
  for(m=0; m<tamMuestra; m++){
    Serial.println(L[m]); 
  }

  if(tamMuestra%2==0){
    med=((L[tamMuestra/2]+L[(tamMuestra/2)-1])/2);
  }else{
    med=L[int(tamMuestra/2)];
  }
  
  Serial.println("MEDIANA >> "+String(med));
  delay(1000);
  Serial.println("<<VALORES>>");
}
