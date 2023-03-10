String cadena,texto;
int i,c,j,b,numero;
char n;
int leds[]={2,3,4,5,6,7,8,9};

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
  
  for(i=0; i<8; i++){
    pinMode(leds[i],OUTPUT);
  }
}

void loop() {
  if(Serial.available()>0){
    cadena = Serial.readString();
    c=0;
    
      while (c!=cadena.length()) {
      int Bin[]={0,0,0,0,0,0,0,0};
      j=-1;
      
      n = cadena.charAt(c);
      numero=int(n);
      Serial.println(String(numero));

      for(i=numero;i>0;){
        j++;
        b=i%2;
        Bin[j]=b;
        i=i/2;
      }

      int o=7;
      
      for(int m=0; m<8; m++){
      digitalWrite(leds[m],Bin[o]);
      Serial.println(Bin[o]);
      o--;
      }
      delay(3000);
      c++;
    }
    for(int m=0; m<8; m++){
    digitalWrite(leds[m],0);
    }
  }
}
