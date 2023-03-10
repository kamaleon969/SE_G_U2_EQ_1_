int potenciometro = A0;
int tamMuestra = 30;
int i,j,k,L,m,valor,aux;
String str;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  int Lista[tamMuestra];
  for(i=0;i<tamMuestra; i++){
    valor=analogRead(potenciometro);
    Serial.println(valor);
    Lista[i]=valor;
    delay(1000);
  }
  for(j=0;j<tamMuestra-1;j++){
    for(k=0;k<tamMuestra-j-1;k++){
      if(Lista[k+1]<Lista[k]){
        aux = Lista[k + 1];
        Lista[k + 1] = Lista[k];
        Lista[k] = aux;
      }
    }
  }
  delay(1000);
  int cont=1;
  int may=0,mod=0;
  for(L=0;L<tamMuestra-1;L++){
    if(Lista[L]==Lista[L+1]){
      cont+=1;
    }else{
      if(cont>may){
        mod=Lista[L];
        may=cont;
      }
      cont=1;
    }
  }
  Serial.println("ORDENADO");
  for(m=0; m<tamMuestra; m++){
    Serial.println(Lista[m]); 
  }
  Serial.println("MODA "+String(mod));
  Serial.println("CANTIDAD REPETIDA "+String(may));
}
