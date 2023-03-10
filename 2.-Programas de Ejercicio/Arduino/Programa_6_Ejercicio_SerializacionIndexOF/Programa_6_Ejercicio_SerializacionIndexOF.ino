String texto,cadena,L[3];
int inicio,fin,i,led1=3,led2=5,led3=6;;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);//ms por defecto 1000
}

void loop() {
  i=0;
  inicio=0;
  
  if(Serial.available()>0){
    cadena = Serial.readString();//E001R056R255C 
    Serial.println(cadena);
      
    fin=cadena.indexOf("",inicio); 
    //Serial.println("Valor a descartar >> "+String(fin));
     
    while (fin!=-1) {
    texto = cadena.substring(inicio, fin); 
    //Serial.println("Valor obtenido >> "+String(texto));
    L[i]=texto;

    inicio = fin+1;
    fin = cadena.indexOf(',', inicio);
    //Serial.println("Valor de fin >> "+String(fin));
    i++;
  }
  
  texto=cadena.substring(inicio,cadena.length());
  //Serial.println("Valor obtenido >> "+String(texto));
  L[3]=texto;
  
  analogWrite(led1,L[1].toInt());i
  analogWrite(led2,L[2].toInt());
  analogWrite(led3,L[3].toInt());
  delay(1000);
  }
}
